# شرح ملفات Python - Explanation des fichiers Python

---

## ملف 1: projet_python.py / Fichier 1: projet_python.py

---

### باللغة العربية / En langue arabe

#### نظرة عامة / Vue d'ensemble
ملف `projet_python.py` هو ملف إنشاء البيانات (Data Generation Script). يقوم بإنشاء بيانات محاكاة لحالات الملاريا في موريتانيا للفترة من 2018 إلى 2024. الملف ينشئ ملف CSV يحتوي على بيانات منظمة لكل ولاية (Wilaya) لكل شهر من كل سنة.

#### شرح الكود بالتفصيل / Explication détaillée du code

**1. استيراد المكتبات:**
```python
import pandas as pd
import numpy as np
```
- **pandas**: لإنشاء وإدارة البيانات في شكل جداول
- **numpy**: لإضافة قيم عشوائية واقعية للبيانات

**2. تعريف الثوابت:**
```python
wilayas = [
    'Hodh Chargui', 'Hodh Gharbi', 'Assaba', 'Gorgol', 'Brakna',
    'Trarza', 'Adrar', 'Dakhlet Nouadhibou', 'Tagant', 'Guidimaka',
    'Tiris Zemmour', 'Inchiri', 'Nouakchott'
]
years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
```
- قائمة بجميع الولايات (Wilayas) في موريتانيا (13 ولاية)
- قائمة بالسنوات من 2018 إلى 2024

**3. إنشاء البيانات:**
```python
data = []
for year in years:
    for month in range(1, 13):  # من الشهر 1 إلى 12
        for wilaya in wilayas:
```
- حلقة ثلاثية المستويات: لكل سنة، لكل شهر، لكل ولاية
- ينشئ سجل واحد لكل تركيبة (سنة + شهر + ولاية)

**4. منطق المحاكاة:**
```python
is_rainy = month in [8, 9, 10]  # أغسطس، سبتمبر، أكتوبر
base_cases = 100 if wilaya in ['Guidimaka', 'Hodh Chargui', 'Assaba'] else 20
```
- **is_rainy**: يحدد إذا كان الشهر في موسم الأمطار (أغسطس-أكتوبر)
- **base_cases**: 
  - 100 حالة للولايات الأكثر تأثراً (Guidimaka, Hodh Chargui, Assaba)
  - 20 حالة للولايات الأخرى

**5. حساب الحالات:**
```python
if is_rainy:
    base_cases *= 5  # مضاعفة الحالات في موسم الأمطار

cases = int(base_cases + np.random.normal(0, 10))
if cases < 0:
    cases = 0
```
- في موسم الأمطار: الحالات الأساسية × 5
- إضافة قيمة عشوائية باستخدام التوزيع الطبيعي (متوسط 0، انحراف معياري 10)
- التأكد من أن عدد الحالات لا يكون سالباً

**6. حفظ البيانات:**
```python
df_wilayas = pd.DataFrame(data, columns=['Year', 'Month', 'Wilaya', 'Cases'])
df_wilayas.to_csv('mauritania_wilayas_2018_2024.csv', index=False)
```
- تحويل القائمة إلى DataFrame
- حفظها في ملف CSV للاستخدام في التحليلات الأخرى

#### الهدف من الملف / Objectif du fichier
إنشاء بيانات محاكاة واقعية لحالات الملاريا بناءً على:
- الفروقات الجغرافية بين الولايات
- التغيرات الموسمية (موسم الأمطار)
- التباين العشوائي الطبيعي

---

### En langue française / باللغة الفرنسية

#### Vue d'ensemble / نظرة عامة
Le fichier `projet_python.py` est un script de génération de données (Data Generation Script). Il crée des données simulées pour les cas de paludisme en Mauritanie pour la période de 2018 à 2024. Le fichier génère un fichier CSV contenant des données structurées pour chaque wilaya (région) pour chaque mois de chaque année.

#### Explication détaillée du code / شرح الكود بالتفصيل

