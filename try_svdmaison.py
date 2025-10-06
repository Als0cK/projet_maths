import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os

image_path = "C:\\Users\\alban\\OneDrive\\INSA\\STPI2\\projet_maths\\coucher-de-soleil-sur-misurina.jpg"

# Taille maximale pour la compression
def k_max(A):
    m, n = A.shape[:2]
    return min(m, n)

# Charger une image
A = imread(image_path).astype(float)

# Si l’image est en couleur (3 canaux), on la convertit en niveaux de gris
if A.ndim == 3:
    A = np.mean(A, axis=2)

eigenvalues, U = np.linalg.eigh(A @ A.T)

index_sort = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[index_sort]
U = U[:, index_sort]

eigenvalues, V = np.linalg.eigh(A.T @ A)

index_sort = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[index_sort]
V = V[:, index_sort]

def construire_sigma(eigenvalues, A):
    m, n = A.shape[:2]
    sigma = np.zeros((m, n))
    for i in range(k_max(A)):
        sigma[i, i] = np.sqrt(eigenvalues[i])
    return sigma

def construire_M(eigenvalues, U, V, A):
    return U @ construire_sigma(eigenvalues, A) @ V.T

image_compressed = construire_M(eigenvalues, U, V, A)
plt.imshow(image_compressed, cmap='gray')
plt.axis('off')
plt.show()