library(shiny)

data("mtcars")
pageWithSidebar(
  headerPanel = headerPanel("Scatter Plot"),
  
  sidebarPanel = sidebarPanel(
    
    selectInput(inputId = "VarX",
                label = "Select X-axis Variable:",
                choices = as.list(c("mpg",
                                   "disp", "hp", 
                                   "drat", "wt","qsec","carb"))),
    selectInput(inputId = "VarY",
                label = "Select Y-axis Variable:",
                choices = as.list(c("mpg",
                                    "disp", "hp", 
                                    "drat", "wt","qsec","carb"))),
    selectInput(inputId = "Color",
                label = "Select Colour Variable:",
                choices = as.list(c("am",
                                    "vs", "gear", 
                                    "cyl")))
  ) ,
  mainPanel = mainPanel(
  plotOutput("Scatter")
  )
)