**1. Importation des bibliothèques:**
```python
import pandas as pd
import numpy as np
```
- **pandas**: Pour créer et gérer les données sous forme de tableaux
- **numpy**: Pour ajouter des valeurs aléatoires réalistes aux données

**2. Définition des constantes:**
```python
wilayas = [
    'Hodh Chargui', 'Hodh Gharbi', 'Assaba', 'Gorgol', 'Brakna',
    'Trarza', 'Adrar', 'Dakhlet Nouadhibou', 'Tagant', 'Guidimaka',
    'Tiris Zemmour', 'Inchiri', 'Nouakchott'
]
years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
```
- Liste de toutes les wilayas (régions) en Mauritanie (13 wilayas)
- Liste des années de 2018 à 2024

**3. Création des données:**
```python
data = []
for year in years:
    for month in range(1, 13):  # Du mois 1 au 12
        for wilaya in wilayas:
```
- Boucle à trois niveaux: pour chaque année, pour chaque mois, pour chaque wilaya
- Crée un enregistrement pour chaque combinaison (année + mois + wilaya)

**4. Logique de simulation:**
```python
is_rainy = month in [8, 9, 10]  # Août, septembre, octobre
base_cases = 100 if wilaya in ['Guidimaka', 'Hodh Chargui', 'Assaba'] else 20
```
- **is_rainy**: Détermine si le mois est dans la saison des pluies (août-octobre)
- **base_cases**: 
  - 100 cas pour les wilayas les plus touchées (Guidimaka, Hodh Chargui, Assaba)
  - 20 cas pour les autres wilayas

**5. Calcul des cas:**
```python
if is_rainy:
    base_cases *= 5  # Multiplication des cas pendant la saison des pluies

cases = int(base_cases + np.random.normal(0, 10))
if cases < 0:
    cases = 0
```
- Pendant la saison des pluies: cas de base × 5
- Ajout d'une valeur aléatoire en utilisant une distribution normale (moyenne 0, écart-type 10)
- S'assurer que le nombre de cas n'est pas négatif

**6. Sauvegarde des données:**
```python
df_wilayas = pd.DataFrame(data, columns=['Year', 'Month', 'Wilaya', 'Cases'])
df_wilayas.to_csv('mauritania_wilayas_2018_2024.csv', index=False)
```
- Convertit la liste en DataFrame
- Sauvegarde dans un fichier CSV pour utilisation dans d'autres analyses

#### Objectif du fichier / الهدف من الملف
Créer des données simulées réalistes pour les cas de paludisme basées sur:
- Les différences géographiques entre les wilayas
- Les variations saisonnières (saison des pluies)
- La variation aléatoire naturelle

---

## ملف 2: App.py / Fichier 2: App.py

---

### باللغة العربية / En langue arabe

#### نظرة عامة / Vue d'ensemble
ملف `App.py` هو تطبيق ويب تفاعلي مبني باستخدام Streamlit لعرض وتحليل بيانات الملاريا في موريتانيا. يوفر واجهة مستخدم جميلة مع خرائط جغرافية، رسوم بيانية، وتحليلات تنبؤية باستخدام التعلم الآلي.

#### شرح الكود بالتفصيل / Explication détaillée du code

**1. استيراد المكتبات:**
```python
import streamlit as st
import pandas as pd
import plotly.express as px
import json
import numpy as np
from sklearn.linear_model import LinearRegression
import base64
```
- **streamlit**: لإنشاء تطبيق الويب التفاعلي
- **pandas**: لمعالجة البيانات
- **plotly.express**: لإنشاء رسوم بيانية تفاعلية
- **json**: لقراءة ملفات GeoJSON للخرائط
- **sklearn**: لنموذج التنبؤ بالتعلم الآلي
- **base64**: لتحويل الصور إلى تنسيق base64

**2. دالة تحميل الصور:**
```python
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
```
- تحويل الصور إلى تنسيق base64 لاستخدامها كخلفية في CSS

