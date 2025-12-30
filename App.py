import streamlit as st
import pandas as pd
import plotly.express as px
import json
import numpy as np
from sklearn.linear_model import LinearRegression

# Configuration de la page
st.set_page_config(page_title="Prédiction Triennale Paludisme MRT", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #ddd; }
    h1 { color: #1e3d59; }
    .sidebar .sidebar-content { background-color: #2c3e50; }
    </style>
    """, unsafe_allow_html=True)


# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv('mauritania_wilayas_2018_2024.csv')
    with open('mrt_admin1.geojson', encoding='utf-8') as f:
        geojson = json.load(f)
    return df, geojson


df, mauri_geojson = load_data()

# Barre latérale
st.sidebar.title("🩺 Menu principal")
page = st.sidebar.radio("Aller à :", ["📊 Analyse historique", "🔮 Prédiction triennale (2025-2027)"])

selected_year = st.sidebar.selectbox("Choisir l’année :", sorted(df['Year'].unique(), reverse=True))
st.sidebar.markdown("---")
st.sidebar.markdown("### 🖋️ Préparé par :")
st.sidebar.info("**Yahya Sidna**\n\n**Aly Mohamed**")

# --- Première page : analyse historique ---
if page == "📊 Analyse historique":
    st.title("🦠 Tableau d’analyse de la propagation du paludisme (2018-2024)")
    # selected_year = st.sidebar.selectbox("Choisir l’année :", sorted(df['Year'].unique(), reverse=True))
    df_selected = df[df['Year'] == selected_year]

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Nombre total de cas", f"{df_selected['Cases'].sum():,}")
    with c2:
        st.metric("Wilaya la plus touchée", df_selected.groupby('Wilaya')['Cases'].sum().idxmax())
    with c3:
        st.metric("Année sélectionnée", selected_year)

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

    with col_right:
        wilaya_data = df_selected.groupby('Wilaya')['Cases'].sum().sort_values()
        st.plotly_chart(
            px.bar(wilaya_data, orientation='h', color_continuous_scale="Reds"),
            use_container_width=True
        )

    st.subheader(f"📈 Évolution mensuelle des cas en {selected_year}")
    monthly_trend = df_selected.groupby('Month')['Cases'].sum().reset_index()
    st.plotly_chart(
        px.line(monthly_trend, x='Month', y='Cases', markers=True),
        use_container_width=True
    )

# --- Deuxième page : prédiction pour les trois prochaines années (2025-2027) ---
else:
    st.title("🔮 Prédiction stratégique triennale (2025 - 2027)")
    st.info("Utilisation d’un modèle avancé de Machine Learning pour prédire la tendance générale de la maladie sur trois années à venir.")

    wilayas = df['Wilaya'].unique()
    selected_w = st.selectbox("Choisir une wilaya pour analyser son évolution future :", wilayas)

    # Préparation des données historiques pour l’entraînement
    df_w = df[df['Wilaya'] == selected_w].copy()
    df_w['Time_Index'] = (df_w['Year'] - 2018) * 12 + df_w['Month']

    model = LinearRegression().fit(df_w[['Time_Index']].values, df_w['Cases'].values)

    # Création d’un index temporel pour les 36 mois à venir (janvier 2025 → décembre 2027)
    # 2025 : Index 85–96 | 2026 : 97–108 | 2027 : 109–120
    future_indices = np.array([[i] for i in range(85, 121)])
    future_preds = model.predict(future_indices)

    df_future = pd.DataFrame({
        'Index': range(85, 121),
        'Mois': (list(range(1, 13)) * 3),
        'Année': (['2025'] * 12 + ['2026'] * 12 + ['2027'] * 12),
        'Cas_Prévus': np.maximum(0, future_preds).astype(int)
    })

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

    st.markdown("---")
    st.subheader("🗺️ Carte des prévisions géographiques futures")
    year_to_show = st.select_slider("Choisir l’année future à afficher :", options=["2025", "2026", "2027"])

    # Calcul du total prévisionnel par wilaya selon l’année choisie
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

    # Recommandation finale de Yahya et Aly
    total_2025 = df_future[df_future['Année'] == '2025']['Cas_Prévus'].sum()
    total_2027 = df_future[df_future['Année'] == '2027']['Cas_Prévus'].sum()

    st.success(f"""
    **📝 Rapport prospectif des chercheurs Yahya et Aly :**
    - La wilaya de **{selected_w}** devrait connaître une tendance à la **{'hausse' if total_2027 > total_2025 else 'baisse progressive'}** du nombre de cas d’ici 2027.
    - Recommandation : il est nécessaire de lancer un plan quinquennal fondé sur les prévisions numériques présentées ci-dessus afin d’assurer l’élimination totale des foyers épidémiques.
    """)