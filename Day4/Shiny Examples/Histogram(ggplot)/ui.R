library(shiny)

data("iris")
pageWithSidebar(
  headerPanel = headerPanel("Histogram"),

  sidebarPanel = sidebarPanel(

    selectInput(inputId = "VarName",
                label = "Select Numeric Variable:",
                choices = list("Sepal.Length",
                                    "Sepal.Width",
                                    "Petal.Length",
                                    "Petal.Width")),
    sliderInput(inputId = "Bins",
                label = "No. of Bins",
                min = 2,max = nrow(iris),value = 6)
  ) ,
  mainPanel = mainPanel(
    plotOutput("histogram")
    #tableOutput("data")
  )
)