def ChooseYourNumber(limite, nb):
    step = 0
    print("J'ai choisi un nombre entre 0 et ", limite, " essayez de le deviner: ")
    reponse = -1

    while reponse != nb and step < 5 and reponse <= 0:
        try:
            step = step + 1
            reponse = int(input())

        except ValueError:
            step = step + 1
            reponse = None

        if reponse < 1 or reponse > limite:
            print("Votre réponse n'est pas comprise entre 0 et ", limite)
        elif reponse != nb:
            print("Essai numéro ", step, " .Votre réponse est incorrecte")
            if reponse < nb:
                print("Votre réponse est trop basse")
            if reponse > nb:
                print("Votre réponse est trop haute")
    if reponse == nb:
        print("Félicitation vous avez deviné")
    else:
        print("Echec vous avez perdu")
    return step


def miseAction(compte):
    mise = None
    while not mise or mise > compte or mise < 1:
        print('Veuillez choisir combien vous voulez miser entre 1 et ', compte, ' euros')
        try:
            mise = int(input())
        except ValueError:
            print('Mise incorrect')
    return mise
