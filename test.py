import pandas as pd
import joblib

# Charger le scaler et le modèle KMeans
scaler = joblib.load('scaler_model.joblib')
kmeans = joblib.load('kmeans_model.joblib')

# Colonnes attendues
interesting_columns = ['SOG', 'COG', 'Heading', 'LON', 'LAT']

def demander_valeurs():
    valeurs = []
    for col in interesting_columns:
        val = float(input(f"Entrez la valeur pour {col} : "))
        valeurs.append(val)
    return valeurs

if __name__ == "__main__":
    print("Veuillez entrer les valeurs pour chaque variable :")
    valeurs = demander_valeurs()
    input_data = pd.DataFrame([valeurs], columns=interesting_columns)
    input_scaled = scaler.transform(input_data)
    cluster = kmeans.predict(input_scaled)[0]
    # Pour KMeans, un point appartient toujours à un cluster, mais on peut ajouter une vérification de cohérence
    if cluster in range(kmeans.n_clusters):
        print(f"Le point appartient au cluster KMeans numéro : {cluster}")
    else:
        print("Ce point n'appartient à aucun cluster.")