setwd("D:/Training/Academy/R Course (C-DAC)/Datasets/")
library(tidyverse)
survey <- read.csv("survey.csv", 
                   stringsAsFactors = T)

ggplot(data = survey,aes(x=Age, y=Pulse))+
  geom_point()
ggplot(data = survey,aes(x=Age, y=Pulse))+
  geom_point(colour = "blue")
ggplot(data = survey,
       aes(x=Age, y=Pulse,color = Sex))+
  geom_point()

ggplot(data = survey,
       aes(x=Height,y=Pulse,shape = Smoke))+
  geom_point()

ggplot(data = survey,
       aes(x=Height,y=Pulse,color=Exer,
           shape = Smoke))+
  geom_point()

# Regression Line
ggplot(data = survey,aes(x=Height, y=Pulse))+
  geom_point()+
  geom_smooth(method = "lm")
########################################
ggplot(data = survey, aes(x=Pulse))+
  geom_histogram(fill = "springgreen",
                 colour = "darkgreen",
                 bins = 10)
########################################

ggplot(data = survey, aes(y=Height))+
  geom_boxplot()
ggplot(data = survey, aes(y=Height, x=Smoke))+
  geom_boxplot()
ggplot(data = survey, aes(y=Height, fill=Smoke))+
  geom_boxplot()
ggplot(data = survey, aes(y=Height, color=Smoke))+
  geom_boxplot()
#############################################
# graph for analyzing probability distribution
# of a numerical variable
ggplot(data = survey, aes(x=Pulse))+
  geom_density(fill = "springgreen",
                 colour = "darkgreen")
#############################################
ggplot(data = survey, aes(x=Exer, fill=Exer))+
  geom_bar()
ggplot(data = survey, aes(y=Exer, fill=Exer))+
  geom_bar()
ggplot(data = survey, aes(x=Exer, fill=Smoke))+
  geom_bar(position = 'dodge')
# bar plots by default plot the counts
###############################################
means_age <- survey |> 
             group_by(Exer) |> 
             summarise(avg=mean(Age,na.rm=T))
ggplot(data = means_age, 
       aes(x=Exer, y=avg, fill=Exer))+
  geom_bar(stat = 'identity')


