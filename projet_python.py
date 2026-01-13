#Le fichier `projet_python.py` est un script de 
# génération de données (Data Generation Script). Il crée des données 
# simulées pour les cas de paludisme en Mauritanie pour la période de 2018 à 2024. 
# Ces données sont basées sur des modèles réalistes qui prennent en compte 
# les variations géographiques et saisonnières de la maladie.

import pandas as pd
import numpy as np


# Explication:
# - pandas (pd): Bibliothèque pour créer et manipuler des DataFrames (tableaux de données structurées)
# - numpy (np): Bibliothèque pour générer des nombres aléatoires et effectuer des calculs mathématiques

# Pourquoi ces bibliothèques:
# - Pandas permet de structurer les données en colonnes et lignes avant de les sauvegarder
# - NumPy est utilisé pour ajouter de la variabilité aléatoire réaliste aux données simulées



## 2. Définition des constantes - Wilayas 

wilayas = [
    'Hodh Chargui', 'Hodh Gharbi', 'Assaba', 'Gorgol', 'Brakna',
    'Trarza', 'Adrar', 'Dakhlet Nouadhibou', 'Tagant', 'Guidimaka',
    'Tiris Zemmour', 'Inchiri', 'Nouakchott'
]

# Explication:
# - Liste contenant les 13 wilayas (régions administratives) de la Mauritanie
# - Ces noms correspondent aux divisions administratives réelles du pays
# - Sera utilisée pour créer une entrée de données pour chaque wilaya

# Wilayas mentionnées:
# - Ce sont les vraies régions administratives de la Mauritanie
# - Chaque wilaya aura ses propres données de cas



# 3. Définition des constantes - Années

years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]

# Explication:
# - Liste des années pour lesquelles les données seront générées
# - Période de 7 ans (2018 à 2024)
# - Correspond à la période historique pour laquelle on veut simuler des données

# Pourquoi cette période:
# - Donne suffisamment de données historiques pour les analyses et prédictions
# - 7 ans permettent d'observer les tendances et les cycles saisonniers

# 4. Initialisation de la liste de données
data = []

# Explication:
# - Crée une liste vide qui stockera toutes les lignes de données
# - Chaque élément de la liste sera une liste contenant [année, mois, wilaya, cas]

# Structure des données:
# - Chaque entrée aura le format: `[année, mois, wilaya, nombre_de_cas]`
# - Exemple: `[2018, 8, 'Hodh Chargui', 520]`

# 5. Boucle principale - Génération des données

for year in years:
    for month in range(1, 13):  # du mois 1 au mois 12
        for wilaya in wilayas:

# Explication:
# - Boucle triple imbriquée:
#   1. for year in years: Itère sur chaque année (7 itérations)
#   2. for month in range(1, 13): Itère sur chaque mois (1 à 12, donc 12 itérations)
#   3. for wilaya in wilayas: Itère sur chaque wilaya (13 itérations)

# Nombre total de lignes générées:
# - 7 années × 12 mois × 13 wilayas = **1,092 lignes de données**

# Pourquoi cette structure:
# - Crée une combinaison complète de toutes les années, mois et wilayas
# - Assure qu'il y a des données pour chaque combinaison possible

# 6. Logique de simulation - Saison des pluies
             is_rainy = month in [8, 9, 10]

# Explication:
# - Détermine si le mois actuel fait partie de la saison des pluies
# - Les mois 8, 9 et 10 correspondent à août, septembre et octobre
# - Retourne `True` si le mois est dans cette liste, `False` sinon

# Contexte médical:
# - La saison des pluies en Mauritanie (généralement août-octobre) favorise la propagation du paludisme
# - L'eau stagnante créée par les pluies permet la reproduction des moustiques (vecteurs du paludisme)
# - Donc, on s'attend à plus de cas pendant cette période

# 7. Logique de simulation - Base géographique 

base_cases = 100 if wilaya in ['Guidimaka', 'Hodh Chargui', 'Assaba'] else 20


