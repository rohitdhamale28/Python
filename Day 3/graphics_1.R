setwd("D:/Training/Academy/R Course (C-DAC)/Datasets/")

a <- c(90,45,12,10)
barplot(a)
b <- c(89,23,45,19)
ab <- rbind(a,b)
barplot(ab)
barplot(ab,beside = T)
#########################
pie(a)
########################

survey <- read.csv("survey.csv", 
                   stringsAsFactors = T)
hist(survey$Age)
hist(survey$Pulse, col = "springgreen")
boxplot(survey$Pulse)
boxplot(survey$Pulse~survey$Exer)
##############################