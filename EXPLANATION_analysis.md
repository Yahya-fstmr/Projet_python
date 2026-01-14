# شرح ملف البحث Python - Explanation du fichier de recherche Python

---

## باللغة العربية / En langue arabe

### نظرة عامة / Vue d'ensemble
ملف `analysis.py` هو ملف تحليل بيانات يستخدم مكتبات Python لتحليل بيانات حالات الملاريا في موريتانيا. يقوم الملف بتحميل البيانات من ملف CSV، وإجراء تحليلات إحصائية، واستخدام نموذج تعلم آلي للتنبؤ بالحالات المستقبلية.

### شرح الكود بالتفصيل / Explication détaillée du code

#### 1. استيراد المكتبات / Importation des bibliothèques
```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
```
- **pandas**: مكتبة لمعالجة وتحليل البيانات في شكل جداول (DataFrames)
- **numpy**: مكتبة للحسابات الرياضية والإحصائية
- **sklearn.linear_model.LinearRegression**: نموذج تعلم آلي للانحدار الخطي يستخدم للتنبؤ

#### 2. تحميل البيانات / Chargement des données
```python
df = pd.read_csv('mauritania_wilayas_2018_2024.csv')
```
- يقوم بتحميل ملف CSV الذي يحتوي على بيانات حالات الملاريا من 2018 إلى 2024
- يتم تخزين البيانات في متغير `df` (DataFrame)

#### 3. تحليل البيانات الأساسي / Analyse de base des données

**أ) حساب إجمالي الحالات حسب الولاية:**
```python
total_by_wilaya = df.groupby('Wilaya')['Cases'].sum().sort_values(ascending=False)
```
- يجمع جميع الحالات لكل ولاية (Wilaya) على مدى جميع السنوات
- يرتب النتائج من الأعلى إلى الأدنى

**ب) حساب متوسط الحالات الشهري:**
```python
monthly_avg = df.groupby('Month')['Cases'].mean()
```
- يحسب متوسط عدد الحالات لكل شهر (من 1 إلى 12)
- يساعد في تحديد فترات الذروة (موسم الأمطار)

**ج) حساب الانحراف المعياري:**
```python
total_cases_array = df['Cases'].values
std_dev = np.std(total_cases_array)
```
- يحسب الانحراف المعياري لجميع الحالات
- يقيس مدى توزع البيانات حول المتوسط

#### 4. عرض النتائج / Affichage des résultats
```python
print("--- Résumé de l'analyse ---")
print(f"Nombre total de cas enregistrés : {df['Cases'].sum()}")
print(f"Wilaya la plus touchée : {total_by_wilaya.index[0]}")
print(f"Écart-type des cas : {std_dev:.2f}")
```
- يعرض ملخص التحليل مع:
  - إجمالي الحالات المسجلة
  - الولاية الأكثر تأثراً
  - الانحراف المعياري

#### 5. بناء نموذج التنبؤ / Construction du modèle de prédiction

**أ) إعداد البيانات:**
```python
X = df[['Month']].values  # المتغير المستقل (الشهر)
y = df['Cases'].values     # المتغير التابع (عدد الحالات)
```
- `X`: الشهر كمتغير مستقل (من 1 إلى 12)
- `y`: عدد الحالات كمتغير تابع

**ب) تدريب النموذج:**
```python
model = LinearRegression()
model.fit(X, y)
```
- ينشئ نموذج انحدار خطي
- يدرب النموذج على البيانات التاريخية لتعلم العلاقة بين الشهر وعدد الحالات

**ج) التنبؤ:**
```python
month_2025 = np.array([[8]])  # شهر أغسطس (8)
prediction = model.predict(month_2025)
```
- يتنبأ بعدد الحالات المتوقعة لشهر أغسطس 2025
- يستخدم النموذج المدرب للتنبؤ بناءً على نمط البيانات التاريخية

### الهدف من الملف / Objectif du fichier
الهدف هو تحليل بيانات الملاريا في موريتانيا وتحديد:
1. الولايات الأكثر تأثراً
2. الأشهر التي تشهد ذروة في الحالات
3. التنبؤ بالحالات المستقبلية باستخدام التعلم الآلي

---

## En langue française / باللغة الفرنسية

