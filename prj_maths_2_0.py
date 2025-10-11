import svdmaison as svd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os

image_path = "C:\\Users\\alban\\OneDrive\\INSA\\STPI2\\projet_maths\\coucher-de-soleil-sur-misurina.jpg"

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
    print(f"{filename} : {size_bytes/1024:.2f} Ko ({size_bytes} octets)")


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

plt.show()

# Sauvegarde
print(f"Originale : {os.path.getsize(image_path)/1024:.2f} Ko "
      f"({os.path.getsize(image_path)} octets)")

img3 = svd.construire_M(A, 3)
save_and_size(img3, "compressed_k3.jpg")

img20 = svd.construire_M(A, 20)
save_and_size(img20, "compressed_k20.jpg")

img_full = svd.construire_M(A, k_max(A))
save_and_size(img_full, "compressed_k_max.jpg")