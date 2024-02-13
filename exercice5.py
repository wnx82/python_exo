# Exercice 5 : Ecrire un programme en Python (version 3.7) qui permet d’analyser les attributions dans un diagramme de Venn composé de trois ensembles (voir exercice type fait au cours)
# Pour analyser un diagramme de Venn composé de trois ensembles, nous pouvons utiliser des ensembles (set en Python) pour gérer nos opérations. Nous aurons besoin de sept entrées : une pour chaque sous-ensemble possible du diagramme de Venn.

# Pour simplifier, nous allons nommer ces ensembles :

# A : éléments uniquement dans l'ensemble A
# B : éléments uniquement dans l'ensemble B
# C : éléments uniquement dans l'ensemble C
# AB : éléments à l'intersection de A et B mais pas dans C
# AC : éléments à l'intersection de A et C mais pas dans B
# BC : éléments à l'intersection de B et C mais pas dans A
# ABC : éléments à l'intersection de A, B et C

# pip install matplotlib

# Importation de la bibliothèque matplotlib
import matplotlib.pyplot as plt
from matplotlib_venn import venn3


# Ensembles
ensemble1 = set()
ensemble2 = set()
ensemble3 = set()

# Effectifs
effectif1 = 0
effectif2 = 0
effectif3 = 0
effectif_inter12 = 0
effectif_inter13 = 0
effectif_inter23 = 0
effectif_inter123 = 0


# Menu
def menu():
    print(
        "Analyse des attributions dans un diagramme de Venn composé de trois ensembles"
    )
    print("1. Entrer les données")
    print("2. Tracer le diagramme de Venn")
    print("3. Quitter")
    choix = input("Votre choix : ")
    return choix


# Choix de l'utilisateur
choix = menu()

while choix != "3":
    if choix == "1":
        # Saisie des données
        ensemble1 = set(input("Saisir les éléments de l'ensemble 1 : ").split())
        ensemble2 = set(input("Saisir les éléments de l'ensemble 2 : ").split())
        ensemble3 = set(input("Saisir les éléments de l'ensemble 3 : ").split())

        # Calcul des effectifs
        effectif1 = len(ensemble1)
        effectif2 = len(ensemble2)
        effectif3 = len(ensemble3)
        effectif_inter12 = len(ensemble1.intersection(ensemble2))
        effectif_inter13 = len(ensemble1.intersection(ensemble3))
        effectif_inter23 = len(ensemble2.intersection(ensemble3))
        effectif_inter123 = len(
            ensemble1.intersection(ensemble2).intersection(ensemble3)
        )

    elif choix == "2":
        # Création du diagramme de Venn
        venn3(
            [
                effectif1,
                effectif2,
                effectif3,
                effectif_inter12,
                effectif_inter13,
                effectif_inter23,
                effectif_inter123,
            ],
            ("Group1", "Group2", "Group3"),
        )
        plt.show()

    choix = menu()

print("Au revoir !")
