library(shiny)
library(plotly)
library(dplyr)

data(iris)
iris_df <- iris

iris_cnt <- iris_df %>% 
  group_by(Species) %>% 
  summarise(Count = n())

plot_ly(
  iris_cnt,
  labels = ~Species,
  values = ~Count,
  type = "pie",
  hole = 0.4
) %>%
  layout(
    title = "Proporção de Amostras por Espécie"
  )

