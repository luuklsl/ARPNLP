from newsapi import NewsApiClient
from pprint import pprint
import json
import spacy
from spacy import displacy
import textacy
import sqlite3

from API import API_KEY

nlp = spacy.load('en_core_web_sm')
en = textacy.load_spacy('en_core_web_sm')
con = sqlite3.connect('storage.db')


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

    top_articles = newsapi.get_top_headlines(country='us')

    with open('dumpfile.json', 'w') as file:
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


def load_data_from_dumpfile():
    # Read the file we just created, as we are in early stages i recommend keeping this here
    with open('dumpfile.json') as file:
        x = json.loads(file.read())
        # print(x)

    # horrible code, but it makes clear what it does, if not, use prints ;)
    # article = dict((x['articles'][4]))
    # print(len(((x['articles']))))
    # pprint(x['articles'])
    data = []
    for article in x['articles']:
        # print (article)
        # title_pre = article['title']
        # description_pre = article['description']
        # content_pre = article['content']
        # print (title_pre + "\n" + description_pre +"\n" + content_pre)
        if article['title'] is not None and (article['content'] is not None):
            # print (article['content'] == article['description'])
            result = {'title': textacy.preprocess_text(article['title'], lowercase=True, no_punct=True),
                      'description': textacy.preprocess_text(article['description'], lowercase=True, no_punct=True),
                      'content': textacy.preprocess_text(article['content'], lowercase=True, no_punct=True)}
            data.append(result)

    pprint(data)
    for entry in data:
        for key_val in entry.keys():
            # print(entry[key_val])
            # print('\n')
            doc = nlp(entry[key_val])
            for ent in doc.ents:
                print(ent.text, ent.start_char, ent.end_char, ent.label_)
            print('\n')

            # for ents in entry[key_val]:
            #     print (ents)

        # article_contents = (title + "\n" + description + "\n" + content)
    # print(article_contents)

    # doc = textacy.Doc(article_contents, lang=en)
    # pre_doc = textacy.preprocess_text(article_contents,lowercase=True,no_punct=True)

    # print(doc)
    # print("")
    # print(pre_doc)
    # print("")
    return data


# get_news(API_KEY)   #Turn this off so you don't do API calls all the time

x = load_data_from_dumpfile()
# print(x)


# do_NLP_magic(x)
