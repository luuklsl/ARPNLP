from newsapi import NewsApiClient
from pprint import pprint
import json

from API import API_KEY

#Init
newsapi = NewsApiClient(api_key=API_KEY)


# sources = newsapi.get_sources(language='en', category='general')
#
# print(sources)

# get_everything requires either a query, sources and domain
# articles = newsapi.get_everything(sources='reuters')
# #
# print(articles)


top_articles =newsapi.get_top_headlines(country='ca')

print(top_articles)

with open('dumpfile.json', 'w') as file:
    json.dump(top_articles, file, indent=4)
    print('dumped')

# dictdump = json.dumps(top_articles)
#
# with open('dumpfile.txt') as file:
#     file.write(top_articles)
#
# print(dictdump)

print('end')