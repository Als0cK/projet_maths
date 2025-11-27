Guide d utilisation des scripts de compression SVD
===================================================

Objet
-----
Scripts Python pour compresser une image avec la decomposition en valeurs singulieres (SVD), en niveaux de gris ou en couleur. Deux approches : calcul NumPy natif et version simplifiee dans `svdmaison.py`.

Prerequis
---------
- Python 3.x.
- Librairies : numpy, matplotlib.

Lancement rapide
----------------
1) Ouvrir un terminal dans ce dossier.
2) Executer un script, par exemple :
   - `python prj_maths.py`
   - `python prj_maths_2_0.py`
   - `python prj_maths_couleur.py`
   - `python prj_maths_couleur_2_0.py`
3) Le script affiche la taille du fichier d origine, ouvre une figure avec l image originale et des approximations, puis genere des fichiers compressees.
4) Appuyer sur Entree quand le script le demande pour quitter proprement.

Sorties generees
----------------
- Images compressees : `compressed_k3.jpg`, `compressed_k20.jpg`, `compressed_k<kmax>.jpg` (suffixe `_couleur_` pour prj_maths_couleur.py). Les valeurs de k sont les rangs utilises pour l approximation.
- Affichage : une fenetre Matplotlib avec l originale et les approximations.

Ajuster la compression
----------------------
- Modifier la liste `k_array` (ne pas dépasser 3 valeurs dans la tableau pour une bonne lisibilite de l'affichage matplotlib).
- Plus k est petit, plus la compression est forte (fichier leger mais details perdus).
- Plus k est grand, meilleure est la qualite (fichier plus lourd mais details preserves).

Changer l image source
----------------------
- Remplacer `coucher-de-soleil-sur-misurina.jpg` par une autre image dans le meme dossier.
- Les images au format portait et paysage sont supportees.
- Assurer que le nom du fichier dans le script correspond a celui de l image remplacee.

Conseils
--------
- Ne pas utiliser une image trop grande pour eviter une longue duree de calcul, le processus SVD peut etre gourmand en ressources.
- Tester avec differentes valeurs de k pour trouver le compromis ideal entre qualite et taille de fichier.
- Consulter les commentaires dans les scripts pour plus de details sur le fonctionnement interne.
- Deux autres images sont disponibles, ne vous aventurez pas dans la compression de 'pexels-maxfrancis-2246476.jpg' sans vous assurer d'avoir une machine pouvant encaisser le calcul, cette image est tres lourde.