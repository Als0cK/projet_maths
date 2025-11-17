import svdmaison as svd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os

image_path = "..\\projet_maths\\coucher-de-soleil-sur-misurina.jpg"

# Charger une image
A = imread(image_path).astype(float)

# Si l’image est en couleur (3 canaux), on la convertit en niveaux de gris
if A.ndim == 3:
    A = np.mean(A, axis=2)

# Taille maximale pour la compression
def k_max(A):
    m, n = A.shape[:2]
    return min(m, n)

# Sauvegarde et taille des fichiers
def save_and_size(img, filename):
    plt.imsave(filename, img, cmap="gray")
    size_bytes = os.path.getsize(filename)
    print(f"{filename} : {size_bytes/1024:.2f} Ko ({size_bytes} octets), réduction de {(1 - size_bytes/os.path.getsize(image_path))*100:.2f} %")

def save_compressed_images():
    for k in [3, 20, k_max(A)]:
        img_k = svd.construire_M(A, k)
        filename = f"compressed_k{k}.jpg"
        save_and_size(img_k, filename)

def affichage_images():
    plt.figure(figsize=(12,6))

    plt.subplot(1,4,1)
    plt.imshow(A, cmap="gray")
    plt.title("Originale")
    plt.axis("off")

    k_array = [1, 20, k_max(A)]

    for i, k in enumerate(k_array, start=2):
        img_k = svd.construire_M(A, k)
        plt.subplot(1,4,i)
        plt.imshow(img_k, cmap="gray")
        plt.title(f"k={k}")
        plt.axis("off")
    plt.show(block = False)

def main():
    print(f"Originale : {os.path.getsize(image_path)/1024:.2f} Ko ({os.path.getsize(image_path)} octets)")
    affichage_images()
    save_compressed_images()
    input("Appuyez sur entrée pour quitter...")

main()