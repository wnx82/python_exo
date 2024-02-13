#  Exercice 3 : Réaliser un programme en Python (version 3.7) permettant la résolution du modèle d’équation du second degré AX² + BX + C = 0. On prendra en compte toutes les possibilités (delta >0, =0, <0).

import math


# Fonction de résolution de l'équation du second degré
def resoudre(a, b, c):
    # Calcul du discriminant
    delta = b**2 - 4 * a * c

    # Cas où l'équation a deux solutions
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)

    # Cas où l'équation a une solution
    elif delta == 0:
        x = -b / (2 * a)
        return (x,)

    # Cas où l'équation n'a pas de solution
    else:
        return None


# Menu
def menu():
    print("Résolution d'équation du second degré")
    print("1. Résoudre une équation")
    print("2. Quitter")
    choix = input("Votre choix : ")
    return choix


# Programme principal
choix = menu()
while choix != "2":
    if choix == "1":
        print("Saisir les coefficients de l'équation :")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))

        # Résolution de l'équation
        solutions = resoudre(a, b, c)

        # Affichage des solutions
        if solutions is not None:
            print("Les solutions de l'équation sont :")
            for x in solutions:
                print("x = %.2f" % x)
        else:
            print("L'équation n'a pas de solution")
    choix = menu()
