import numpy as np

def calcul_U_V(A, k):
    taille = max(np.shape(A))

    eigenvalues, U = np.linalg.eigh(A @ A.T)
    index_sort = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[index_sort]
    U = U[:, index_sort]

    eigenvalues = np.maximum(eigenvalues, 0)

    singular_values = np.sqrt(eigenvalues)

    V = np.zeros((taille, taille))

    ATU = A.T @ U

    V[:, :k] = ATU[:, :k] / singular_values[:k]

    return U, V, singular_values

def construire_sigma(singular_values, A, k):
    m, n = A.shape[:2]
    sigma = np.zeros((m, n))
    for i in range(k):
        sigma[i, i] = singular_values[i]
    return sigma

def construire_M(A, k):
    m, n = A.shape[:2]
    if n < m:
        A = np.rot90(A)

    U, V, singular_values = calcul_U_V(A, k)

    if n < m:
        return np.rot90(np.clip(U @ construire_sigma(singular_values, A, k) @ V.T, 0, 255), -1)
    else:
        return np.clip(U @ construire_sigma(singular_values, A, k) @ V.T, 0, 255)