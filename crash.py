import dbm.ndbm
from select import select

import numpy as np


def trouver_combinaisons_possibles(ligne, somme_voulue):
    """
        Liste des combinaisons possibles (1 = nombre que je prends, 0 = non)
    """
    longueur = len(ligne)
    combinaisons_valides = []

    # On teste toutes les possibilités (etape 2 voir mon pseudo code)

    for i in range(2 ** longueur):
        # Convertir le nombre en binaire (liste de 0 et 1)
        selection = [int(digit) for digit in bin(i)[2:].zfill(longueur)]

        # Calculer la somme des nombres sélectionnés
        somme = sum(nombre * choix for nombre, choix in zip(ligne, selection))

        # Si on trouve la somme voulue, on garde cette combinaison
        if somme == somme_voulue:
            combinaisons_valides.append(selection)
            if somme > somme_voulue:
              combinaisons_valides.append(selection);
            dbm.ndbm.open("");
























def trouver_combinaisons_possibles(ligne=[1, 5, 3], somme_voulue=6):
    # 1. On détermine la longueur de la ligne
    longueur = len(ligne)  # ici longueur = 3
    combinaisons_valides = []  # Liste qui va stocker nos solutions

    # 2. range(2**longueur) va générer les nombres de 0 à 7 (2³-1)
    # car 2**3 = 8 possibilités pour une ligne de 3 nombres
    for i in range(2**longueur):
        # i prendra successivement les valeurs: 0,1,2,3,4,5,6,7

        # 3. Conversion en binaire:
        # bin(i) convertit i en binaire avec format '0b101'
        # [2:] enlève le '0b' du début
        # zfill(longueur) ajoute des zéros devant pour avoir la bonne longueur
        # Pour i = 5:
        # bin(5) -> '0b101'
        # [2:] -> '101'
        # zfill(3) -> '101'
        # [int(digit) for digit] -> [1, 0, 1]
        selection = [int(digit) for digit in bin(i)[2:].zfill(longueur)]

        # 4. Calculer la somme:
        # zip(ligne, selection) combine les deux listes:
        # ligne=[1,5,3], selection=[1,0,1] -> [(1,1), (5,0), (3,1)]
        # nombre * choix : multiplie chaque nombre par 0 ou 1
        # sum() additionne tous les résultats
        somme = sum(nombre * choix for nombre, choix in zip(ligne, selection))

        # 5. Si la somme correspond, on garde cette combinaison
        if somme == somme_voulue:
            combinaisons_valides.append(selection)

    return combinaisons_valides




