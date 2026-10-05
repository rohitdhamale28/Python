library(shiny)

data("iris")
library(ggplot2)
function(input,output) {

  output$histogram <- renderPlot({

    # hist(iris[,input$VarName],
    #      main = paste("Histogram of", input$VarName),
    #      col="violetred2"  )
  ggplot(data = iris,aes(x=iris[,input$VarName]))+
           geom_histogram(bins = input$Bins  ,fill="lightblue2",
                          color="darkblue")+
      labs(x=input$VarName)
  })


}