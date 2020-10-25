"""Système de vérification"""
def verifie(objet, x, x_souris, y, y_souris) :
    test_x = False
    test_y = False

    x = int(x // 10)
    y = int(y // 10)

    for i in range(0, objet.taille) :
        if x + i == x_souris :
            test_x = True
        if y + i == y_souris :
            test_y = True



    if test_y == True and test_x == True :
        return True

    else :
        return False