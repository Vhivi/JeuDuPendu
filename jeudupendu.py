#!/usr/bin/python
# -*- coding: utf-8 -*-

# Projet de jeu dupendu

# Un mot est choisi soit par le joueur adverse, soit par le programme. Et le
# joueur dispose de tout l’alphabet pour deviner les lettres.

# Le but pour le joueur est de devenir le mot en choisissant les bonnes
# lettres. Si la lettre est correcte, le mot est complété. Si la lettre
# choisie est incorrecte, vous perdez une vie et le pendu apparaît davantage.

# La partie se termine soit par une victoire si le mot entier est trouvé,
# soit par une défaite sir le bonhomme du pendu apparaît en intégralité
# (vous n’avez plus de vie). Traditionnellement, six erreurs sont autorisées
# avant que le joueur ne perde le jeu, mais ce nombre peut être modifié en
# fonction de la manière dont vous souhaitez créer votre itération du jeu.

from operator import index
import random

# Définition de la liste de mot
# Mot de 5 lettres
# Aucun accent
listeMot = ["Acces",
            "Aimer",
            "Aloes",
            "Assez",
            "Avion",
            "Awale",
            "Balai",
            "Banjo",
            "Barbe",
            "Bonne",
            "Bruit",
            "Buche",
            "Cache",
            "Capot",
            "Carte",
            "Chien",
            "Crane",
            "Cycle",
            "Ebene",
            "Essai",
            "Gifle",
            "Honni",
            "Jambe",
            "Koala",
            "Livre",
            "Lourd",
            "Maman",
            "Moult",
            "Noeud",
            "Ortie",
            "Peche",
            "Poire",
            "Pomme",
            "Poste",
            "Prune",
            "Radar",
            "Radis",
            "Robot",
            "Route",
            "Rugby",
            "Seuil",
            "Taupe",
            "Tenue",
            "Texte",
            "Tyran",
            "Usuel",
            "Valse"]

# Définition du visuel du mot caché
motCache = []
for _ in range(0, 5):
    motCache.append("_")

# Définition de la liste des lettres jouées dans la partie
lettrejouee = []


# On va choisir le mot de façon aléatoire dans la liste
def choixMot():
    indiceMot = random.randint(1, len(listeMot))
    motChoisi = listeMot[indiceMot]
    return motChoisi.upper()


# On affiche le visuel du mot caché
def afficherMot(gagne=None):
    print(motCache[0] + " " + motCache[1] + " " + motCache[2] + " "
          + motCache[3] + " " + motCache[4])

    if gagne:
        print('Bravo ! Vous avez trouvé le mot.')


# On génère la potence pour l'affichage aux échecs.
def afficherPendu(tour):
    pendu = ['___|___',
             '''   |
   |
   |
   |
___|___''',
             '''   -----
   |
   |
   |
   |
___|___''',
             '''   -----
   |/
   |
   |
   |
___|___''',
             '''   -----
   |/  |
   |
   |
   |
___|___''',
             '''   -----
   |/  |
   |   O
   |
   |
___|___''',
             '''   -----
   |/  |
   |   O
   |   |
   |
___|___''',
             '''   -----
   |/  |
   |   O
   |  /|
   |
___|___''',
             '''   -----
   |/  |
   |   O
   |  /|\\
   |
___|___''',
             '''   -----
   |/  |
   |   O
   |  /|\\
   |  /
___|___''',
             '''   -----
   |/  |
   |   O
   |  /|\\
   |  / \\
___|___''']

    print(pendu[tour])


# On va effectuer la révélation
def revelation(lettre, mot):
    indexTour = 0
    # On liste chaque caractère du mot
    motList = list(mot)
    # Pour chaque caractère du mot
    for i in motList:
        # On vérifie si la lettre jouée correspond et que son emplacement
        # est vide
        if i == lettre and motCache[indexTour] == "_":
            motCache[indexTour] = lettre

        indexTour += 1


def main():
    # Définition du tour du pendu
    penduTour = 0

    print('Le mot choisi comprend 5 lettres.')
    # On récupère le mot choisi
    mot = choixMot()

    while True:
        afficherMot()
        # On vérifie si il reste des lettres à découvrir et on affiche les
        # lettres cachées
        if "_" in motCache:
            # On demande une lettre
            lettre = input("Quelle lettre jouez-vous ?").upper()
        else:
            print('Bravo ! Vous avez trouvé toutes les lettres.')
            break

        # On vérifie qu'elle n'a pas déjà été jouée
        if lettre in lettrejouee:
            print('La lettre {} a déjà été jouée, choisissez en une autre.'
                  .format(lettre))
        # Sinon
        else:
            # On ajoute la lettre à une liste pour savoir quelles lettres ont
            # été jouées
            lettrejouee.append(lettre)
            # Si la lettre est dans le mot
            if lettre in mot:
                print('Bingo ! Vous avez trouvé une lettre.')
                # On procède à la révélation
                revelation(lettre, mot)
            # Sinon
            else:
                print('Dommage, réessaie encore !')
                afficherPendu(penduTour)
                penduTour += 1

        if penduTour == 11:
            print('Dommage, vous avez perdu.')
            break

main()
