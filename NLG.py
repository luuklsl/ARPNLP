import sqlite3
import nltk

con = sqlite3.connect('storage.db')

result = con.execute('SELECT title FROM DATA').fetchall()

#print("result", result)

for sentence in result:
   # print("sentence", sentence)
    sentence = sentence[0]
    sentence = nltk.re.sub(r"\!", ",", sentence)
    sentence = nltk.re.sub(r"\?", ",", sentence)
    sentence = nltk.re.sub(r"\:", ",", sentence)
    sentence = nltk.re.sub(r"\-", ",", sentence)
    if ',' in sentence:
        split = sentence.split(',')
        split = split[:-1]
        print("len split", len(split))
        if len(split) > 1:
            sentence = str(split[1])
        else:
            sentence = str(split)

    temp_1 = print("Did you hear that " + sentence + "? " + "Do you like that? Why?")

    temp_2 = print(sentence + ". What do you think of this?")





# transform to past tense (as it already happened)


