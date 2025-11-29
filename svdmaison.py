import numpy as np

def calcul_U_V(A, k):
    taille = max(np.shape(A)) # taille maximale de la matrice A

    eigenvalues, U = np.linalg.eigh(A @ A.T) # valeurs et vecteurs propres de AAT
    index_sort = np.argsort(eigenvalues)[::-1] # indices du tri décroissant
    eigenvalues = eigenvalues[index_sort] # valeurs propres triées
    U = U[:, index_sort] # vecteurs propres triés

    eigenvalues = np.maximum(eigenvalues, 0) # éviter les valeurs négatives dues aux erreurs numériques

    singular_values = np.sqrt(eigenvalues) # valeurs singulières

    V = np.zeros((taille, taille)) # initialisation de V

    ATU = A.T @ U # calcul de A^T * U

    V[:, :k] = ATU[:, :k] / singular_values[:k] # calcul des k premiers vecteurs singuliers droits

    return U, V, singular_values

# Construction de la matrice sigma
def construire_sigma(singular_values, A, k):
    m, n = A.shape[:2] # dimensions de A
    sigma = np.zeros((m, n)) # initialisation de sigma
    for i in range(k):
        sigma[i, i] = singular_values[i] # remplissage des k premières valeurs singulières
    return sigma

# Construction de la matrice approximée
def construire_M(A, k):
    m, n = A.shape[:2] # dimensions de A
    if n < m:
        A = np.rot90(A) # rotation si n < m

    U, V, singular_values = calcul_U_V(A, k) # calcul de U, V et des valeurs singulières

    if n < m:
        return np.rot90(np.clip(U @ construire_sigma(singular_values, A, k) @ V.T, 0, 255), -1) # rotation inverse si n < m
    else:
        return np.clip(U @ construire_sigma(singular_values, A, k) @ V.T, 0, 255) # retour de l'approximation forcée dans [0,255]