**3. تخصيص التصميم (CSS):**
```python
st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{
        background-image: linear-gradient(...);
    }}
    ...
    </style>
""", unsafe_allow_html=True)
```
- تخصيص مظهر التطبيق:
  - خلفية للشريط الجانبي
  - ألوان للبطاقات والمقاييس
  - تنسيق القوائم المنسدلة

**4. تحميل البيانات:**
```python
@st.cache_data
def load_data():
    df = pd.read_csv('mauritania_wilayas_2018_2024.csv')
    with open('mrt_admin1.geojson', encoding='utf-8') as f:
        geojson = json.load(f)
    return df, geojson
```
- **@st.cache_data**: تخزين مؤقت للبيانات لتحسين الأداء
- تحميل بيانات CSV وملف GeoJSON للخرائط

**5. القائمة الجانبية (Sidebar):**
```python
st.sidebar.title("🩺 Menu principal")
page = st.sidebar.radio("Aller à :", ["📊 Analyse historique", "🔮 Prédiction triennale (2025-2027)"])
selected_year = st.sidebar.selectbox("Choisir l'année :", sorted(df['Year'].unique(), reverse=True))
```
- قائمة تنقل بين صفحتين:
  - **Analyse historique**: تحليل البيانات التاريخية
  - **Prédiction triennale**: التنبؤ بالسنوات الثلاث القادمة
- اختيار السنة للعرض

**6. صفحة التحليل التاريخي:**
```python
if page == "📊 Analyse historique":
    st.title("🦠 Tableau d'analyse de la propagation du paludisme (2018-2024)")
    df_selected = df[df['Year'] == selected_year]
```

**أ) المقاييس الرئيسية:**
```python
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Nombre total de cas", f"{df_selected['Cases'].sum():,}")
with c2:
    st.metric("Wilaya la plus touchée", ...)
with c3:
    st.metric("Année sélectionnée", selected_year)
```
- عرض ثلاث بطاقات مقاييس:
  - إجمالي الحالات
  - الولاية الأكثر تأثراً
  - السنة المختارة

**ب) الخريطة الجغرافية:**
```python
fig_map = px.choropleth_mapbox(
    df_selected,
    geojson=mauri_geojson,
    locations='Wilaya',
    featureidkey="properties.adm1_name",
    color='Cases',
    color_continuous_scale="Reds",
    ...
)
```
- خريطة ملونة تعرض عدد الحالات لكل ولاية
- الألوان الحمراء تشير إلى المناطق الأكثر تأثراً

**ج) الرسم البياني الشريطي:**
```python
wilaya_data = df_selected.groupby('Wilaya')['Cases'].sum().sort_values()
px.bar(wilaya_data, orientation='h', ...)
```
- رسم بياني شريطي أفقي يوضح الحالات لكل ولاية

**د) الرسم البياني الخطي الشهري:**
```python
monthly_trend = df_selected.groupby('Month')['Cases'].sum().reset_index()
px.line(monthly_trend, x='Month', y='Cases', markers=True)
```
- رسم بياني خطي يوضح تطور الحالات خلال أشهر السنة

**7. صفحة التنبؤ (Prédiction):**
```python
else:
    st.title("🔮 Prédiction stratégique triennale (2025 - 2027)")
```

**أ) إعداد النموذج:**
```python
df_w = df[df['Wilaya'] == selected_w].copy()
df_w['Time_Index'] = (df_w['Year'] - 2018) * 12 + df_w['Month']
model = LinearRegression().fit(df_w[['Time_Index']].values, df_w['Cases'].values)
```
- إنشاء فهرس زمني (Time_Index) يمثل الشهر من بداية 2018
- تدريب نموذج الانحدار الخطي على البيانات التاريخية

**ب) التنبؤ:**
```python
future_indices = np.array([[i] for i in range(85, 121)])  # 36 شهر (2025-2027)
future_preds = model.predict(future_indices)
```
- التنبؤ بالحالات للـ 36 شهراً القادمة (2025-2027)
- الفهرس 85-96 = 2025، 97-108 = 2026، 109-120 = 2027

