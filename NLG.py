import sqlite3
import nltk
import json

from nltk.stem.snowball import EnglishStemmer

def transform_to_past(tag):
    ps = EnglishStemmer()
    tag_0, tag_1 = tag
    tag_0 = ps.stem(tag[0])
    print("tag_0", tag_0)
    if tag_0 == 'be' or tag_0 == 'is':
        tag_0 = 'was'
    elif tag_0 == 'begin':
        tag_0 = 'began'
    elif tag_0 == 'break':
        tag_0 = 'broke'
    elif tag_0 == 'bring':
        tag_0 = 'brought'
    elif tag_0 == 'buy':
        tag_0 = 'bought'
    elif tag_0 == 'build':
        tag_0 = 'built'
    elif tag_0 == 'choose':
        tag_0 = 'chose'
    elif tag_0 == 'come':
        tag_0 = 'came'
    elif tag_0 == 'do':
        tag_0 = 'did'
    elif tag_0 == 'draw':
        tag_0 = 'drew'
    elif tag_0 == 'drive':
        tag_0 = 'drove'
    elif tag_0 == 'eat':
        tag_0 = 'ate'
    elif tag_0 == 'feel':
        tag_0 = 'felt'
    elif tag_0 == 'find':
        tag_0 = 'found'
    elif tag_0 == 'get':
        tag_0 = 'got'
    elif tag_0 == 'give':
        tag_0 = 'gave'
    elif tag_0 == 'go':
        tag_0 = 'went'
    elif tag_0 == 'have' or tag_0 == "has":
        tag_0 = 'had'
    elif tag_0 == 'hear':
        tag_0 = 'heard'
    elif tag_0 == 'hold':
        tag_0 = 'held'
    elif tag_0 == 'keep':
        tag_0 = 'kept'
    elif tag_0 == 'know':
        tag_0 = 'knew'
    elif tag_0 == 'leave':
        tag_0 = 'left'
    elif tag_0 == 'lead':
        tag_0 = 'led'
    elif tag_0 == 'lie':
        tag_0 = 'lay'
    elif tag_0 == 'lose':
        tag_0 = 'lost'
    elif tag_0 == 'make':
        tag_0 = 'made'
    elif tag_0 == 'mean':
        tag_0 = 'meant'
    elif tag_0 == 'meet':
        tag_0 = 'met'
    elif tag_0 == 'pay':
        tag_0 = 'paid'
    elif tag_0 == 'run':
        tag_0 = 'ran'
    elif tag_0 == 'say':
        tag_0 = 'said'
    elif tag_0 == 'see':
        tag_0 = 'saw'
    elif tag_0 == 'sell':
        tag_0 = 'sold'
    elif tag_0 == 'send':
        tag_0 = 'sent'
    elif tag_0 == 'sit':
        tag_0 = 'sat'
    elif tag_0 == 'speak':
        tag_0 = 'spoke'
    elif tag_0 == 'spend':
        tag_0 = 'spent'
    elif tag_0 == 'stand':
        tag_0 = 'stood'
    elif tag_0 == 'take':
        tag_0 = 'took'
    elif tag_0 == 'teach':
        tag_0 = 'taught'
    elif tag_0 == 'tell':
        tag_0 = 'told'
    elif tag_0 == 'think':
        tag_0 = 'thought'
    elif tag_0 == 'understand':
        tag_0 = 'understood'
    elif tag_0 == 'wear':
        tag_0 = 'wore'
    elif tag_0 == 'win':
        tag_0 = 'won'
    elif tag_0 == 'write':
        tag_0 = 'wrote'
    else:
        tag_0 = tag_0+'ed'
    tag = tag_0, tag_1
    return tag

con = sqlite3.connect('storage.db')

result = con.execute('SELECT title, category FROM DATA').fetchall()

print("result", result)

sentences_business = []
sentences_entertainment = []
sentences_general = []
sentences_health = []
sentences_science = []
sentences_sports = []
sentences_tech = []


