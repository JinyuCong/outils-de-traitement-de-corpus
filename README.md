# outils-de-traitement-de-corpus


## Tâche

Détection des visages des humains. Je souhaite que le modèle puisse détecter l'emplacement des visages dans une image et représenter la plage des visages en utilisant des coordonnées de pixels.

## Corpus

Avec un dataset de taille d'à peu près 2000 photos des personnes avec leurs visages. Chaque photo de taille 64*64 est liée avec un label d'une suite de position de pixel, ces pixels couvrent les emplacements des visages dans l'image, chaque pixel étant représenté par ses coordonnées dans l'image, par exemple (100, 200) représente une coordonnée de la ligne 100 et de la colonne 200. 

## Type de prédiction peut servir ce corpus

Localisation de visages : Prédire les coordonnées (position) des visages dans une image ou une vidéo, souvent sous forme de boîtes englobantes (bounding boxes).

## à quel modèle il a servi

Certains modèles spécifiquement conçus pour la détection d'objets, tels que Faster R-CNN, YOLO (You Only Look Once), SSD (Single Shot MultiBox Detector), RetinaNet, etc., peuvent être adaptés pour détecter les visages. Plus spécifiquement on peut utiliser le modèle CascadeClassifier de cv2.



