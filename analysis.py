# Le fichier `analysis.py` est un script Python d'analyse de données pour 
# étudier les cas de paludisme en Mauritanie. Il charge les données historiques, 
# effectue des analyses statistiques et utilise un modèle d'apprentissage 
# automatique pour prédire les cas futurs.

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Explication:
# - pandas (pd): Bibliothèque pour manipuler et analyser les données tabulaires (DataFrames)
# - numpy (np): Bibliothèque pour les calculs mathématiques et statistiques
# - sklearn.linear_model.LinearRegression: Modèle de machine learning pour la régression linéaire, utilisé pour faire des prédictions

# ---

### 2. Chargement des données 
df = pd.read_csv('mauritania_wilayas_2018_2024.csv')

# Explication:
# - pd.read_csv(): Charge les données depuis un fichier CSV
# - Le fichier contient les cas de paludisme par wilaya (région), année et mois
# - Les données sont stockées dans un DataFrame pandas nommé `df`
# - Colonnes typiques: `Year`, `Month`, `Wilaya`, `Cases`

# 3. Analyse statistique - Total par wilaya :
total_by_wilaya = df.groupby('Wilaya')['Cases'].sum().sort_values(ascending=False)

# Explication:
# - **groupby('Wilaya')**: Groupe les données par wilaya (région)
# - **['Cases'].sum()**: Additionne tous les cas pour chaque wilaya sur toutes les années
# - **sort_values(ascending=False)**: Trie les résultats du plus élevé au plus bas
# - Résultat: Un objet Series avec chaque wilaya et son total de cas, trié décroissant

# Exemple de résultat:
# 
# Wilaya
# Hodh Chargui      12540
# Guidimaka         11230
# Assaba            10500
# ...


# 4. Analyse statistique - Moyenne mensuelle
monthly_avg = df.groupby('Month')['Cases'].mean()

# Explication
# - groupby('Month'): Groupe les données par mois (1 à 12)
# - ['Cases'].mean(): Calcule la moyenne des cas pour chaque mois, toutes années et toutes wilayas confondues
# - Permet d'identifier les mois avec le plus de cas en moyenne (périodes de pic épidémique)

# Pourquoi c'est utile:
# - Identifie la saisonnalité (ex: plus de cas pendant la saison des pluies, généralement août-septembre-octobre)
# - Aide à planifier les campagnes de prévention

# 5. Calcul de l'écart-type (Lignes 16-17)

total_cases_array = df['Cases'].values
std_dev = np.std(total_cases_array)

# Explication:
# - df['Cases'].values: Extrait toutes les valeurs de la colonne 'Cases' sous forme de tableau NumPy
# - np.std(): Calcule l'écart-type (standard deviation)
# - L'écart-type mesure la dispersion des données autour de la moyenne
#   - Valeur élevée = grande variation (cas très variables)
#   - Valeur faible = faible variation (cas assez constants)

# Signification:
# - Aide à comprendre la variabilité des données
# - Utile pour évaluer la fiabilité des prévisions

# 6. Affichage des résultats d'analyse

print("--- Résumé de l'analyse ---")
print(f"Nombre total de cas enregistrés dans la simulation : {df['Cases'].sum()}")
print(f"Wilaya la plus touchée (hypothèse) : {total_by_wilaya.index[0]}")
print(f"Écart-type des cas : {std_dev:.2f}")
print("\nMoyenne des cas par mois :")
print(monthly_avg)

# Explication:
# - df['Cases'].sum(): Additionne tous les cas dans tout le DataFrame
# - total_by_wilaya.index[0]: Prend la première wilaya de la liste triée (celle avec le plus de cas)
# - f"...": Formatage de chaîne (f-string) pour insérer des variables
# - {std_dev:.2f}: Affiche l'écart-type avec 2 décimales
# - print(monthly_avg): Affiche la série avec les moyennes par mois

# Sortie exemple:
# 
# --- Résumé de l'analyse ---
# Nombre total de cas enregistrés dans la simulation : 245680
# Wilaya la plus touchée (hypothèse) : Hodh Chargui
# Écart-type des cas : 45.23

# Moyenne des cas par mois :
# Month
# 1     850.5
# 2     920.3
# ...
# 8    4200.8  (pic pendant la saison des pluies)
# ...


# 7. Préparation des données pour l'entraînement

X = df[['Month']].values
y = df['Cases'].values

