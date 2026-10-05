library(shiny)
library(DT)
data("mtcars")
pageWithSidebar(
  headerPanel = headerPanel("Histogram"),

  sidebarPanel = sidebarPanel(

    selectInput(inputId = "VarName",#size = 5,selectize = F,
                label = "Select Numeric Variable:",
                choices = list("mpg",
                                   "disp", "hp",
                                   "drat", "wt","qsec","carb"))
  ) ,
  mainPanel = mainPanel(
    tabsetPanel(
      tabPanel("Histogram",plotOutput("histogram")),
      tabPanel("Box Plot",plotOutput("boxplt")),
      tabPanel("Data",dataTableOutput("dt"))

    )


  )
)