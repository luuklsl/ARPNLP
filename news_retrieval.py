from newsapi import NewsApiClient
from pprint import pprint
import json
import spacy

from API import API_KEY


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

    top_articles = newsapi.get_top_headlines(country='ca')


    with open('dumpfile.json', 'w') as file:
        json.dump(top_articles, file, indent=4)
        print('dumped')


def do_NLP_magic():
    """"Function to call spaCy NLP magic. Reads from file so we aren't forced to
    do API calls all the time if we don't want to"""

    # Read the file we just created, as we are in early stages i recommend keeping this here
    with open('dumpfile.json') as file:
        x = json.loads(file.read())
        # print(x)

    # horrible code, but it makes clear what it does, if not, use prints ;)
    article = dict((x['articles'][2]))
    title = (article['title'])
    description = (article['description'])
    content = (article['content'])
    article_contents = (title + "\n" + description + "\n" + content)
    print(article_contents)

    # Literally the example on the spaCy website, seems to work okay enough for now
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(article_contents)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)


get_news(API_KEY)   #Turn this off so you don't do API calls all the time
do_NLP_magic()
