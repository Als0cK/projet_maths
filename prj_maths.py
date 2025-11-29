import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os

#variable image source
image_path = ".\\coucher-de-soleil-sur-misurina.jpg"

# Charger une image
A = imread(image_path).astype(float)

# Si l’image est en couleur (3 canaux), on la convertit en niveaux de gris
if A.ndim == 3:
    A = np.mean(A, axis=2)

# Taille maximale pour la compression
def k_max(A):
    m, n = A.shape[:2]
    return min(m, n)

# Calcul de la SVD
U, S, Vt = np.linalg.svd(A, full_matrices=False)

# Fonction d’approximation
def approx_image(k):
    Uk = U[:, :k]
    Sk = np.diag(S[:k])
    Vk = Vt[:k, :]
    img = Uk @ Sk @ Vk
    return np.clip(img, 0, 255)  # force dans [0,255]


# Sauvegarde et taille des fichiers
def save_and_size(img, filename):
    plt.imsave(filename, img, cmap="gray")
    size_bytes = os.path.getsize(filename)
    print(f"{filename} : {size_bytes/1024:.2f} Ko ({size_bytes} octets), réduction de {(1 - size_bytes/os.path.getsize(image_path))*100:.2f} %")

# Fonction d’affichage des images
def affichage_images():
    plt.figure(figsize=(12,6))

    plt.subplot(1,4,1)
    plt.imshow(A, cmap="gray")
    plt.title("Originale")
    plt.axis("off")

    for i, k in enumerate(k_array, start=2):
        img_k = approx_image(k)
        plt.subplot(1,4,i)
        plt.imshow(img_k, cmap="gray")
        plt.title(f"k={k}")
        plt.axis("off")

    plt.show(block = False)

# Fonction de sauvegarde des images compressées
def save_compressed_images():
    for k in k_array:
        img_k = approx_image(k)
        filename = f"compressed_k{k}.jpg"
        save_and_size(img_k, filename)

# Tableau des valeurs de k à tester
k_array = [1, 20, k_max(A)]

def main():
    print(f"Originale : {os.path.getsize(image_path)/1024:.2f} Ko ({os.path.getsize(image_path)} octets)") #affiche la taille de l’image originale
    affichage_images() #affiche les images compressées
    save_compressed_images() #sauvegarde les images compressées
    input("Appuyez sur entrée pour quitter...")

main()