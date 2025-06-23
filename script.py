import numpy as np
import matplotlib.pyplot as plt
import joblib
import sys
def main(args):
    if len(args)!= 14:
        print("ERREUR!")
        return
    
    #Conversion des arguments en float
    input = np.array([float(i) for i in args]).reshape(1, -1)

    #Chargement du modèle
    model_5 = joblib.load('model_5.pkl')
    model_10 = joblib.load('model_10.pkl')
    model_15 = joblib.load('model_15.pkl')

    #Prédiction²²²
    pred_5 = model_5.predict(input)
    pred_10 = model_10.predict(input)
    pred_15 = model_15.predict(input)

    print(f"Position prédite à +5 minutes: LAT={pred_5[0][0]}, LON={pred_5[0][1]}")
    print(f"Position prédite à +10 minutes: LAT={pred_10[0][0]}, LON={pred_10[0][1]}")
    print(f"Position prédite à +15 minutes: LAT={pred_15[0][0]}, LON={pred_15[0][1]}")

if __name__ == "__main__":
    main(sys.argv[1:]) #Exclure le nom du script de la liste des arguments
#Commande: python script.py LAT1 LON1 SOG1 COG1 Heading1 Length1 Draft1 LAT2 LON2 ...
#Exemple pour LA LUNA:
# python script.py 25.95847 -97.37876  0.0  0.0 0 200 32 25.95846 -97.37880  0.0  0.0 0 200 32