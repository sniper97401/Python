from Feature.IdentificationAction import definePseudo
from Feature.ChooseLevelAction import ChooseLevel
from Feature.ProfecyAction import ChooseYourNumber, miseAction
from Feature.ManagePoint import ManagePoint
from random import randrange
from Class.Game import Game
import array
from Feature.AnalyseAction import *

endGame = False
pseudo = definePseudo()
partie = []
compte = 500
level = 1
while (endGame == False or compte <= 0):
    print("Montant disponible: ",compte, "\n")
    print(pseudo, " ,vous débutez une nouvelle partie au level ", level)
    reponse = None
    limite = ChooseLevel(level)
    mise = miseAction(compte)
    compte = compte - mise
    nb = randrange(1, limite)
    print('nb :', nb)
    step = ChooseYourNumber(limite, nb)
    gain = ManagePoint(limite, step, mise)
    compte = compte + gain
    game = Game(level, step, mise, gain)
    partie.append(game)
    print("Vous avez actuellement ", compte, " sur votre compte")
    print("Voulez vous continuer ou arreter?")
    while reponse != "continuer" and reponse != "arreter":
        reponse = input()
    if reponse == "arreter":
        endGame = True
    level = level + 1
if(compte == 0):
    print("Vous êtes trop pauvre , dehors.")
Analyse(partie)
