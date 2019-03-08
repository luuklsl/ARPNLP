import json
import re

from newsapi import NewsApiClient
import spacy
import textacy

import sql

from API import API_KEY

nlp = spacy.load('en_core_web_sm')
en = textacy.load_spacy('en_core_web_sm')

categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']


def get_news(API_KEY):
    """"A rudimentary way to retrieve some recent news will be improved upon, but serves purpose so far. Also dumps
    news in dumpfile.json for possible manual inspection"""
    # Init tne newsapi client
    newsapi = NewsApiClient(api_key=API_KEY)

    # Code below is mainly useful for getting the sources in a country, or from a specific type of news category
    # sources = newsapi.get_sources(language='en', category='general')
    # print(sources)

    # get_everything requires either a query, sources and domain
    # articles = newsapi.get_everything(sources='reuters')
    # print(articles)

    for cat in categories:
        top_articles = newsapi.get_top_headlines(country='gb', category=cat, page_size=100)

        with open('dumpfile' + str(cat) + '.json', 'w') as file:
            json.dump(top_articles, file, indent=4)
            print('dumped')


def do_NLP_magic(data):
    """"Function to call spaCy NLP magic. Reads from file so we aren't forced to
    do API calls all the time if we don't want to"""

    # Literally the example on the spaCy website, seems to work okay enough for now
    # nlp = spacy.load('en_core_web_sm')
    doc = nlp(data)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)


# Render results to text displayer, go to http://127.0.0.1:5000/ to view the results of this
# displacy.serve(doc, style='ent')


def load_and_process_data(cat):
    # Read the file we just created, as we are in early stages i recommend keeping this here
    with open('dumpfile' + str(cat) + '.json') as file:
        x = json.loads(file.read())

    # horrible code, but it makes clear what it does, if not, use prints ;)

    data = []
    for article in x['articles']:

        if (article['title'] is not None) and (article['content'] is not None) and (article['description'] is not None):
            """""Build a dict with non-processed and processed data (for manual checking later on)"""

            result = {'title': article['title'],
                      'description': article['description'],
                      'content': article['content'],
                      'title_pre': textacy.preprocess_text(article['title'], lowercase=True, no_punct=True),
                      'description_pre': textacy.preprocess_text(article['description'], lowercase=True, no_punct=True),
                      'content_pre': textacy.preprocess_text(article['content'], lowercase=True, no_punct=True)}
            data.append(result)

    # pprint(data)
    return_data = []
    """Everything within the loop below will be dumped to sql later on"""
    for entry in data:
        data_store = dict(entry)
        for key_val in entry.keys():
            # print(key_val)
            if key_val == 'title':
                entry[key_val] = re.sub(r'( - [a-zA-Z ]+$)', '', entry[key_val])
            entities, tokens, dependencies = str(), str(), str()

            doc = nlp(entry[key_val])
            for ent in doc.ents:
                # print(ent.text, ent.start_char, ent.end_char, ent.label_)
                entities += str(ent.text) + ", " + str(ent.label_) + "; "

            for token in doc:
                # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                #       token.shape_, token.is_alpha, token.is_stop)
                tokens += str(token.text) + ", " + str(token.lemma_) + ", " + str(token.pos_) + ", " + str(
                    token.tag_) + ", " + str(token.dep_) + "; "

            for token in doc:
                # print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])
                dependencies += str(token.text) + ", " + str(token.dep_) + ", " + str(token.head.text) + ", " + str(
                    token.head.pos_) + ", " + str([child for child in token.children]) + "; "
            # print(entities + '\n\n' + tokens + '\n\n' + dependencies)

            data_store[str(key_val) + "_" + "entities"] = entities
            data_store[str(key_val) + "_" + "tokens"] = tokens
            data_store[str(key_val) + "_" + "dependencies"] = dependencies

            # print('\n')
        return_data.append(data_store)
        # print('\n')
    assert (len(return_data) == len(data))
    return return_data


# get_news(API_KEY)   #Turn this off so you don't do API calls all the time

for cat in categories:
    data = load_and_process_data(cat)

    # print(data[0])
    # print(type(data))

    sql.dump_data(data, cat)