# Explication:
# - Expression conditionnelle (ternaire): Si la wilaya est dans la liste, base = 100, sinon base = 20
# - Wilayas à haut risque: Guidimaka, Hodh Chargui, Assaba
#   - Ces wilayas reçoivent un nombre de base plus élevé (100 cas)
# - Autres wilayas: Reçoivent un nombre de base plus faible (20 cas)

# Raison géographique:
# - Certaines régions sont plus propices au paludisme en raison de:
#   - Climat plus humide
#   - Présence de rivières et zones d'eau
#   - Densité de population
#   - Conditions sanitaires

# 5x plus de cas de base dans les wilayas à haut risque reflète les différences épidémiologiques réelles

# 8. Multiplication pendant la saison des pluies
if is_rainy:
    base_cases *= 5  # multiplication des cas pendant la saison des pluies

# Explication:
# - Si c'est la saison des pluies (`is_rainy == True`), multiplie les cas de base par 5
# - Exemples de calcul:
#   - Wilaya normale (base=20) en août: 20 × 5 = **100 cas**
#   - Wilaya à haut risque (base=100) en août: 100 × 5 = **500 cas**
#   - Wilaya normale en janvier (pas de pluie): **20 cas** (pas de multiplication)

# Facteur 5:
# - Réaliste car la saison des pluies peut effectivement multiplier les cas par 3 à 10 fois
# - Le facteur 5 est un compromis réaliste

# 9. Ajout de variabilité aléatoire 

cases = int(base_cases + np.random.normal(0, 10))

# Explication:
# - np.random.normal(0, 10): Génère un nombre aléatoire suivant une distribution normale
#   - Moyenne (μ): 0 (pas de biais systématique)
#   - Écart-type (σ): 10 (variation modérée)
# - base_cases + ...: Ajoute cette variation aux cas de base
# - int(...): Convertit en nombre entier (on ne peut pas avoir 0.5 cas)

# Pourquoi ajouter de la variabilité:
# - Dans la réalité, les cas ne suivent pas une formule exacte
# - Il y a toujours des fluctuations naturelles (météo variable, interventions sanitaires, etc.)
# - Cette variabilité rend les données plus réalistes

# Exemples de variation:
# - Base = 100, variation peut être entre -30 et +30 environ (3 écarts-types)
# - Donc résultat final entre ~70 et ~130 cas

## 10. Protection contre les valeurs négatives


if cases < 0:
    cases = 0


# Explication:
# - Vérifie si le nombre de cas est devenu négatif (possible si la variation aléatoire était très négative)
# - Si c'est le cas, le remplace par 0

# Pourquoi c'est important:
# - On ne peut pas avoir un nombre négatif de cas de paludisme
# - Les données doivent rester logiques et utilisables
# - 0 est la valeur minimale réaliste

## 11. Ajout à la liste de données
data.append([year, month, wilaya, cases])

# Explication:
# - Ajoute une nouvelle ligne à la liste `data`
# - Format: `[année, mois, wilaya, nombre_de_cas]`
# - Cette ligne sera ensuite convertie en ligne de DataFrame

# Exemple concret:
# - `[2018, 8, 'Hodh Chargui', 485]` signifie:
#   - Année: 2018
#   - Mois: août (8)
#   - Wilaya: Hodh Chargui
#   - Cas: 485

## 12. Création du DataFrame 

df_wilayas = pd.DataFrame(data, columns=['Year', 'Month', 'Wilaya', 'Cases'])

# Explication:
# - pd.DataFrame(): Crée un DataFrame pandas à partir de la liste de données
# - columns=...: Définit les noms des colonnes
#   - `Year`: Année
#   - `Month`: Mois (1-12)
#   - `Wilaya`: Nom de la région
#   - `Cases`: Nombre de cas

# Résultat:
# - Un DataFrame avec 1,092 lignes et 4 colonnes
# - Format structuré prêt pour l'analyse

# Exemple de DataFrame:
# ```
#    Year  Month          Wilaya  Cases
# 0  2018      1  Hodh Chargui     95
# 1  2018      1   Hodh Gharbi     18
# 2  2018      1          Assaba    102
# ...