**ج) عرض التنبؤات:**
```python
df_future = pd.DataFrame({
    'Index': range(85, 121),
    'Mois': (list(range(1, 13)) * 3),
    'Année': (['2025'] * 12 + ['2026'] * 12 + ['2027'] * 12),
    'Cas_Prévus': np.maximum(0, future_preds).astype(int)
})
```
- إنشاء DataFrame يحتوي على التنبؤات الشهرية

**د) خريطة التنبؤات الجغرافية:**
```python
for w in wilayas:
    df_tmp = df[df['Wilaya'] == w].copy()
    m_tmp = LinearRegression().fit(...)
    year_total = m_tmp.predict(...).sum()
    map_list.append({'Wilaya': w, 'Total_Prévu': int(max(0, year_total))})
```
- إنشاء نموذج تنبؤ لكل ولاية
- حساب إجمالي الحالات المتوقعة لكل سنة
- عرضها على خريطة جغرافية

**هـ) التوصيات:**
```python
total_2025 = df_future[df_future['Année'] == '2025']['Cas_Prévus'].sum()
total_2027 = df_future[df_future['Année'] == '2027']['Cas_Prévus'].sum()
st.success(f"La wilaya de {selected_w} devrait connaître une tendance à la {'hausse' if total_2027 > total_2025 else 'baisse progressive'}...")
```
- مقارنة 2025 و 2027 لتحديد الاتجاه
- تقديم توصيات بناءً على النتائج

#### الهدف من الملف / Objectif du fichier
تطبيق ويب شامل يوفر:
1. **تحليل تفاعلي**: عرض البيانات التاريخية بطرق مختلفة
2. **تنبؤات ذكية**: استخدام التعلم الآلي للتنبؤ بالمستقبل
3. **تصورات جغرافية**: خرائط تفاعلية لعرض البيانات
4. **واجهة مستخدم جميلة**: تصميم احترافي وسهل الاستخدام

---

### En langue française / باللغة الفرنسية

#### Vue d'ensemble / نظرة عامة
Le fichier `App.py` est une application web interactive construite avec Streamlit pour afficher et analyser les données du paludisme en Mauritanie. Il fournit une interface utilisateur élégante avec des cartes géographiques, des graphiques et des analyses prédictives utilisant l'apprentissage automatique.

#### Explication détaillée du code / شرح الكود بالتفصيل

**1. Importation des bibliothèques:**
```python
import streamlit as st
import pandas as pd
import plotly.express as px
import json
import numpy as np
from sklearn.linear_model import LinearRegression
import base64
```
- **streamlit**: Pour créer l'application web interactive
- **pandas**: Pour manipuler les données
- **plotly.express**: Pour créer des graphiques interactifs
- **json**: Pour lire les fichiers GeoJSON pour les cartes
- **sklearn**: Pour le modèle de prédiction par apprentissage automatique
- **base64**: Pour convertir les images en format base64

**2. Fonction de chargement d'images:**
```python
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
```
- Convertit les images en format base64 pour les utiliser comme arrière-plan en CSS

**3. Personnalisation du design (CSS):**
```python
st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), {sidebar_bg};
        background-size: cover;
        background-position: center;
    }}

    /* 2. Fond de la page principale pour réduire l'éblouissement */
    [data-testid="stAppViewContainer"] {{
        background-color: #f8fafc !important;
    }}

    /* 3. Style des cartes de métriques (Metrics) */
    div[data-testid="stMetric"] {{
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        border-bottom: 4px solid #3b82f6; /* Ligne bleue médicale */
    }}

    /* 4. Style du menu déroulant (Selectbox) */
    div[data-baseweb="select"] > div {{
        background-color: white !important;
        color: black !important;
        border-radius: 8px !important;
    }}
    
    /* Couleur du texte dans la barre latérale */
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}

    /* Titres principaux */
    h1 {{
        color: #1e40af !important;
        font-weight: 700 !important;
    }}
    </style>
""", unsafe_allow_html=True)
```
#- Personnalise l'apparence de l'application:
 # - Arrière-plan pour la barre latérale
  #- Couleurs pour les cartes et métriques
  #- Formatage des menus déroulants

