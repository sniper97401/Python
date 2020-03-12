def definePseudo():
    print('Veuillez entrer votre pseudo')
    pseudo = input()
    while (len(pseudo) < 2):
        print('Votre pseudo n\'est pas conforme')
        pseudo = input()
    return pseudo