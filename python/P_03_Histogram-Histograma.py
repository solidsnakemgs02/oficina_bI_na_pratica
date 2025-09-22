import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_wine

# Carregar dataset
wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
wine_df["WineType"] = [wine.target_names[t] for t in wine.target]

st.title("🍷 Histogram - Distribuição dos Ingredientes")

ingredient = st.selectbox("Selecione o ingrediente", wine_df.columns[:-1], index=0)
bins = st.slider("Número de bins", min_value=5, max_value=50, value=20, step=5)

fig = px.histogram(
    wine_df,
    x=ingredient,
    color="WineType",
    nbins=bins,
    opacity=0.7,
    title=f"Distribuição de {ingredient.capitalize()}"
)

st.plotly_chart(fig, use_container_width=True)
