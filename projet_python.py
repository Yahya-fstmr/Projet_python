import pandas as pd
import numpy as np

# Définition des constantes
wilayas = [
    'Hodh Chargui', 'Hodh Gharbi', 'Assaba', 'Gorgol', 'Brakna',
    'Trarza', 'Adrar', 'Dakhlet Nouadhibou', 'Tagant', 'Guidimaka',
    'Tiris Zemmour', 'Inchiri', 'Nouakchott'
]

# les années choisices
years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]

data = []
for year in years:
    for month in range(1, 13):  # du mois 1 au mois 12
        for wilaya in wilayas:
            # Simulation simple des valeurs basée sur la saison des pluies et la localisation géographique
            is_rainy = month in [8, 9, 10]
            base_cases = 100 if wilaya in ['Guidimaka', 'Hodh Chargui', 'Assaba'] else 20

            if is_rainy:
                base_cases *= 5  # multiplication des cas pendant la saison des pluies

            cases = int(base_cases + np.random.normal(0, 10))
            if cases < 0:
                cases = 0

            data.append([year, month, wilaya, cases])

# Création du fichier et sauvegarde
df_wilayas = pd.DataFrame(data, columns=['Year', 'Month', 'Wilaya', 'Cases'])
df_wilayas.to_csv('mauritania_wilayas_2018_2024.csv', index=False)

print("Le fichier des wilayas pour les années 2018-2024 a été créé avec succès !")
