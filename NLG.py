import sqlite3
import nltk

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

result = con.execute('SELECT title, title_tokens FROM DATA').fetchall()

#print("result", result)

for sentence in result:
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
        continue
    elif ',' in sentence:
        print("whole sentence", sentence)
        split = sentence.split(',')
        split = split[:-1]
        print("len split", len(split))
        if len(split) > 1 and len(split[1]) > 14:
            sentence = str(split[1])
        else:
            sentence = str(split)

    temp_1 = print("Did you hear that " + sentence + "? " + "Do you like that? Why?")

    temp_2 = print(sentence + ". What do you think of this?")

# optie om meer info te geven als de mensen dat willen? Dan bijv de intro printen?

pressed_button = False

if pressed_button == True:
    con = sqlite3.connect('storage.db')
    result = con.execute('SELECT content FROM DATA').fetchall()
    print(result)






