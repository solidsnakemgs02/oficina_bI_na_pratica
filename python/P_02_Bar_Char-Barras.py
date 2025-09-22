import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_wine

# Carregar dataset
wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
wine_df["WineType"] = [wine.target_names[t] for t in wine.target]

# Calcular média dos ingredientes por tipo
avg_wine_df = wine_df.groupby("WineType").mean().reset_index()

st.title("🍷 Bar Chart - Ingredientes Médios por Tipo de Vinho")

options = avg_wine_df.columns[1:]  # ignora WineType
selected = st.multiselect("Selecione os ingredientes", options, default=["alcohol", "malic_acid"])

if selected:
    fig = px.bar(
        avg_wine_df,
        x="WineType",
        y=selected,
        barmode="group",
        title="Média de Ingredientes por Tipo de Vinho"
    )
    st.plotly_chart(fig, use_container_width=True)
