import numpy as np


def trouver_combinaisons_possibles(ligne, somme_voulue):
    """
    Pour une ligne donnée, trouve toutes les façons possibles de sélectionner des nombres
    pour atteindre la somme voulue.

    For a given row, finds all possible ways to select numbers to reach the desired sum.

    Args:
        ligne: La ligne de nombres à analyser / The row of numbers to analyze.
        somme_voulue: La somme qu'on veut atteindre / The desired sum to reach.
    Returns:
        Liste des combinaisons possibles (1 = nombre sélectionné, 0 = non sélectionné).
        List of possible combinations (1 = number selected, 0 = not selected).
    """
    longueur = len(ligne)  # Longueur de la ligne / Length of the row.
    combinaisons_valides = []

    # On teste toutes les possibilités de 0 à 2^longueur-1
    # Test all possibilities from 0 to 2^length - 1.
    for i in range(2 ** longueur):
        # Convertir le nombre en binaire (liste de 0 et 1)
        # Convert the number to binary (list of 0 and 1).
        selection = [int(digit) for digit in bin(i)[2:].zfill(longueur)]

        # Calculer la somme des nombres sélectionnés
        # Calculate the sum of the selected numbers.
        somme = sum(nombre * choix for nombre, choix in zip(ligne, selection))

        # Si on trouve la somme voulue, on garde cette combinaison
        # If the desired sum is found, keep this combination.
        if somme == somme_voulue:
            combinaisons_valides.append(selection)

    return combinaisons_valides


def verifier_solution(matrice, solution, sommes_lignes, sommes_colonnes):
    """
    Vérifie si la solution actuelle respecte toutes les contraintes.

    Checks if the current solution satisfies all the constraints.

    Args:
        matrice: La matrice d'origine / The original matrix.
        solution: La matrice de 0 et 1 indiquant les sélections / The 0 and 1 matrix indicating selections.
        sommes_lignes: Les sommes cibles pour les lignes / Target sums for rows.
        sommes_colonnes: Les sommes cibles pour les colonnes / Target sums for columns.
    Returns:
        True si la solution est valide, False sinon / True if the solution is valid, False otherwise.
    """
    # Vérifier les sommes des lignes / Check row sums.
    for i, ligne in enumerate(solution):
        # Calculer la somme pour cette ligne
        # Calculate the sum for this row.
        somme = sum(nombre * choix for nombre, choix in zip(matrice[i], ligne))

        # Si la somme ne correspond pas, retourner False
        # If the sum does not match, return False.
        if somme != sommes_lignes[i]:
            return False

    # Vérifier les sommes des colonnes / Check column sums.
    for j in range(len(solution[0])):
        # Calculer la somme pour cette colonne
        # Calculate the sum for this column.
        somme = sum(matrice[i][j] * solution[i][j] for i in range(len(solution)))

        # Si la somme ne correspond pas, retourner False
        # If the sum does not match, return False.
        if somme != sommes_colonnes[j]:
            return False

    # Si tout est valide, retourner True / If everything is valid, return True.
    return True


def resoudre_puzzle(matrice, sommes_lignes, sommes_colonnes):
    """
    Fonction principale qui résout le puzzle.

    Main function to solve the puzzle.

    Args:
        matrice: La matrice d'origine / The original matrix.
        sommes_lignes: Les sommes cibles pour les lignes / Target sums for rows.
        sommes_colonnes: Les sommes cibles pour les colonnes / Target sums for columns.
    Returns:
        La matrice solution si une solution est trouvée, None sinon.
        The solution matrix if a solution is found, None otherwise.
    """
    nb_lignes = len(matrice)  # Nombre de lignes / Number of rows.
    solution = np.zeros_like(matrice)  # Créer une matrice remplie de 0 / Create a matrix filled with 0s.

    def essayer_ligne(ligne_actuelle):
        # Si toutes les lignes ont été traitées, vérifier la solution
        # If all rows have been processed, check the solution.
        if ligne_actuelle == nb_lignes:
            return verifier_solution(matrice, solution, sommes_lignes, sommes_colonnes)

        # Trouver toutes les combinaisons possibles pour la ligne actuelle
        # Find all possible combinations for the current row.
        combinaisons = trouver_combinaisons_possibles(
            matrice[ligne_actuelle],
            sommes_lignes[ligne_actuelle]
        )

        # Essayer chaque combinaison possible / Try each possible combination.
        for combo in combinaisons:
            # Sauvegarder l'état actuel de la ligne / Save the current row state.
            ancien_etat = solution[ligne_actuelle].copy()

            # Appliquer la nouvelle combinaison / Apply the new combination.
            solution[ligne_actuelle] = combo

            # Passer à la ligne suivante / Move to the next row.
            if essayer_ligne(ligne_actuelle + 1):
                return True

            # Si ça ne marche pas, revenir en arrière / If it doesn't work, backtrack.
            solution[ligne_actuelle] = ancien_etat

        return False

    # Commencer la résolution depuis la première ligne / Start solving from the first row.
    if essayer_ligne(0):
        return solution
    return None


# Test du programme / Program test.
matrice_test = [
    [1, 5, 3, 4, 1, 4],
    [1, 9, 8, 9, 1, 3],
    [7, 7, 5, 9, 1, 4],
    [8, 6, 2, 7, 5, 7],
    [6, 3, 9, 3, 4, 3],
    [7, 5, 5, 5, 3, 6]
]

sommes_l = [2, 13, 14, 13, 19, 17]  # Sommes des lignes / Row sums.
sommes_c = [17, 8, 14, 18, 11, 10]  # Sommes des colonnes / Column sums.

solution = resoudre_puzzle(matrice_test, sommes_l, sommes_c)

if solution is not None:
    print("Solution trouvée:")  # Solution found.
    for ligne in solution:
        print([int(x) for x in
               ligne])  # Convertit les nombres en entiers pour l'affichage / Converts numbers to integers for display.
else:
    print("Pas de solution trouvée")  # No solution found.
