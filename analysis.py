import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Chargement des données
df = pd.read_csv('mauritania_wilayas_2018_2024.csv')

# Analyse à l’aide de NumPy et Pandas
# Calcul du total des cas par wilaya sur l’ensemble des années
total_by_wilaya = df.groupby('Wilaya')['Cases'].sum().sort_values(ascending=False)

# Calcul de la moyenne des cas par mois (pour identifier les périodes de pic)
monthly_avg = df.groupby('Month')['Cases'].mean()

# Utilisation de NumPy pour calculer certaines statistiques avancées
total_cases_array = df['Cases'].values
std_dev = np.std(total_cases_array)  # écart-type

print("--- Résumé de l’analyse ---")
print(f"Nombre total de cas enregistrés dans la simulation : {df['Cases'].sum()}")
print(f"Wilaya la plus touchée (hypothèse) : {total_by_wilaya.index[0]}")
print(f"Écart-type des cas : {std_dev:.2f}")
print("\nMoyenne des cas par mois :")
print(monthly_avg)

# Préparation des données pour l’entraînement
# Nous utiliserons le « mois » comme facteur principal de prédiction
X = df[['Month']].values
y = df['Cases'].values

# Création du modèle de prédiction et entraînement
model = LinearRegression()
model.fit(X, y)

# Prédiction pour l’année 2025 (par exemple pour le mois d’août – mois 8)
month_2025 = np.array([[8]])
prediction = model.predict(month_2025)

print(f"Prédiction pour le mois d’août 2025 : {int(prediction[0])} cas")
