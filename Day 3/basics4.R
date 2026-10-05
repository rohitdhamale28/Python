setwd("D:/Training/Academy/R Course (C-DAC)/Datasets/")
cars2018 <- read.csv("cars2018.csv",
                     stringsAsFactors = T)
table(cars2018$Aspiration)
table(cars2018$Aspiration, cars2018$Transmission)
addmargins(table(cars2018$Aspiration, cars2018$Transmission))
#############################################################

marks <- c(23, 12, 18, 34, 29, 30, 10, 2)
ifelse(marks>=16, "Passes", "Fails")
############################################################
survey <- read.csv("survey.csv", 
                   stringsAsFactors = T)
sum(is.na(survey$Age))
sum(is.na(survey$Height))
mean(survey$Age)
mean(survey$Height, na.rm = T)
sd(survey$Height, na.rm = T)
summary(survey$Height)
summary(survey$Sex)
summary(survey)
################################################
attach(survey)
table(Smoke)
summary(Height)
################################################

