import numpy as np


def trouver_combinaisons_possibles(ligne, somme_voulue):
    """
    Pour une ligne donnée, trouve toutes les façons possibles de sélectionner des nombres
    pour atteindre la somme voulue

    Args:
        ligne: La ligne de nombres à analyser
        somme_voulue: La somme qu'on veut atteindre
    Returns:
        Liste des combinaisons possibles (1 = nombre sélectionné, 0 = non sélectionné)
    """
    longueur = len(ligne) #Lengh tha have receive in params
    combinaisons_valides = []

    # On teste toutes les possibilités de 0 à 2^longueur-1
    # Par exemple pour une ligne de 3 nombres: 000, 001, 010, 011, 100, 101, 110, 111
    for i in range(2 ** longueur):
        # Convertir le nombre en binaire (liste de 0 et 1)
        selection = [int(digit) for digit in bin(i)[2:].zfill(longueur)]

        # Calculer la somme des nombres sélectionnés
        somme = sum(nombre * choix for nombre, choix in zip(ligne, selection))

        # Si on trouve la somme voulue, on garde cette combinaison
        if somme == somme_voulue:
            combinaisons_valides.append(selection)



    return combinaisons_valides
#Elle regarde chaque ligne de la solution
#Multiplie chaque nombre par sa sélection (0 ou 1)
#Calcule la somme totale
#Vérifie si cette somme correspond exactement à la somme attendue


def verifier_solution(matrice, solution, sommes_lignes, sommes_colonnes):
    # matrice c'est mon tab origianal
    #solution ici c'est 0 ou 1 d'en haut et

    """
    Vérifie si la solution actuelle respecte toutes les contraintes
    """
    # vérifier les sommes des lignes  Parcourir chaque ligne de la solution

    for i, ligne in enumerate(solution):
        # calculer la somme pour cette ligne
        # (on multiplie les valeurs de la matrice par les choix dans la solution)
        somme = sum(nombre * choix for nombre, choix in zip(matrice[i], ligne))

        # vérifier si la somme de la ligne correspond à la somme attendue
        if somme != sommes_lignes[i]:
            return False  # Si ce n'est pas le cas, la solution est invalide

    # parcourir chaque colonne de la solution
    for j in range(len(solution[0])):
        # Calculer la somme pour cette colonne
        # (on fait la somme des produits des valeurs de la matrice et des choix de la solution)
        somme = sum(matrice[i][j] * solution[i][j] for i in range(len(solution)))

        # vérifier si la somme de la colonne correspond à la somme attendue
        if somme != sommes_colonnes[j]:
            return False  # Si ce n'est pas le cas, la solution est invalide

    # si toutes les lignes et colonnes sont valides, la solution est correcte

    return True


def resoudre_puzzle(matrice, sommes_lignes, sommes_colonnes):
    """
    Fonction principale qui résout le puzzle
    """
    nb_lignes = len(matrice)
    solution = np.zeros_like(matrice)  # Crée une matrice de même taille remplie de 0

    def essayer_ligne(ligne_actuelle):
        # Si on a traité toutes les lignes, on vérifie la solution
        if ligne_actuelle == nb_lignes:
            return verifier_solution(matrice, solution, sommes_lignes, sommes_colonnes)

        # Chercher toutes les combinaisons possibles pour la ligne actuelle
        combinaisons = trouver_combinaisons_possibles(
            matrice[ligne_actuelle],
            sommes_lignes[ligne_actuelle]
        )

        # Essayer chaque combinaison possible
        for combo in combinaisons:
            # Sauvegarder l'ancienne ligne
            ancien_etat = solution[ligne_actuelle].copy()
            # Essayer la nouvelle combinaison
            solution[ligne_actuelle] = combo

            # Passer à la ligne suivante
            if essayer_ligne(ligne_actuelle + 1):
                return True

            # Si ça ne marche pas, on revient en arrière
            solution[ligne_actuelle] = ancien_etat

        return False

    # Commencer la résolution à partir de la première ligne
    if essayer_ligne(0):
        return solution
    return None


# Test du programme
matrice_test = [
    [1, 5, 3, 4, 1, 4],
    [1, 9, 8, 9, 1, 3],
    [7, 7, 5, 9, 1, 4],
    [8, 6, 2, 7, 5, 7],
    [6, 3, 9, 3, 4, 3],
    [7, 5, 5, 5, 3, 6]
]

sommes_l = [2, 13, 14, 13, 19, 17]
sommes_c = [17, 8, 14, 18, 11, 10]

solution = resoudre_puzzle(matrice_test, sommes_l, sommes_c)

if solution is not None:
    print("Solution trouvée:")
    for ligne in solution:
        print([int(x) for x in ligne])  # Convertit les nombres en entiers pour l'affichage
else:
    print("Pas de solution trouvée")
