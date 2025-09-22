library(shiny)
library(plotly)
library(dplyr)

data(iris)
iris_df <- iris

plot_ly(
  iris_df,
  x = ~Sepal.Length,
  y = ~Sepal.Width,
  color = ~Species,
  type = "scatter",
  mode = "markers"
) %>%
  layout(
    title = "Scatter Plot: Sepal.Length vs Sepal.Width",
    xaxis = list(title = "Sepal.Length"),
    yaxis = list(title = "Sepal.Width")
  )