def sentence_generation(sentence):
   # print("sentence", sentence)
    sentence = sentence[0]
    sentence_pos = nltk.word_tokenize(sentence)
  #  print("before pos", sentence_pos)
    sentence_pos = nltk.pos_tag(sentence_pos)
    print("postags", sentence_pos)
    for tag in sentence_pos:
      #  print("tag", tag)
        if tag[1] == 'VBZ':
            tag0, tag1 = tag
            tag_after = transform_to_past(tag)
            print("tag after", tag_after)
            tag0after, tag1after = tag_after
            tag_finished = tag0after, tag1
            if tag0 in sentence:
                sentence = sentence.replace(tag0, tag0after)
        else:
            continue
    sentence = nltk.re.sub(r"\!", ",", sentence)
    #sentence = nltk.re.sub(r"\?", ",", sentence)
    sentence = nltk.re.sub(r"\:", ",", sentence)
    sentence = nltk.re.sub(r"\-", ",", sentence)
    if '?' in sentence:
       sentence = 'pech'
  #  elif ',' in sentence:
    else:
        print("whole sentence", sentence)
        split = sentence.split(',')
        split = split[:-1]
        print("len split", len(split))
        if len(split) > 1 and len(split) < 3 and len(split[1]) > 14:
            sentence = str(split[1])
            if 'said' in split[1] or 'mentioned' in split[1] or 'reports' in split[1] or 'claimed'in split[1] or 'found' in split[1] or 'but' in split[1] or 'say' in split[1]:
                #print("yes!")
                #sentence = str(split[0])
                sentence = 'pech'
        elif len(split) > 2:
            sentence = 'pech'
        else:
            #sentence = str(split)
            sentence = 'pech'
    print("sentence", sentence)
    return sentence


def creating_sentence_lists():
    for sentence in result:
        category = sentence[1]
        print("category", category)
        generated = sentence_generation(sentence)
        if generated is not 'pech':
            if category == 'business':
                generated = "Business is an interesting field. I heard that " + generated + ". Do you like this or not?"
                generated = json.dumps(generated)
                sentences_business.append(generated)
            if category == 'entertainment':
               # generated = sentence_generation(sentence)
                generated = "A lot happens in the entertainment scene. Today I heard that " + generated + ". What do you think of this?"
                generated = json.dumps(generated)
                sentences_entertainment.append(generated)
            if category == 'general':
                #generated = sentence_generation(sentence)
                generated = generated + ". What do you think of this?"
                generated = json.dumps(generated)
                sentences_general.append(generated)
            if category == 'health':
               # generated = sentence_generation(sentence)
                generated = "Staying healthy is important. Someone told me that " + generated + ". Do you like this?"
                generated = json.dumps(generated)
                sentences_health.append(generated)
            if category == 'science':
               # generated = sentence_generation(sentence)
                generated = "We all love science. I heard that " + generated + ". Did you hear about this already?"
                generated = json.dumps(generated)
                sentences_science.append(generated)
            if category == 'sports':
               # generated = sentence_generation(sentence)
                generated = "Did you know about the sport scene that " + generated +"? What do you think of this?"
                generated = json.dumps(generated)
                sentences_sports.append(generated)
            if category == 'technology':
               # generated = sentence_generation(sentence)
                generated = 'Something happened in the technology world, namely ' + generated + ". Do you think this is great or not?"
                generated = json.dumps(generated)
                sentences_tech.append(generated)



    return sentences_business, sentences_entertainment, sentences_general, sentences_health, sentences_science, sentences_sports, sentences_tech

#Deze aanroepen :)
sentences_business, sentences_entertainment, sentences_general, sentences_health, sentences_science, sentences_sports, sentences_tech = creating_sentence_lists()

print("sentences_business", sentences_business)
print("sentences_entertainment", sentences_entertainment)
print("sentences_general", sentences_general)
print("sentences_health", sentences_health)
print("sentences_science", sentences_science)
print("sentences_sports", sentences_sports)
print("sentences_tech", sentences_tech)


    # temp_1 = print("Did you hear that " + sentence + "? " + "Do you like that? Why?")
    #
    # temp_2 = print(sentence + ". What do you think of this?")
    # return template








