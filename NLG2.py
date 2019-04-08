import sqlite3
import re

import spacy
from spacy import displacy

con = sqlite3.connect('storage.db')

results = con.execute('SELECT title, title_entities, title_dependencies, category FROM DATA').fetchmany(20)
con.close()

x= 0
for result in results:
    x+=1
    title = result[0]
    entities = result[1]
    dependencies = result[2]
    category = result[3]

    if x == 18:
        print(title)
        print(entities)
        print(dependencies)
        print(category)

        title = re.sub(r'( - [a-zA-Z ]+$)', '', title)

        nlp = spacy.load('en_core_web_sm')
        doc = nlp(title)

        displacy.serve(doc, style='dep')

