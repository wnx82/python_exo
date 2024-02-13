# Exercice 2 : Veuillez concevoir un programme en Python (version 3.7) qui permettra de réaliser le cycle complet d’encryptage / décryptage d’un message et produira des résultats détaillés (Méthode RSA) .

import random

def gcd(a, b):
    """Calcul du plus grand commun diviseur."""
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    """Calcul de l'inverse modulaire."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    """Générer une paire de clés RSA."""
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = modinv(e, phi)
    return ((e, n), (d, n))

def encrypt(message, public_key):
    """Chiffrer un message avec la clé publique."""
    key, n = public_key
    encrypted_message = []
    for char in message:
        encrypted_char = pow(ord(char), key, n)
        encrypted_message.append(encrypted_char)
    return encrypted_message

def decrypt(encrypted, private_key):
    """Déchiffrer un message avec la clé privée."""
    key, n = private_key
    decrypted_message = ""
    for char in encrypted:
        decrypted_char = chr(pow(char, key, n))
        decrypted_message += decrypted_char
    return decrypted_message

def main():
    # Choix des nombres premiers p et q (petits pour la démonstration)
    p = 61
    q = 53
    
    # Génération de la paire de clés RSA
    public_key, private_key = generate_keypair(p, q)
    print("Clé publique:", public_key)
    print("Clé privée:", private_key)

    # Demander à l'utilisateur s'il souhaite crypter ou décrypter
    mode = input("Souhaitez-vous crypter ou décrypter le message? (c/d): ")

    if mode.lower() == "c":
        # Message à chiffrer
        message = input("Entrez le message à crypter: ")

        # Chiffrement du message
        encrypted_message = encrypt(message, public_key)

        # Affichage du message chiffré sous forme de chaîne de caractères
        print("Message crypté:", ''.join(map(str, encrypted_message)))
        
    elif mode.lower() == "d":
        # Message à déchiffrer
        message = input("Entrez le message à décrypter (sous forme de liste d'entiers): ")
        # Conversion de la chaîne de caractères en liste d'entiers
        encrypted_message = [int(x) for x in message]

        # Déchiffrement du message
        decrypted_message = decrypt(encrypted_message, private_key)
        print("Message décrypté:", decrypted_message)
    else:
        print("Choix invalide. Veuillez entrer 'c' pour crypter ou 'd' pour décrypter.")

if __name__ == "__main__":
    main()
