setwd("D:/Training/Academy/R Course (C-DAC)/Datasets/")
library(tidyverse)
survey <- read.csv("survey.csv", 
                   stringsAsFactors = T)

ggplot(data = survey,
       aes(x=Height, y=Pulse,color = Exer))+
  geom_point()

ggplot(data = survey,
       aes(x=Height, y=Pulse,color = Exer))+
  geom_point()+
  facet_grid(Exer~.)


ggplot(data = survey,
       aes(x=Height, y=Pulse,color = Exer))+
  geom_point()+
  facet_grid(.~Exer)

ggplot(data = survey,
       aes(x=Height, y=Pulse,color = Exer))+
  geom_point()+
  facet_grid(Sex~Exer)+
  labs(title = "Pulse by Height and Exercise",
       color = "Exercise")
#####################################################
library(plotly)
p <- ggplot(data = survey,
       aes(x=Height, y=Pulse,color = Exer))+
  geom_point()
ggplotly(p)
#####################################################
p <- ggplot(data = survey, 
            aes(y=Height, x=Smoke,fill=Smoke))+
  geom_boxplot()
ggplotly(p)
####################################################
data(EuStockMarkets)
EuStockMarkets <- as.data.frame(EuStockMarkets)
EuStockMarkets$Time <- seq(1, nrow(EuStockMarkets))
p <- ggplot(data = EuStockMarkets,
            aes(x=Time, y=DAX))+
  geom_line()
ggplotly(p)
######
df <- EuStockMarkets |> 
        pivot_longer(cols = c(DAX, SMI, CAC, FTSE),
          names_to = "MarketIndex",
                     values_to = "Value")
p <- ggplot(data = df,
            aes(x=Time, y=Value, color = MarketIndex))+
  geom_line()
ggplotly(p)

####################################################
data("mtcars")
mtcars$gear <- factor(mtcars$gear)
ggplot(data = mtcars, 
       aes(x=disp, y=mpg, colour=gear))+
  geom_point()

