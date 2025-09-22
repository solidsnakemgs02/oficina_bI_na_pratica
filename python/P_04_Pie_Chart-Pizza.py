import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_wine

# Carregar dataset
wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
wine_df["WineType"] = [wine.target_names[t] for t in wine.target]

st.title("🍷 Pie Chart - Proporção de Amostras por Tipo de Vinho")

wine_cnt = (
    wine_df.groupby("WineType")
    .count()[["alcohol"]]
    .rename(columns={"alcohol": "Count"})
    .reset_index()
)

fig = px.pie(
    wine_cnt,
    names="WineType",
    values="Count",
    hole=0.4,
    title="Distribuição de Amostras por Tipo de Vinho"
)

st.plotly_chart(fig, use_container_width=True)
