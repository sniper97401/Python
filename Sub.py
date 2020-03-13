from Feature.IdentificationAction import definePseudo
from Feature.ChooseLevelAction import ChooseLevel
from Feature.ProfecyAction import ChooseYourNumber, miseAction
from Feature.ManagePoint import ManagePoint
from Feature.ImportAction import *
from random import randrange
from Class.Game import Game
from Class.Partie import Partie
import array
from Feature.AnalyseAction import *

partie = Partie()
partie = importResult(partie)
endGame = False
pseudo = definePseudo()
level = partie.level
compte = partie.compte
reponse = None

if compte != 500 and level != 1 :
    print("Voulez vous écraser votre précédente partie? oui ou non")
    while reponse != "oui" and reponse != "non":
        reponse = input().lower()
    if reponse == "oui":
        compte = 500
        level = 1

while endGame == False and compte > 0 :
    print("Montant disponible: ", compte, "\n")
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
    game = Game(pseudo, level, step, gain, mise)
    partie.games.append(game)
    partie.compte = compte
    print("Vous avez actuellement ", compte, " sur votre compte")
    print("Voulez vous continuer ou arreter?")
    while compte != 0 and reponse != "continuer" and reponse != "arreter":
        reponse = input().lower()
    if reponse == "arreter":
        endGame = True
    partie.level = level + 1
    level = partie.level
    ExportResult(partie)
    print(compte)
    print(partie.compte)
if compte == 0:
    print("Vous êtes trop pauvre , dehors.")
Analyse(partie.games)
