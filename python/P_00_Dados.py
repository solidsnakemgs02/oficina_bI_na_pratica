import streamlit as st

import pandas as pd

import cufflinks as cf

import warnings
warnings.filterwarnings("ignore")

#print("Streamlit Version : {}".format(st.__version__))

from sklearn.datasets import load_wine

wine = load_wine()

wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)

wine_df["WineType"] = [wine.target_names[t] for t in wine.target ]

print(wine_df.head())

#print(wine_df["WineType"].unique())