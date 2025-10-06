import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os

image_path = "C:\\Users\\alban\\OneDrive\\INSA\\STPI2\\projet_maths\\feuilles-d-automne-colorees-transparentes.jpg"

# Charger une image couleur
A = imread(image_path).astype(float)

# Normalisation pour les PNG
if A.max() <= 1.0:
    A = (A * 255).astype(float)

# Taille maximale pour la compression
def k_max(A):
    m, n = A.shape[:2]
    return min(m, n)

# Fonction de compression SVD pour un canal
def compress_channel(channel, k):
    U, S, Vt = np.linalg.svd(channel, full_matrices=False)
    Uk = U[:, :k]
    Sk = np.diag(S[:k])
    Vk = Vt[:k, :]
    return Uk @ Sk @ Vk

# Compression couleur
def approx_color_image(k):
    R = compress_channel(A[:,:,0], k)
    G = compress_channel(A[:,:,1], k)
    B = compress_channel(A[:,:,2], k)
    # On recolle les canaux et on force dans [0,255]
    return np.clip(np.stack([R, G, B], axis=2), 0, 255)

# Affichage
plt.figure(figsize=(12,6))

plt.subplot(1,4,1)
plt.imshow(A.astype(np.uint8))
plt.title("Originale")
plt.axis("off")

k_array = [1, 20, k_max(A)]

for i, k in enumerate(k_array, start=2):
    img_k = approx_color_image(k)
    plt.subplot(1,4,i)
    plt.imshow(img_k.astype(np.uint8))
    plt.title(f"k={k}")
    plt.axis("off")

plt.show()

# Sauvegarde et taille des fichiers
def save_and_size(img, filename):
    plt.imsave(filename, img.astype(np.uint8))
    size_bytes = os.path.getsize(filename)
    print(f"{filename} : {size_bytes/1024:.2f} Ko ({size_bytes} octets)")

print(f"Originale : {os.path.getsize(image_path)/1024:.2f} Ko ({os.path.getsize(image_path)} octets)")

img5 = approx_color_image(k_array[0])
save_and_size(img5, "compressed_couleur_k5.jpg")

img20 = approx_color_image(k_array[1])
save_and_size(img20, "compressed_couleur_k20.jpg")

img100 = approx_color_image(k_array[2])
save_and_size(img100, "compressed_couleur_k100.jpg")