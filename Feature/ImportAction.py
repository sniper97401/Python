import json
from collections import namedtuple
from Class.Game import Game
from Class.Partie import Partie
from json import JSONEncoder

def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())

def importResult(partie):
    try:
        with open('data.json') as json_file:
            data = json.load(json_file)
            partie.compte = (data[0]['compte'])
            data.remove(data[0])
            partie.level = (data[0]['level'])
            data.remove(data[0])
            for d in data:

                game = Game(d['pseudo'], d['level'], d['step'], d['gain'], d['mise'])
                partie.games.append(game)
    except:
        partie = Partie()
        partie.level = 1
        partie.compte = 500
    return partie


def ExportResult(parties):
    data =[]
    data.append({'compte': parties.compte})
    data.append({'level': parties.level})
    for partie in parties.games:
        data.append({
            'pseudo': partie.pseudo,
            'mise': partie.mise,
            'gain': partie.gain,
            'level': partie.level,
            'step': partie.step
        })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)