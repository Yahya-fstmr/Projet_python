# Explication du fichier App.py

## Vue d'ensemble
# Le fichier `App.py` est une application web interactive construite avec Streamlit pour afficher et analyser les données du paludisme en Mauritanie. Il fournit une interface utilisateur élégante avec des cartes géographiques, des graphiques et des analyses prédictives utilisant l'apprentissage automatique.

# ---

## Structure du code

### 1. Importation des bibliothèques (Lignes 1-7)

# ```python
import streamlit as st
import pandas as pd
import plotly.express as px
import json
import numpy as np
from sklearn.linear_model import LinearRegression
import base64
# ```

# **Explication:**
# - **streamlit (st)**: Framework Python pour créer des applications web interactives rapidement
# - **pandas (pd)**: Bibliothèque pour manipuler et analyser les données structurées (DataFrames)
# - **plotly.express (px)**: Bibliothèque pour créer des graphiques interactifs et des visualisations
# - **json**: Module standard pour lire et manipuler des fichiers JSON (notamment GeoJSON pour les cartes)
# - **numpy (np)**: Bibliothèque pour les calculs numériques et mathématiques
# - **sklearn.linear_model.LinearRegression**: Modèle de machine learning pour la régression linéaire (prédiction)
# - **base64**: Module standard pour encoder les images en base64 (pour les utiliser dans CSS)

# ---

### 2. Fonction de conversion d'image (Lignes 9-13)

# ```python
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
# ```

# **Explication:**
# - Cette fonction prend un fichier binaire (image) en paramètre
# - Lit le contenu du fichier en mode binaire (`'rb'`)
# - Encode l'image en base64 pour pouvoir l'intégrer directement dans du code HTML/CSS
# - Retourne la chaîne encodée qui sera utilisée comme arrière-plan

# ---

### 3. Configuration de l'image de fond (Lignes 18-23)

# ```python
try:
    bin_str = get_base64('image/image_1.jpg')
    sidebar_bg = f"url('data:image/jpg;base64,{bin_str}')"
except FileNotFoundError:
    sidebar_bg = "linear-gradient(#1e3a8a, #000000)" # Fallback color
# ```

# **Explication:**
# - Tente de charger l'image de fond pour la barre latérale
# - Si l'image existe, la convertit en base64 et crée une URL de données CSS
# - Si l'image n'existe pas (FileNotFoundError), utilise un dégradé bleu/noir comme solution de secours
# - Cela assure que l'application fonctionne même sans l'image

# ---

# ### 4. Personnalisation CSS (Lignes 25-66)