# Explication:
# - X: Variable indépendante (feature) - le mois (1 à 12)
#   - `[['Month']]` crée un DataFrame avec une seule colonne
#   - `.values` le convertit en tableau NumPy 2D
# - y: Variable dépendante (target) - le nombre de cas à prédire
#   - `.values` convertit en tableau NumPy 1D

# Note importante:
# - Ce modèle simple utilise uniquement le mois comme variable prédictive
# - Un modèle plus sophistiqué pourrait utiliser plusieurs variables (année, wilaya, températures, précipitations, etc.)


# 8. Création et entraînement du modèle

model = LinearRegression()
model.fit(X, y)

# Explication:
# - LinearRegression(): Crée une instance du modèle de régression linéaire
#   - Modèle mathématique: `y = a*x + b`
#   - `a` = coefficient (pente de la droite)
#   - `b` = intercept (ordonnée à l'origine)
# - model.fit(X, y): Entraîne le modèle avec les données
#   - Le modèle apprend la relation entre le mois (X) et le nombre de cas (y)
#   - Calcule automatiquement les valeurs optimales de `a` et `b`

# Comment fonctionne la régression linéaire:
# 1. Trace une droite qui passe "au mieux" à travers tous les points de données
# 2. Minimise l'erreur (distance entre les points réels et la droite)
# 3. Utilise cette droite pour prédire de nouvelles valeurs

# Limitations:
# - Suppose une relation linéaire (droite), ce qui peut ne pas être réaliste
# - Ne prend pas en compte la saisonnalité complexe ou d'autres facteurs

# ---

# 9. Prédiction pour l'avenir

# Prédiction pour l'année 2025 (par exemple pour le mois d'août – mois 8)
month_2025 = np.array([[8]])
prediction = model.predict(month_2025)

print(f"Prédiction pour le mois d'août 2025 : {int(prediction[0])} cas")


# Explication:
# - np.array([[8]]): Crée un tableau NumPy 2D avec la valeur 8 (août)
#   - Format `[[8]]` car le modèle attend un tableau 2D (matrice)
#   - 8 représente le mois d'août
# - model.predict(): Utilise le modèle entraîné pour prédire
#   - Le modèle applique la formule apprise: `cas_prévus = a * 8 + b`
# - prediction[0]: Extrait la première (et seule) valeur du tableau de prédictions
# - int(...): Convertit en nombre entier (on ne peut pas avoir 0.5 cas)
# - Affiche le résultat avec un message formaté

# Exemple de sortie:
# Prédiction pour le mois d'août 2025 : 4250 cas


# Flux de travail complet

# 1. Chargement: Lit les données historiques depuis le CSV
# 2. Analyse descriptive: Calcule des statistiques (totaux, moyennes, écarts-types)
# 3. Visualisation: Affiche les résultats de l'analyse
# 4. Préparation: Prépare les données pour le machine learning
# 5. Entraînement: Entraîne un modèle de régression linéaire
# 6. Prédiction: Utilise le modèle pour prédire les cas futurs


## Points forts

# ✅ Analyse statistique complète des données
# ✅ Identification des zones et périodes les plus touchées
# ✅ Prédiction basée sur l'apprentissage automatique
# ✅ Code simple et facile à comprendre

## Limitations et améliorations possibles

# ❌ Modèle trop simple: Utilise uniquement le mois, ignore d'autres facteurs importants
#    - Amélioration: Ajouter l'année, la wilaya, les variables climatiques

# ❌ Régression linéaire: Suppose une relation linéaire qui peut ne pas être réaliste
#    - Amélioration: Utiliser des modèles plus complexes (polynomiaux, ARIMA, LSTM)

# ❌ Pas de validation: Le modèle n'est pas testé sur des données de test
#    - Amélioration: Diviser les données en train/test, calculer des métriques d'erreur

# ❌ Une seule prédiction: Prédit seulement un mois
#    - Amélioration: Prédire tous les mois de 2025-2027

## Comment exécuter

# bash
# python analysis.py
#

# **Fichiers requis:**
# - `mauritania_wilayas_2018_2024.csv` doit exister dans le même dossier

# **Sortie attendue:**
# - Affichage dans la console des résultats de l'analyse et de la prédiction

# ---

# ## Relation avec les autres fichiers

# - **projet_python.py**: Génère le fichier CSV utilisé par `analysis.py`
# - **App.py**: Utilise un modèle similaire mais intégré dans une interface web interactive
# - **analysis.py**: Version script simple, idéale pour l'analyse rapide et les tests
