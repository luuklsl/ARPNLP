import json

qtable = {'bsentences.json' : 0,'esentences.json' : 0,'gsentences.json' : 0,'hsentences.json' : 0,'scsentences.json' : 0,'spsentences.json' : 0,'tsentences.json' : 0}


with open('q.json','w') as outfile:
    json.dump(qtable, outfile)
