# Addition de deux matrices
# Multiplication de deux matrices
# Multiplication d’une matrice par un scalaire
# Transposition d’une matrice
# Voici le programme :


def saisie_matrice(rows, cols):
    matrice = []
    for i in range(rows):
        row = list(
            map(
                float,
                input(f"Entrez la ligne {i+1} (séparée par des espaces) : ").split(),
            )
        )
        assert len(row) == cols, f"La ligne doit avoir {cols} éléments."
        matrice.append(row)
    return matrice


def addition_matrices(mat1, mat2):
    return [
        [mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))
    ]


def multiplication_matrices(mat1, mat2):
    result = [[0 for j in range(len(mat2[0]))] for i in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


def multiplication_scalaire(mat, scalar):
    return [[scalar * mat[i][j] for j in range(len(mat[0]))] for i in range(len(mat))]


def transposition(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]


def afficher_matrice(mat):
    for row in mat:
        print(" | ".join(map(str, row)))


def main():
    print("Opérations sur des matrices :")
    print("1. Addition de deux matrices")
    print("2. Multiplication de deux matrices")
    print("3. Multiplication d’une matrice par un scalaire")
    print("4. Transposition d’une matrice")

    choix = int(input("\nEntrez votre choix : "))

    if choix == 1:
        print("\nAddition de deux matrices :")
        rows = int(input("Entrez le nombre de lignes des matrices : "))
        cols = int(input("Entrez le nombre de colonnes des matrices : "))
        print("\nSaisie de la première matrice :")
        mat1 = saisie_matrice(rows, cols)
        print("\nSaisie de la deuxième matrice :")
        mat2 = saisie_matrice(rows, cols)
        result = addition_matrices(mat1, mat2)
        print("\nRésultat de l'addition :")
        afficher_matrice(result)

    elif choix == 2:
        print("\nMultiplication de deux matrices :")
        rows1 = int(input("Entrez le nombre de lignes de la première matrice : "))
        cols1 = int(input("Entrez le nombre de colonnes de la première matrice : "))
        rows2 = cols1
        cols2 = int(input("Entrez le nombre de colonnes de la deuxième matrice : "))
        print("\nSaisie de la première matrice :")
        mat1 = saisie_matrice(rows1, cols1)
        print("\nSaisie de la deuxième matrice :")
        mat2 = saisie_matrice(rows2, cols2)
        result = multiplication_matrices(mat1, mat2)
        print("\nRésultat de la multiplication :")
        afficher_matrice(result)

    elif choix == 3:
        print("\nMultiplication d’une matrice par un scalaire :")
        rows = int(input("Entrez le nombre de lignes de la matrice : "))
        cols = int(input("Entrez le nombre de colonnes de la matrice : "))
        mat = saisie_matrice(rows, cols)
        scalar = float(input("\nEntrez le scalaire : "))
        result = multiplication_scalaire(mat, scalar)
        print("\nRésultat de la multiplication :")
        afficher_matrice(result)

    elif choix == 4:
        print("\nTransposition d’une matrice :")
        rows = int(input("Entrez le nombre de lignes de la matrice : "))
        cols = int(input("Entrez le nombre de colonnes de la matrice : "))
        mat = saisie_matrice(rows, cols)
        result = transposition(mat)
        print("\nRésultat de la transposition :")
        afficher_matrice(result)

    else:
        print("Choix non valide.")


if __name__ == "__main__":
    main()
