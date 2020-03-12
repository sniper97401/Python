def ManagePoint(limite,step,mise):
    if step == 1:
        recompense = mise * 2
        print("Vous avez remporter ", recompense, " euros ")
        return recompense
    if step == 2:
        recompense = mise * 0.5
        print("Vous avez remporter ", recompense," euros ")
        return recompense
    if step > 2:
        recompense = mise * 0
        print("Vous avez perdu ", mise," euros ")
        return 0