### Vue d'ensemble / نظرة عامة
Le fichier `analysis.py` est un script d'analyse de données qui utilise des bibliothèques Python pour analyser les données des cas de paludisme en Mauritanie. Le fichier charge les données depuis un fichier CSV, effectue des analyses statistiques et utilise un modèle d'apprentissage automatique pour prédire les cas futurs.

### Explication détaillée du code / شرح الكود بالتفصيل

#### 1. Importation des bibliothèques / استيراد المكتبات
```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
```
- **pandas**: Bibliothèque pour manipuler et analyser les données sous forme de tableaux (DataFrames)
- **numpy**: Bibliothèque pour les calculs mathématiques et statistiques
- **sklearn.linear_model.LinearRegression**: Modèle d'apprentissage automatique de régression linéaire utilisé pour la prédiction

#### 2. Chargement des données / تحميل البيانات
```python
df = pd.read_csv('mauritania_wilayas_2018_2024.csv')
```
- Charge le fichier CSV contenant les données des cas de paludisme de 2018 à 2024
- Les données sont stockées dans la variable `df` (DataFrame)

#### 3. Analyse de base des données / تحليل البيانات الأساسي

**a) Calcul du total des cas par wilaya:**
```python
total_by_wilaya = df.groupby('Wilaya')['Cases'].sum().sort_values(ascending=False)
```
- Additionne tous les cas pour chaque wilaya (région) sur toutes les années
- Trie les résultats du plus élevé au plus bas

**b) Calcul de la moyenne mensuelle des cas:**
```python
monthly_avg = df.groupby('Month')['Cases'].mean()
```
- Calcule le nombre moyen de cas pour chaque mois (de 1 à 12)
- Aide à identifier les périodes de pic (saison des pluies)

**c) Calcul de l'écart-type:**
```python
total_cases_array = df['Cases'].values
std_dev = np.std(total_cases_array)
```
- Calcule l'écart-type de tous les cas
- Mesure la dispersion des données autour de la moyenne

#### 4. Affichage des résultats / عرض النتائج
```python
print("--- Résumé de l'analyse ---")
print(f"Nombre total de cas enregistrés : {df['Cases'].sum()}")
print(f"Wilaya la plus touchée : {total_by_wilaya.index[0]}")
print(f"Écart-type des cas : {std_dev:.2f}")
```
- Affiche un résumé de l'analyse avec:
  - Le total des cas enregistrés
  - La wilaya la plus touchée
  - L'écart-type

#### 5. Construction du modèle de prédiction / بناء نموذج التنبؤ

**a) Préparation des données:**
```python
X = df[['Month']].values  # Variable indépendante (le mois)
y = df['Cases'].values     # Variable dépendante (nombre de cas)
```
- `X`: Le mois comme variable indépendante (de 1 à 12)
- `y`: Le nombre de cas comme variable dépendante

**b) Entraînement du modèle:**
```python
model = LinearRegression()
model.fit(X, y)
```
- Crée un modèle de régression linéaire
- Entraîne le modèle sur les données historiques pour apprendre la relation entre le mois et le nombre de cas

**c) Prédiction:**
```python
month_2025 = np.array([[8]])  # Mois d'août (8)
prediction = model.predict(month_2025)
```
- Prédit le nombre de cas attendus pour août 2025
- Utilise le modèle entraîné pour prédire basé sur le modèle des données historiques

### Objectif du fichier / الهدف من الملف
L'objectif est d'analyser les données du paludisme en Mauritanie et d'identifier:
1. Les wilayas les plus touchées
2. Les mois qui connaissent un pic de cas
3. La prédiction des cas futurs en utilisant l'apprentissage automatique

---

## Résumé technique / الملخص التقني

**Technologies utilisées:**
- Pandas pour la manipulation de données
- NumPy pour les calculs statistiques
- Scikit-learn pour l'apprentissage automatique (régression linéaire)

**Méthode de prédiction:**
Le modèle utilise une régression linéaire simple où le mois est la variable d'entrée et le nombre de cas est la variable de sortie. Cette méthode suppose une relation linéaire entre le temps (mois) et le nombre de cas.

**Limitations:**
- Le modèle ne prend en compte que le mois comme facteur, sans considérer d'autres variables comme la météo, les interventions sanitaires, etc.
- La régression linéaire simple peut ne pas capturer des tendances non-linéaires complexes.
