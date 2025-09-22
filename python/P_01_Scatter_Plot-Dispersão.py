import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_wine

# Carregar dataset
wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
wine_df["WineType"] = [wine.target_names[t] for t in wine.target]

st.title("🍷 Scatter Plot - Relação entre Ingredientes")

x_axis = st.selectbox("Selecione o eixo X", wine_df.columns[:-1], index=0)
y_axis = st.selectbox("Selecione o eixo Y", wine_df.columns[:-1], index=1)

fig = px.scatter(
    wine_df,
    x=x_axis,
    y=y_axis,
    color="WineType",
    opacity=0.8,
    title=f"{x_axis.capitalize()} vs {y_axis.capitalize()}"
)

st.plotly_chart(fig, use_container_width=True)