**4. Chargement des données:**
```python
@st.cache_data
def load_data():
    df = pd.read_csv('mauritania_wilayas_2018_2024.csv')
    with open('mrt_admin1.geojson', encoding='utf-8') as f:
        geojson = json.load(f)
    return df, geojson
```
- **@st.cache_data**: Mise en cache des données pour améliorer les performances
- Charge les données CSV et le fichier GeoJSON pour les cartes

**5. Barre latérale (Sidebar):**
```python
st.sidebar.title("🩺 Menu principal")
page = st.sidebar.radio("Aller à :", ["📊 Analyse historique", "🔮 Prédiction triennale (2025-2027)"])
selected_year = st.sidebar.selectbox("Choisir l'année :", sorted(df['Year'].unique(), reverse=True))
st.sidebar.markdown("---")
st.sidebar.markdown("### 🖋️ Préparé par :")
st.sidebar.info("**Yahya Sidna**\n\n**Aly Mohamed**")

'''  ```
- Menu de navigation entre deux pages:
  - **Analyse historique**: Analyse des données historiques
  - **Prédiction triennale**: Prédiction pour les trois prochaines années
- Sélection de l'année à afficher

**6. Page d'analyse historique:**
```python '''
if page == "📊 Analyse historique":
    st.title("🦠 Tableau d'analyse de la propagation du paludisme (2018-2024)")
    df_selected = df[df['Year'] == selected_year]
''' ```

**a) Métriques principales:**
```python '''
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Nombre total de cas", f"{df_selected['Cases'].sum():,}")
with c2:
    st.metric("Wilaya la plus touchée", df_selected.groupby('Wilaya')['Cases'].sum().idxmax())
with c3:
    st.metric("Année sélectionnée", selected_year)

''' ```
- Affiche trois cartes de métriques:
  - Total des cas
  - Wilaya la plus touchée
  - Année sélectionnée

**b) Carte géographique:**
```python '''
col_left, col_right = st.columns([1.5, 1])
with col_left:
 fig_map = px.choropleth_mapbox(
    df_selected,
    geojson=mauri_geojson,
    locations='Wilaya',
    featureidkey="properties.adm1_name",
    color='Cases',
    color_continuous_scale="Reds",
     mapbox_style="carto-positron",
            zoom=4.2,
            center={"lat": 20.2, "lon": -12.7},
            opacity=0.7
 )
 fig_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        st.plotly_chart(fig_map, use_container_width=True)

   
''' ```
- Carte colorée affichant le nombre de cas pour chaque wilaya
- Les couleurs rouges indiquent les zones les plus touchées

**c) Graphique en barres:**
```python  '''
with col_right:
 wilaya_data = df_selected.groupby('Wilaya')['Cases'].sum().sort_values()
 st.plotly_chart(
   px.bar(wilaya_data, orientation='h', color_continuous_scale="Reds"),
            use_container_width=True
            )

''' ```
- Graphique en barres horizontal montrant les cas par wilaya

**d) Graphique linéaire mensuel:**
```python '''
st.subheader(f"📈 Évolution mensuelle des cas en {selected_year}")
monthly_trend = df_selected.groupby('Month')['Cases'].sum().reset_index()
st.plotly_chart(
  px.line(monthly_trend, x='Month', y='Cases', markers=True),use_container_width=True)

st.subheader(f"📈 Évolution mensuelle des cas en {selected_year}")
    monthly_trend = df_selected.groupby('Month')['Cases'].sum().reset_index()
    st.plotly_chart(
        px.line(monthly_trend, x='Month', y='Cases', markers=True),
        use_container_width=True
    )  

''' ```
- Graphique linéaire montrant l'évolution des cas au cours des mois de l'année

**7. Page de prédiction:**
```python '''
else:
    st.title("🔮 Prédiction stratégique triennale (2025 - 2027)")
      st.info("Utilisation d’un modèle avancé de Machine Learning pour prédire la tendance générale de la maladie sur trois années à venir.")

    wilayas = df['Wilaya'].unique()
    selected_w = st.selectbox("Choisir une wilaya pour analyser son évolution future :", wilayas)


''' ```

