from Class.Game import Game
def Analyse(partie):
    nbPartie = len(partie)
    print(nbPartie)
    steps = 0
    gain = 0
    for value in partie:
        valueStep = value.step
        valueGain = value.gain
        steps = steps + valueStep
        gain = gain+ valueGain
    moyenStep = steps/nbPartie
    moyenGain = gain/nbPartie
    print("Vous avez fait ",moyenStep," essais en moyenne")
    print("Vous avez fait ",moyenGain," de gain en moyenne")