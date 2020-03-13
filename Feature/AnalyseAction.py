from Class.Game import Game
import matplotlib.pyplot as plt
from tkinter import *


def Analyse(partie):
    nbPartie = len(partie)
    steps = 0
    gain = 0
    bestgain = 0
    worsegain = None
    bigmise = 0
    cpt = 1
    allGain = []
    allMise = []
    allPartie = []
    allStep = []
    for value in partie:
        valueStep = value.step
        valueGain = value.gain
        valueMise = value.mise
        allGain.append(valueGain)
        allMise.append(valueMise)
        allStep.append(valueStep)
        cpt=cpt+1
        allPartie.append(cpt)
        if valueGain > bestgain:
            bestgain = valueGain
        if worsegain == None or valueGain < worsegain:
            worsegain = valueGain
        if valueMise > bigmise:
            bigmise = valueMise
        steps = steps + valueStep
        gain = gain + valueGain
    moyenStep = steps / nbPartie
    moyenGain = gain / nbPartie

    print("Vous avez effectuer ", nbPartie, "partie")
    print("Vous avez fait ", moyenStep, " essais en moyenne")
    print("Vous avez fait ", moyenGain, " de gain en moyenne")
    print("Votre meilleur gain est de  ", bestgain, " euros")
    print("Votre pire gain est de  ", worsegain, " euros")
    print("Votre plus grosse mise est de   ", bigmise, " euros")
    plt.plot(allPartie, allGain)
    plt.title("Gain par partie")
    plt.show()
    plt.close()
    plt.title("Mise par partie")
    plt.plot(allPartie, allMise)
    plt.show()
    plt.title("Essai par partie")
    plt.plot(allPartie, allStep)
    plt.show()