# ```python
st.markdown(f"""
    <style>
    /* 1. Style de la barre latérale (Sidebar) */
    [data-testid="stSidebar"] {{
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), {sidebar_bg};
        background-size: cover;
        background-position: center;
    }}

    /* 2. Fond de la page principale */
    [data-testid="stAppViewContainer"] {{
        background-color: #f8fafc !important;
    }}

    /* 3. Style des cartes de métriques */
    div[data-testid="stMetric"] {{
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        border-bottom: 4px solid #3b82f6;
    }}

    /* 4. Style du menu déroulant */
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
# ```

# **Explication:**
# - Utilise `st.markdown()` avec `unsafe_allow_html=True` pour injecter du CSS personnalisé
# - **Barre latérale**: Applique une image de fond avec un overlay sombre pour améliorer la lisibilité
# - **Page principale**: Définit un fond clair (#f8fafc) pour réduire l'éblouissement
# - **Cartes métriques**: Style avec bordure bleue, ombre et coins arrondis pour un look professionnel
# - **Menus déroulants**: Style blanc avec coins arrondis
# - **Texte sidebar**: Force la couleur blanche pour contraster avec le fond sombre
# - **Titres**: Bleu foncé (#1e40af) en gras

# ---
# ### 6. Configuration de la page (Ligne 89)

# ```python
st.set_page_config(page_title="Prédiction Triennale Paludisme MRT", layout="wide")
# ### 5. Fonction de chargement des données (Lignes 104-109)

# ```python
@st.cache_data
def load_data():
    df = pd.read_csv('mauritania_wilayas_2018_2024.csv')
    with open('mrt_admin1.geojson', encoding='utf-8') as f:
        geojson = json.load(f)
    return df, geojson
# ```

# **Explication:**
# - **@st.cache_data**: Décorateur Streamlit qui met en cache les données
#   - Évite de recharger les fichiers à chaque interaction utilisateur
#   - Améliore significativement les performances de l'application
# - **df**: Charge les données CSV contenant les cas de paludisme par wilaya, année et mois
# - **geojson**: Charge le fichier GeoJSON contenant les limites géographiques des wilayas
# - Retourne les deux pour utilisation dans l'application

# ---


# ```

# **Explication:**
# - Définit le titre de la page dans l'onglet du navigateur
# - `layout="wide"`: Utilise toute la largeur de l'écran pour un meilleur affichage

# ---

# ### 7. Barre latérale (Sidebar) - Lignes 115-121

# ```python
df, mauri_geojson = load_data()

st.sidebar.title("🩺 Menu principal")
page = st.sidebar.radio("Aller à :", ["📊 Analyse historique", "🔮 Prédiction triennale (2025-2027)"])
selected_year = st.sidebar.selectbox("Choisir l'année :", sorted(df['Year'].unique(), reverse=True))
st.sidebar.markdown("---")
st.sidebar.markdown("### 🖋️ Préparé par :")
st.sidebar.info("**Yahya Sidna**\n\n**Aly Mohamed**")
# ```

# **Explication:**
# - **Title**: Titre avec emoji médical dans la barre latérale
# - **radio**: Crée des boutons radio pour naviguer entre deux pages
#   - "Analyse historique": Page d'analyse des données passées
#   - "Prédiction triennale": Page de prédiction future
# - **selectbox**: Menu déroulant pour choisir l'année à analyser
#   - `sorted(..., reverse=True)`: Trie les années de la plus récente à la plus ancienne
# - **markdown("---")**: Ligne horizontale de séparation
# - **info**: Affiche une boîte d'information avec les noms des auteurs

# ---

# ### 8. Page 1: Analyse historique (Lignes 124-166)

# #### 8.1 Titre et filtrage des données

# ```python
if page == "📊 Analyse historique":
    st.title("🦠 Tableau d'analyse de la propagation du paludisme (2018-2024)")
    df_selected = df[df['Year'] == selected_year]
# ```

# **Explication:**
# - Affiche un titre avec emoji
# - Filtre le DataFrame pour ne garder que les données de l'année sélectionnée

# #### 8.2 Métriques principales (Lignes 129-135)

# ```python
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Nombre total de cas", f"{df_selected['Cases'].sum():,}")
    with c2:
        st.metric("Wilaya la plus touchée", df_selected.groupby('Wilaya')['Cases'].sum().idxmax())
    with c3:
        st.metric("Année sélectionnée", selected_year)
# ```

# **Explication:**
# - **st.columns(3)**: Crée 3 colonnes égales côte à côte
# - **c1**: Affiche le total des cas avec formatage numérique (virgules)
# - **c2**: Trouve la wilaya avec le plus de cas en groupant par wilaya et prenant l'index du maximum
# - **c3**: Affiche l'année sélectionnée

# #### 8.3 Carte géographique (Lignes 137-152)

# ```python
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
# ```

# **Explication:**
# - **columns([1.5, 1])**: Crée deux colonnes (la gauche 1.5 fois plus large que la droite)
# - **choropleth_mapbox**: Crée une carte choroplèthe (carte colorée selon les valeurs)
#   - `geojson`: Fichier contenant les formes géographiques des wilayas
#   - `locations='Wilaya'`: Colonne du DataFrame qui correspond aux régions
#   - `featureidkey`: Propriété dans le GeoJSON qui correspond aux noms des wilayas
#   - `color='Cases'`: Variable qui détermine la couleur
#   - `color_continuous_scale="Reds"`: Palette de couleurs rouges (plus sombre = plus de cas)
#   - `mapbox_style="carto-positron"`: Style de carte clair
#   - `zoom` et `center`: Niveau de zoom et position centrée sur la Mauritanie
# - **update_layout**: Supprime les marges pour un affichage plein écran
# - **st.plotly_chart**: Affiche la carte interactive

# #### 8.4 Graphique en barres (Lignes 154-159)

# ```python
    with col_right:
        wilaya_data = df_selected.groupby('Wilaya')['Cases'].sum().sort_values()
        st.plotly_chart(
            px.bar(wilaya_data, orientation='h', color_continuous_scale="Reds"),
            use_container_width=True
        )
# ```

# **Explication:**
# - **groupby('Wilaya')['Cases'].sum()**: Additionne les cas pour chaque wilaya
# - **sort_values()**: Trie par ordre croissant (les moins touchées en haut)
# - **px.bar(..., orientation='h')**: Crée un graphique en barres horizontal
# - Affiche dans la colonne de droite

# #### 8.5 Graphique linéaire mensuel (Lignes 161-166)

# ```python
    st.subheader(f"📈 Évolution mensuelle des cas en {selected_year}")
    monthly_trend = df_selected.groupby('Month')['Cases'].sum().reset_index()
    st.plotly_chart(
        px.line(monthly_trend, x='Month', y='Cases', markers=True),
        use_container_width=True
    )
# ```

# **Explication:**
# - **subheader**: Sous-titre avec emoji
# - **groupby('Month')['Cases'].sum()**: Additionne les cas pour chaque mois
# - **reset_index()**: Convertit le résultat en DataFrame normal (avec colonnes Month et Cases)
# - **px.line(..., markers=True)**: Crée un graphique linéaire avec des marqueurs sur chaque point
# - Montre l'évolution des cas au cours de l'année

# ---

# ### 9. Page 2: Prédiction triennale (Lignes 169-252)

# #### 9.1 Configuration de la page de prédiction

# ```python
# else:
#     st.title("🔮 Prédiction stratégique triennale (2025 - 2027)")
#     st.info("Utilisation d'un modèle avancé de Machine Learning pour prédire la tendance générale de la maladie sur trois années à venir.")

#     wilayas = df['Wilaya'].unique()
#     selected_w = st.selectbox("Choisir une wilaya pour analyser son évolution future :", wilayas)
# # ```

# # **Explication:**
# # - Le `else` correspond à la page "Prédiction triennale"
# # - Affiche un titre et un message d'information
# # - **unique()**: Récupère toutes les wilayas uniques du DataFrame
# # - **selectbox**: Permet à l'utilisateur de choisir une wilaya spécifique

# # #### 9.2 Préparation et entraînement du modèle (Lignes 176-180)

# # ```python
# # Préparation des données historiques pour l'entraînement
# df_w = df[df['Wilaya'] == selected_w].copy()
else:
    st.title("🔮 Prédiction stratégique triennale (2025 - 2027)")
    st.info("Utilisation d’un modèle avancé de Machine Learning pour prédire la tendance générale de la maladie sur trois années à venir.")

    wilayas = df['Wilaya'].unique()
    selected_w = st.selectbox("Choisir une wilaya pour analyser son évolution future :", wilayas)

     # # **Explication:**
 # - Le `else` correspond à la page "Prédiction triennale"
 # - Affiche un titre et un message d'information
 # - **unique()**: Récupère toutes les wilayas uniques du DataFrame
 # - **selectbox**: Permet à l'utilisateur de choisir une wilaya spécifique
  

    # Préparation des données historiques pour l’entraînement
    df_w = df[df['Wilaya'] == selected_w].copy()
    df_w['Time_Index'] = (df_w['Year'] - 2018) * 12 + df_w['Month']

    model = LinearRegression().fit(df_w[['Time_Index']].values, df_w['Cases'].values)
# ```

# **Explication:**
# - **df[df['Wilaya'] == selected_w]**: Filtre les données pour la wilaya sélectionnée
# - **copy()**: Crée une copie pour éviter les avertissements
# - **Time_Index**: Crée un index temporel continu
#   - Formule: `(Année - 2018) * 12 + Mois`
#   - Exemple: Janvier 2018 = (2018-2018)*12 + 1 = 1
#   - Exemple: Janvier 2019 = (2019-2018)*12 + 1 = 13
#   - Cela transforme le temps en nombre séquentiel pour le modèle
# - **LinearRegression().fit()**: Entraîne le modèle de régression linéaire
#   - `X`: Time_Index (variable indépendante)
#   - `y`: Cases (variable dépendante à prédire)

# #### 9.3 Prédiction pour les 36 prochains mois (Lignes 182-192)

# ```python
# Création d'un index temporel pour les 36 mois à venir (janvier 2025 → décembre 2027)
# 2025 : Index 85–96 | 2026 : 97–108 | 2027 : 109–120
    future_indices = np.array([[i] for i in range(85, 121)])
    future_preds = model.predict(future_indices)

    df_future = pd.DataFrame({
        'Index': range(85, 121),
        'Mois': (list(range(1, 13)) * 3),
        'Année': (['2025'] * 12 + ['2026'] * 12 + ['2027'] * 12),
        'Cas_Prévus': np.maximum(0, future_preds).astype(int)
    })
# ```

# **Explication:**
# - **future_indices**: Crée les indices temporels pour les 36 mois à venir (85 à 120)
#   - 85-96 = 12 mois de 2025
#   - 97-108 = 12 mois de 2026
#   - 109-120 = 12 mois de 2027
# - **model.predict()**: Utilise le modèle entraîné pour prédire les cas futurs
# - **df_future**: Crée un DataFrame avec les prédictions
#   - `Index`: Les indices temporels
#   - `Mois`: Liste [1,2,...,12] répétée 3 fois (pour 3 années)
#   - `Année`: Liste de strings ['2025','2025',...,'2027']
#   - `Cas_Prévus`: Les prédictions, avec `np.maximum(0, ...)` pour éviter les valeurs négatives
#   - `.astype(int)`: Convertit en nombres entiers

# #### 9.4 Graphique comparatif (Lignes 194-204)

# ```python
# Graphique comparatif des trois années
    fig_tri = px.line(
        df_future,
        x='Mois',
        y='Cas_Prévus',
        color='Année',
        markers=True,
        title=f"Comparaison des prévisions mensuelles pour la wilaya de {selected_w} (2025-2027)",
        labels={'Cas_Prévus': 'Cas prévus', 'Mois': 'Mois'}
    )
    st.plotly_chart(fig_tri, use_container_width=True)
# ```

# **Explication:**
# - **px.line(..., color='Année')**: Crée un graphique linéaire avec une ligne par année (3 lignes colorées)
# - Permet de comparer visuellement les prévisions entre 2025, 2026 et 2027
# - Montre l'évolution prévue au cours de chaque année et entre les années

# #### 9.5 Carte géographique des prévisions (Lignes 206-242)

# ```python
    st.markdown("---")
    st.subheader("🗺️ Carte des prévisions géographiques futures")
    year_to_show = st.select_slider("Choisir l'année future à afficher :", options=["2025", "2026", "2027"])

# Calcul du total prévisionnel par wilaya selon l'année choisie
    map_list = []
    for w in wilayas:
        df_tmp = df[df['Wilaya'] == w].copy()
        df_tmp['Time_Index'] = (df_tmp['Year'] - 2018) * 12 + df_tmp['Month']
        m_tmp = LinearRegression().fit(df_tmp[['Time_Index']].values, df_tmp['Cases'].values)

        if year_to_show == "2025":
            start_idx = 85
        elif year_to_show == "2026":
            start_idx = 97
        else:
            start_idx = 109

        year_total = m_tmp.predict(np.array([[i] for i in range(start_idx, start_idx + 12)])).sum()
        map_list.append({'Wilaya': w, 'Total_Prévu': int(max(0, year_total))})

    df_map_future = pd.DataFrame(map_list)

    fig_map_f = px.choropleth_mapbox(
        df_map_future,
        geojson=mauri_geojson,
        locations='Wilaya',
        featureidkey="properties.adm1_name",
        color='Total_Prévu',
        color_continuous_scale="YlOrRd",
        mapbox_style="carto-positron",
        zoom=4,
        center={"lat": 20.2, "lon": -12.7},
        opacity=0.8
    )
    fig_map_f.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig_map_f, use_container_width=True)
# ```

# **Explication:**
# - **select_slider**: Curseur pour choisir l'année à visualiser (2025, 2026 ou 2027)
# - **Boucle for**: Pour chaque wilaya:
#   1. Filtre les données de la wilaya
#   2. Crée le Time_Index
#   3. Entraîne un modèle de régression linéaire spécifique à cette wilaya
#   4. Détermine l'index de départ selon l'année choisie
#   5. Prédit les 12 mois de l'année et fait la somme
#   6. Ajoute le total prévu à la liste
# - **df_map_future**: DataFrame avec wilayas et totaux prévus
# - **choropleth_mapbox**: Carte colorée montrant les prévisions totales par wilaya
#   - `color_continuous_scale="YlOrRd"`: Palette jaune-orange-rouge (différente de la page historique)

# #### 9.6 Recommandations finales (Lignes 244-252)

# ```python
# Recommandation finale de Yahya et Aly
    total_2025 = df_future[df_future['Année'] == '2025']['Cas_Prévus'].sum()
    total_2027 = df_future[df_future['Année'] == '2027']['Cas_Prévus'].sum()

    st.success(f"""
    **📝 Rapport prospectif des chercheurs Yahya et Aly :**
    - La wilaya de **{selected_w}** devrait connaître une tendance à la **{'hausse' if total_2027 > total_2025 else 'baisse progressive'}** du nombre de cas d'ici 2027.
    - Recommandation : il est nécessaire de lancer un plan quinquennal fondé sur les prévisions numériques présentées ci-dessus afin d'assurer l'élimination totale des foyers épidémiques.
    """)



# ```

# **Explication:**
# - **Filtrage**: Calcule le total des cas prévus pour 2025 et 2027
# - **Comparaison**: Détermine si la tendance est à la hausse ou à la baisse
# - **st.success**: Affiche une boîte de message verte avec les recommandations
# - **Expression ternaire**: `{'hausse' if total_2027 > total_2025 else 'baisse progressive'}` affiche le mot approprié selon la tendance

# ---

# ## Résumé des fonctionnalités

# 1. **Analyse historique interactive**: Visualisation des données passées avec cartes, graphiques et métriques
# 2. **Prédiction par machine learning**: Utilisation de la régression linéaire pour prédire les cas futurs
# 3. **Visualisations géographiques**: Cartes interactives montrant la répartition spatiale des cas
# 4. **Interface utilisateur moderne**: Design personnalisé avec CSS et éléments interactifs
# 5. **Navigation intuitive**: Menu latéral avec deux pages principales

# ---

# ## Technologies utilisées

# - **Streamlit**: Framework d'application web
# - **Pandas**: Manipulation de données
# - **Plotly**: Graphiques interactifs
# - **Scikit-learn**: Machine learning (régression linéaire)
# - **NumPy**: Calculs numériques
# - **JSON**: Géodonnées (GeoJSON)

# ---

# ## Comment exécuter

# ```bash
# streamlit run App.py
# ```

# L'application s'ouvrira dans votre navigateur à l'adresse `http://localhost:8501`
