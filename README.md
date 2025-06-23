# Ce dépôt a été crée pour coordonner les tâches du projet ISEN de fin d'années, spécifiquement celui pour l'IA

-----Cette partie répond au besoin client n°3-----
Objectif: Cette branche contient le nécessaire pour la prédiction de la trajectoire future des navires à partir des données contenues dans notre db
Source: Fichier CSV contenant les données brutes
Méthdes:
- Modèles: RandomForest, LinearRegression, DecisionTree
- x: vecteurs de positions passées
- y: vecteurs de positions futures (à 5, 10 et 15 minutes)
Evaluation: RMSE, cross-validation.
Précision: R²
Résultats attendus: Prédictions cohérentes avec les données réelles, permettant de visualiser la trajectoire future des navires.
Script:
 - Controle de saise
 - Conversion de la saisie en format float
  - Prédiction de la trajectoire future du navire
  - Affichage de la trajectoire future du navire
Utilisation du script:
python script.py LAT1 LON1 SOG1 COG1 Heading1 Length1 Draft1 LAT2 LON2 ...
Exemple pour LA LUNA:
python script.py 25.95847 -97.37876  0.0  0.0 0 200 32 25.95846 -97.37880  0.0  0.0 0 200 32
