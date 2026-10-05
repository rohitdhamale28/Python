library(shiny)
library(ggplot2)
data("mtcars")
function(input,output) {

  output$Scatter <- renderPlot({
    ss <- mtcars[,c(input$VarX,input$VarY,input$Color) ]
    ss[,3] <- as.factor(ss[,3])
    ggplot(data = ss, aes(x=ss[,1],y=ss[,2],color=ss[,3]))+
      geom_point()+labs(color=input$Color)

  })


}