def resoudre_systeme(a, b, c, d, e, f):
    determinant = a * d - b * c

    if determinant == 0:
        return None, None  # Pas de solution unique

    x = (e * d - b * f) / determinant
    y = (a * f - e * c) / determinant

    return x, y


def main():
    print("Pour le système d'équations suivant :")
    print("ax + by = e")
    print("cx + dy = f")

    a = float(input("Entrez la valeur de a : "))
    b = float(input("Entrez la valeur de b : "))
    c = float(input("Entrez la valeur de c : "))
    d = float(input("Entrez la valeur de d : "))
    e = float(input("Entrez la valeur de e : "))
    f = float(input("Entrez la valeur de f : "))

    x, y = resoudre_systeme(a, b, c, d, e, f)

    if x is not None and y is not None:
        print(f"\nLa solution du système est : x = {x}, y = {y}")
    else:
        print("\nLe système n'a pas de solution unique.")


if __name__ == "__main__":
    main()
