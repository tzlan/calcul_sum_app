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
    longueur = len(ligne)
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


def verifier_solution(matrice, solution, sommes_lignes, sommes_colonnes):
    """
    Vérifie si la solution actuelle respecte toutes les contraintes
    """
    # Vérifier les sommes des lignes
    for i, ligne in enumerate(solution):
        somme = sum(nombre * choix for nombre, choix in zip(matrice[i], ligne))
        if somme != sommes_lignes[i]:
            return False

    # Vérifier les sommes des colonnes
    for j in range(len(solution[0])):
        somme = sum(matrice[i][j] * solution[i][j] for i in range(len(solution)))
        if somme != sommes_colonnes[j]:
            return False

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
