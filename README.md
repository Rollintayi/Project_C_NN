# Cette brache sert à répondre au besoin client 1
Préparation des données :
• Extraction des données d’intérêt : sélectionner les colonnes pertinentes de la base de données selon ce besoin.
• Encodage des données catégorielles si nécessaire : utiliser des techniques de prétraitement pour convertir les données non numériques en données
numériques si nécessaire. Référez-vous à https://scikit-learn.org/stable/modules/preprocessing.html
• Apprentissage non-supervisé :
• Choix de l'algorithme de clustering : sélectionner un/des algorithme(s) de clustering pour regrouper les navires selon des schémas de navigation
similaires . Référez-vous à https://scikit-learn.org/stable/modules/clustering.html
• Détermination du nombre de clusters : expérimenter avec différents nombres de clusters pour voir quel modèle offre le meilleur regroupement.
• Métriques pour l'apprentissage non-supervisé :
• Évaluation des clusters : utiliser des métriques pour évaluer la qualité du clustering. Référez-vous aux méthodes : Silhouette Coefficient , Calinski-Harabasz
Index , Davies-Bouldin Index.
• Visualisation sur un carte :
• Création de la carte : utiliser une bibliothèque de visualisation pour représenter les bateaux sur une carte avec des couleurs différentes pour chaque
cluster. Référez-vous à https://plotly.com/python/scattermapbox/
• Préparation d'un script :
• Écrire un script prenant en entré les spécificités d’un navire et qui renvoie le cluster associé. Un exemple de script est fourni dans les ressources du
projet.
• Attention : le script ne doit pas relancer une recherche des clusters à chaque usage, il doit impérativement charger le
modèle préalablement enregistré.
Les attendus
• Justifier le choix des variables sélectionnées
• Justifier le choix du modèle de clustering + Expliquer le principe de son fonctionnement
• Justifier le choix des métriques et discuter les résultats obtenus (tableau + graphes)
