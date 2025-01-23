import numpy as np


def resoudre_sumnumber(matrice, sommes_lignes, sommes_col):
    # Création matrice de choix (0/1) de même taille
    n, m = matrice.shape
    choix = np.zeros((n, m))

    # Parcours de la matrice
    for i in range(n):
        for j in range(m):
            # Calcul sommes actuelles
            somme_ligne = np.sum(matrice[i, :] * choix[i, :])
            somme_col = np.sum(matrice[:, j] * choix[:, j])

            # Test si ce nombre aide pour les sommes
            if (somme_ligne + matrice[i, j] <= sommes_lignes[i] and
                    somme_col + matrice[i, j] <= sommes_col[j]):
                choix[i, j] = 1

    # Vérification finale        
    sommes_l = np.sum(matrice * choix, axis=1)
    sommes_c = np.sum(matrice * choix, axis=0)

    if np.array_equal(sommes_l, sommes_lignes) and np.array_equal(sommes_c, sommes_col):
        return choix
    else:
        return "Pas de solution"


# Test
matrice = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
sommes_lignes = np.array([5, 11, 15])
sommes_col = np.array([8, 13, 10])

solution = resoudre_sumnumber(matrice, sommes_lignes, sommes_col)
print(solution)
