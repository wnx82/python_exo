# Exercice 4 :  Ecrire un programme en Python (version 3.7) permettant de gérer les calculs sur les polynômes (somme de deux polynômes, produit de deux polynômes, produit d’un polynôme par un coefficient réel). Vous devez pouvoir gérer au moins le 4 ème degré.

import math


# Classe représentant un polynôme
class Polynome:
    # Constructeur
    def __init__(self, coefficients):
        self.coefficients = coefficients

    # Méthode permettant de calculer la valeur du polynôme en x
    def evaluer(self, x):
        result = 0
        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * x**i
        return result

    # Méthode permettant de calculer la somme de deux polynômes
    def additionner(self, autre_polynome):
        coefficients = []
        for i in range(max(len(self.coefficients), len(autre_polynome.coefficients))):
            coefficients.append(self.coefficients[i] + autre_polynome.coefficients[i])
        return Polynome(coefficients)

    # Méthode permettant de calculer le produit de deux polynômes
    def multiplier(self, autre_polynome):
        coefficients = []
        for i in range(len(self.coefficients)):
            for j in range(len(autre_polynome.coefficients)):
                coefficients.append(
                    self.coefficients[i]
                    * autre_polynome.coefficients[j]
                    * (x ** (i + j))
                )
        return Polynome(coefficients)

    # Méthode permettant de demander à l'utilisateur d'introduire les coefficients du polynôme
    def demander_coefficients(self):
        print(
            "Entrez les coefficients du polynôme, un par ligne, en commençant par le coefficient du terme constant :"
        )
        coefficients = []
        for i in range(self.degre + 1):
            coefficients.append(float(input()))
        return coefficients


# Menu
def menu():
    print("Calcul sur les polynômes")
    print("1. Saisir un polynôme")
    print("2. Calculer la somme de deux polynômes")
    print("3. Calculer le produit de deux polynômes")
    print("4. Calculer la valeur d'un polynôme en x")
    print("5. Quitter")
    choix = input("Votre choix : ")
    return choix


# Programme principal
choix = menu()
while choix != "5":
    if choix == "1":
        print("Saisir un polynôme :")
        p1 = Polynome()
        p1.demander_coefficients()
        print("Polynôme saisi :")
        print(p1.coefficients)
    elif choix == "2":
        print("Saisir un deuxième polynôme :")
        p2 = Polynome()
        p2.demander_coefficients()
        print("Polynômes saisis :")
        print(p1.coefficients)
        print(p2.coefficients)
        print("Somme des polynômes :")
        print(p1.additionner(p2).coefficients)
    elif choix == "3":
        print("Saisir un deuxième polynôme :")
        p2 = Polynome()
        p2.demander_coefficients()
        print("Polynômes saisis :")
        print(p1.coefficients)
        print(p2.coefficients)
        print("Produit des polynômes :")
        print(p1.multiplier(p2).coefficients)
    elif choix == "4":
        print("Saisir la valeur de x :")
        x = float(input())
        print("Valeur du polynôme en x :")
        print(p1.evaluer(x))
    else:
        print("Choix invalide")
    choix = menu()
