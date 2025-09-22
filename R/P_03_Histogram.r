library(shiny)
library(plotly)
library(dplyr)

data(iris)
iris_df <- iris

plot_ly(
  iris_df,
  x = ~Sepal.Length,
  color = ~Species,
  type = "histogram",
  nbinsx = 15,
  opacity = 0.7
) %>%
  layout(
    title = "Distribuição de Sepal.Length por Espécie",
    xaxis = list(title = "Sepal.Length")
  )
