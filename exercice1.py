# Exercice 1 : On demande de réaliser un programme en Python (version 3.7). Celui-ci permettra l’entrée d’un message à crypter et/ou à décrypter (maximum 80 caractères en utilisant 27 possibilités, les 26 caractères majuscules + le blanc).

# Définition des constantes
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

# Fonction de cryptage
def crypter(message, decalage):
    message_crypte = ""
    for lettre in message.upper():  # Transformation en majuscules
        if lettre in ALPHABET:
            index_lettre = ALPHABET.find(lettre)
            index_lettre_crypte = (index_lettre + decalage) % len(ALPHABET)
            lettre_crypte = ALPHABET[index_lettre_crypte]
        else:
            lettre_crypte = lettre
        message_crypte += lettre_crypte
    return message_crypte

# Fonction de décryptage
def decrypter(message, decalage):
    #On inverse le décalage
    return crypter(message, -decalage)

# Affichage du menu
print("1. Crypter un message")
print("2. Décrypter un message")

# Saisie du choix de l'utilisateur
choix = input("Votre choix : ")

decalage = 3  # Décalage par défaut, vous pouvez le changer selon vos besoins

# Traitement du choix de l'utilisateur
if choix == "1":
    # Saisie du message à crypter
    message = input("Message à crypter : ").upper()  # Transformation en majuscules
    # Cryptage du message
    message_crypte = crypter(message, decalage)
    # Affichage du message crypté
    print("Message crypté : " + message_crypte)
elif choix == "2":
    # Saisie du message à décrypter
    message = input("Message à décrypter : ").upper()  # Transformation en majuscules
    # Décryptage du message
    message_decrypte = decrypter(message, decalage)
    # Affichage du message décrypté
    print("Message décrypté : " + message_decrypte)
else:
    print("Choix invalide")