**a) Préparation du modèle:**
```python '''
    # Préparation des données historiques pour l’entraînement
    df_w = df[df['Wilaya'] == selected_w].copy()
    df_w['Time_Index'] = (df_w['Year'] - 2018) * 12 + df_w['Month']
    model = LinearRegression().fit(df_w[['Time_Index']].values, df_w['Cases'].values)

''' ```
- Crée un index temporel (Time_Index) représentant le mois depuis le début de 2018
- Entraîne le modèle de régression linéaire sur les données historiques

**b) Prédiction:**
```python '''
future_indices = np.array([[i] for i in range(85, 121)])  # 36 mois (2025-2027)
future_preds = model.predict(future_indices)

''' ```
- Prédit les cas pour les 36 prochains mois (2025-2027)
- Index 85-96 = 2025, 97-108 = 2026, 109-120 = 2027

**c) Affichage des prédictions:**
```python '''

df_future = pd.DataFrame({
    'Index': range(85, 121),
    'Mois': (list(range(1, 13)) * 3),
    'Année': (['2025'] * 12 + ['2026'] * 12 + ['2027'] * 12),
    'Cas_Prévus': np.maximum(0, future_preds).astype(int)
})

''' ```
- Crée un DataFrame contenant les prédictions mensuelles

**d) Carte des prédictions géographiques:**
```python '''
for w in wilayas:
    df_tmp = df[df['Wilaya'] == w].copy()
    m_tmp = LinearRegression().fit(...)
    year_total = m_tmp.predict(...).sum()
    map_list.append({'Wilaya': w, 'Total_Prévu': int(max(0, year_total))})
```
- Crée un modèle de prédiction pour chaque wilaya
- Calcule le total des cas prévus pour chaque année
- Les affiche sur une carte géographique

**e) Recommandations:**
```python
total_2025 = df_future[df_future['Année'] == '2025']['Cas_Prévus'].sum()
total_2027 = df_future[df_future['Année'] == '2027']['Cas_Prévus'].sum()
st.success(f"La wilaya de {selected_w} devrait connaître une tendance à la {'hausse' if total_2027 > total_2025 else 'baisse progressive'}...")
```
- Compare 2025 et 2027 pour déterminer la tendance
- Fournit des recommandations basées sur les résultats

#### Objectif du fichier / الهدف من الملف
Application web complète qui fournit:
1. **Analyse interactive**: Affichage des données historiques de différentes manières
2. **Prédictions intelligentes**: Utilisation de l'apprentissage automatique pour prédire l'avenir
3. **Visualisations géographiques**: Cartes interactives pour afficher les données
4. **Interface utilisateur élégante**: Design professionnel et facile à utiliser

---

## ملخص التقنيات المستخدمة / Résumé des technologies utilisées

### المكتبات الرئيسية / Bibliothèques principales:
- **Streamlit**: Framework لتطبيقات الويب التفاعلية
- **Pandas**: معالجة البيانات
- **Plotly**: رسوم بيانية تفاعلية
- **Scikit-learn**: نماذج التعلم الآلي
- **NumPy**: الحسابات الرياضية

### الميزات الرئيسية / Fonctionnalités principales:
1. **تصور البيانات**: خرائط، رسوم بيانية، مقاييس
2. **تحليل تنبؤي**: نماذج تعلم آلي للتنبؤ
3. **واجهة تفاعلية**: اختيارات ديناميكية للسنوات والولايات
4. **تصميم احترافي**: CSS مخصص وواجهة مستخدم جميلة

---

## كيفية التشغيل / Comment exécuter

### للبيانات (projet_python.py):
```bash
python projet_python.py
```
ينشئ ملف `mauritania_wilayas_2018_2024.csv`

### للتطبيق (App.py):
```bash
streamlit run App.py
```
يفتح التطبيق في المتصفح على `http://localhost:8501`
