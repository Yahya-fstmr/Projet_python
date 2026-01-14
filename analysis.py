import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('mauritania_wilayas_2018_2024.csv')


total_by_wilaya = df.groupby('Wilaya')['Cases'].sum().sort_values(ascending=False)


monthly_avg = df.groupby('Month')['Cases'].mean()



total_cases_array = df['Cases'].values
std_dev = np.std(total_cases_array)


print("--- Résumé de l'analyse ---")
print(f"Nombre total de cas enregistrés dans la simulation : {df['Cases'].sum()}")
print(f"Wilaya la plus touchée (hypothèse) : {total_by_wilaya.index[0]}")
print(f"Écart-type des cas : {std_dev:.2f}")
print("\nMoyenne des cas par mois :")
print(monthly_avg)



X = df[['Month']].values
y = df['Cases'].values

model = LinearRegression()
model.fit(X, y)

month_2025 = np.array([[8]])
prediction = model.predict(month_2025)

print(f"Prédiction pour le mois d'août 2025 : {int(prediction[0])} cas")