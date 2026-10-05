library(shiny)
library(DT)
data("mtcars")

function(input,output) {

  output$histogram <- renderPlot({

    hist(mtcars[,input$VarName],
         main = paste("Histogram of", input$VarName),
         col="pink")
  })

  output$boxplt <- renderPlot({
    boxplot(mtcars[,input$VarName],
            main=paste("Box Plot of", input$VarName))
  })

  output$dt <- renderDataTable({mtcars})
}