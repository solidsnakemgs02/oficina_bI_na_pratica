library(shiny)
library(plotly)
library(dplyr)

data(iris)
iris_df <- iris

ui <- fluidPage(
  titlePanel("🌸 Iris Dataset Dashboard"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("x_axis", "X-Axis", choices = colnames(iris_df)[1:4], selected = "Sepal.Length"),
      selectInput("y_axis", "Y-Axis", choices = colnames(iris_df)[1:4], selected = "Sepal.Width"),
      selectInput("hist_axis", "Histogram Attribute", choices = colnames(iris_df)[1:4], selected = "Sepal.Length")
    ),
    
    mainPanel(
      fluidRow(
        column(6, plotlyOutput("scatterPlot")),
        column(6, plotlyOutput("barPlot"))
      ),
      fluidRow(
        column(6, plotlyOutput("histPlot")),
        column(6, plotlyOutput("piePlot"))
      )
    )
  )
)

server <- function(input, output) {
  
  # Scatter
  output$scatterPlot <- renderPlotly({
    plot_ly(
      iris_df,
      x = ~get(input$x_axis),
      y = ~get(input$y_axis),
      color = ~Species,
      type = "scatter",
      mode = "markers"
    ) %>%
      layout(title = paste(input$x_axis, "vs", input$y_axis))
  })
  
  # Bar (média por espécie)
  avg_iris <- iris_df %>% group_by(Species) %>% summarise(across(Sepal.Length:Petal.Width, mean))
  output$barPlot <- renderPlotly({
    plot_ly(avg_iris, x = ~Species, y = ~get(input$x_axis), type = "bar", name = input$x_axis) %>%
      layout(title = paste("Média de", input$x_axis, "por espécie"))
  })
  
  # Histogram
  output$histPlot <- renderPlotly({
    plot_ly(
      iris_df,
      x = ~get(input$hist_axis),
      color = ~Species,
      type = "histogram",
      nbinsx = 15,
      opacity = 0.7
    ) %>%
      layout(title = paste("Distribuição de", input$hist_axis))
  })
  
  # Pie
  iris_cnt <- iris_df %>% group_by(Species) %>% summarise(Count = n())
  output$piePlot <- renderPlotly({
    plot_ly(
      iris_cnt,
      labels = ~Species,
      values = ~Count,
      type = "pie",
      hole = 0.4
    ) %>%
      layout(title = "Distribuição de amostras por espécie")
  })
  
}

shinyApp(ui, server)
