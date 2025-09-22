import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_wine
import warnings

warnings.filterwarnings("ignore")

####### Load Dataset #####################
wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
wine_df["WineType"] = [wine.target_names[t] for t in wine.target]

st.set_page_config(layout="wide")
st.markdown("## 🍷 Wine Dataset Analysis")

################# Scatter Chart Logic #################
st.sidebar.markdown("### 📊 Scatter Chart: Explore Relationship Between Ingredients:")

ingredients = wine_df.drop(labels=["WineType"], axis=1).columns.tolist()

x_axis = st.sidebar.selectbox("X-Axis", ingredients)
y_axis = st.sidebar.selectbox("Y-Axis", ingredients, index=1)

if x_axis and y_axis:
    scatter_fig = px.scatter(
        wine_df,
        x=x_axis,
        y=y_axis,
        color="WineType",
        opacity=0.8,
        title=f"{x_axis.replace('_',' ').capitalize()} vs {y_axis.replace('_',' ').capitalize()}",
        labels={x_axis: x_axis.replace("_", " ").capitalize(), y_axis: y_axis.replace("_", " ").capitalize()}
    )
else:
    scatter_fig = None

########## Bar Chart Logic ##################
st.sidebar.markdown("### 📊 Bar Chart: Average Ingredients Per Wine Type:")

avg_wine_df = wine_df.groupby(by=["WineType"]).mean().reset_index()

bar_axis = st.sidebar.multiselect(
    label="Bar Chart Ingredient",
    options=avg_wine_df.columns.tolist()[1:],  # exclui WineType
    default=["alcohol", "malic_acid"]
)

if bar_axis:
    bar_fig = px.bar(
        avg_wine_df,
        x="WineType",
        y=bar_axis,
        barmode="group",
        title="Distribution of Average Ingredients Per Wine Type"
    )
else:
    bar_fig = px.bar(
        avg_wine_df,
        x="WineType",
        y="alcohol",
        title="Distribution of Average Alcohol Per Wine Type"
    )

################# Histogram Logic ########################
st.sidebar.markdown("### 📊 Histogram: Explore Distribution of Ingredients:")

hist_axis = st.sidebar.multiselect(label="Histogram Ingredient", options=ingredients, default=["malic_acid"])
bins = st.sidebar.radio(label="Bins :", options=[10, 20, 30, 40, 50], index=1)

if hist_axis:
    hist_fig = px.histogram(
        wine_df,
        x=hist_axis[0],  # só plota 1 ingrediente por vez
        color="WineType",
        nbins=bins,
        opacity=0.7,
        title=f"Distribution of {hist_axis[0].replace('_',' ').capitalize()}"
    )
else:
    hist_fig = px.histogram(
        wine_df,
        x="alcohol",
        color="WineType",
        nbins=bins,
        opacity=0.7,
        title="Distribution of Alcohol"
    )

#################### Pie Chart Logic ##################################
wine_cnt = wine_df.groupby(by=["WineType"]).count()[['alcohol']].rename(columns={"alcohol":"Count"}).reset_index()

pie_fig = px.pie(
    wine_cnt,
    names="WineType",
    values="Count",
    hole=0.4,
    title="Wine Samples Distribution Per WineType"
)

##################### Layout Application ##################
container1 = st.container()
col1, col2 = st.columns(2)

with container1:
    with col1:
        if scatter_fig:
            st.plotly_chart(scatter_fig, use_container_width=True)
    with col2:
        st.plotly_chart(bar_fig, use_container_width=True)

container2 = st.container()
col3, col4 = st.columns(2)

with container2:
    with col3:
        st.plotly_chart(hist_fig, use_container_width=True)
    with col4:
        st.plotly_chart(pie_fig, use_container_width=True)
