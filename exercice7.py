def determinant3x3(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def resoudre_systeme(coefficients, constants):
    D = determinant3x3(coefficients)

    if D == 0:
        return None, None, None  # Pas de solution unique

    coefficients_x = [list(row) for row in coefficients]
    for i in range(3):
        coefficients_x[i][0] = constants[i]

    coefficients_y = [list(row) for row in coefficients]
    for i in range(3):
        coefficients_y[i][1] = constants[i]

    coefficients_z = [list(row) for row in coefficients]
    for i in range(3):
        coefficients_z[i][2] = constants[i]

    D_x = determinant3x3(coefficients_x)
    D_y = determinant3x3(coefficients_y)
    D_z = determinant3x3(coefficients_z)

    x = D_x / D
    y = D_y / D
    z = D_z / D

    return x, y, z


def main():
    print("Pour le système d'équations suivant :")
    print("ax + by + cz = j")
    print("dx + ey + fz = k")
    print("gx + hy + iz = l")

    coefficients = []
    for i in ["première", "deuxième", "troisième"]:
        row = list(
            map(
                float,
                input(
                    f"Entrez les coefficients (a, b, c) pour la {i} équation, séparés par des espaces : "
                ).split(),
            )
        )
        coefficients.append(row)

    constants = list(
        map(
            float,
            input(
                "Entrez les constantes (j, k, l) pour les équations, séparés par des espaces : "
            ).split(),
        )
    )

    x, y, z = resoudre_systeme(coefficients, constants)

    if x is not None and y is not None and z is not None:
        print(f"\nLa solution du système est : x = {x}, y = {y}, z = {z}")
    else:
        print("\nLe système n'a pas de solution unique.")


if __name__ == "__main__":
    main()
