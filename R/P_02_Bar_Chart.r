library(shiny)
library(plotly)
library(dplyr)

data(iris)
iris_df <- iris

avg_iris <- iris_df %>% 
  group_by(Species) %>% 
  summarise(across(Sepal.Length:Petal.Width, mean))

plot_ly(avg_iris, x = ~Species, y = ~Sepal.Length, type = "bar", name = "Sepal.Length") %>%
  add_trace(y = ~Sepal.Width, name = "Sepal.Width") %>%
  layout(
    barmode = "group",
    title = "Média de Atributos por Espécie"
  )
