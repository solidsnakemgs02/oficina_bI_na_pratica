library(shiny)
library(plotly)
library(dplyr)

#Carrega conjunto de dados Iris
data(iris)
iris_df <- iris

head(iris_df)
summary(iris_df)

#write.csv(iris, "E:/Alex/2025/UCB/Semana de TI/BI na Prática/Oficina_BI_na_Prática/R/iris.csv", row.names = FALSE)