## 13. Sauvegarde en fichier CSV 

df_wilayas.to_csv('mauritania_wilayas_2018_2024.csv', index=False)

# Explication:
# - to_csv(): Sauvegarde le DataFrame dans un fichier CSV
# - 'mauritania_wilayas_2018_2024.csv': Nom du fichier de sortie
# - index=False: N'inclut pas la colonne d'index (les nombres 0, 1, 2...) dans le fichier CSV

# Format CSV:
# - Fichier texte avec valeurs séparées par des virgules
# - Peut être ouvert dans Excel, lu par d'autres programmes Python, etc.

# Fichier généré:

# Year,Month,Wilaya,Cases
# 2018,1,Hodh Chargui,95
# 2018,1,Hodh Gharbi,18
# 2018,1,Assaba,102
# ...

## 14. Message de confirmation (Ligne 35)
print("Le fichier des wilayas pour les années 2018-2024 a été créé avec succès !")


# Explication:
# - Affiche un message de confirmation dans la console
# - Indique à l'utilisateur que le script s'est exécuté avec succès

## Caractéristiques de la simulation

### Réalisme géographique
# ✅ Différencie les wilayas à haut risque (5x plus de cas de base)
# ✅ Reflète les variations régionales réelles du paludisme

## Réalisme saisonnier
# ✅ Multiplie les cas par 5 pendant la saison des pluies (août-octobre)
# ✅ Reflète l'augmentation réelle des cas pendant cette période

## Variabilité naturelle
# ✅ Ajoute de la variation aléatoire pour simuler les fluctuations réelles
# ✅ Évite des données trop régulières et artificielles

## Exemples de données générées

## Cas 1: Wilaya normale, hors saison des pluies
# - Wilaya: Nouakchott
# - Mois: Janvier (1)
# - Base: 20
# - Variation aléatoire: +5
# - **Résultat: 25 cas**

## Cas 2: Wilaya à haut risque, saison des pluies
# - Wilaya: Hodh Chargui
# - Mois: Septembre (9)
# - Base: 100 × 5 = 500
# - Variation aléatoire: -15
# - Résultat: 485 cas

## Cas 3: Wilaya normale, saison des pluies
# - Wilaya: Adrar
# - Mois: Octobre (10)
# - Base: 20 × 5 = 100
# - Variation aléatoire: +12
# - Résultat: 112 cas

## Utilisation des données générées

# Ce fichier CSV sera utilisé par:
# - analysis.py: Pour analyser les données et faire des prédictions
# - App.py: Pour créer une application web interactive de visualisation

# ## Comment exécuter
# python projet_python.py


# Résultat:
# - Crée le fichier `mauritania_wilayas_2018_2024.csv` dans le même dossier
# - Affiche un message de confirmation

# Note: 
# - Chaque exécution générera des données légèrement différentes à cause de la variabilité aléatoire
# - Si vous voulez des données identiques à chaque fois, vous pouvez fixer la graine aléatoire avec `np.random.seed(42)` au début du script

## Améliorations possibles

## 1. Ajouter des tendances temporelles
# - Augmentation ou diminution progressive au fil des années
# - Simuler l'impact des interventions sanitaires

## 2. Ajouter plus de variables
# - Températures
# - Précipitations
# - Interventions sanitaires
# - Densité de population

## 3. Modèles plus sophistiqués
# - Utiliser des distributions statistiques plus complexes
# - Intégrer des corrélations entre wilayas voisines

## 4. Validation des données
# - Vérifier que les données générées sont réalistes
# - Comparer avec des données réelles si disponibles

## Résumé

# Ce script est essentiel car il:
# 1. ✅ Génère des données de test réalistes
# 2. ✅ Permet de développer et tester les autres scripts sans données réelles
# 3. ✅ Simule les variations géographiques et saisonnières réelles
# 4. ✅ Crée un dataset cohérent et structuré

# Workflow complet:
# ```
# projet_python.py → génère → mauritania_wilayas_2018_2024.csv
#                                               ↓
#                                     utilisé par analysis.py et App.py
# ```
