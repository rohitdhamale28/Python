setwd("D:/Training/Academy/R Course (C-DAC)/Datasets")
funds <- read.csv("Funds.csv", 
                  stringsAsFactors = T)
str(funds)
survey <- read.csv("survey.csv", 
                   stringsAsFactors = T)
str(survey)
diamonds <- read.csv2("Diamonds.csv", 
                      stringsAsFactors = T)
str(diamonds)
###############################################
library(readxl)
sales <- read_excel("Sales.xlsx",sheet = 1)
brupt <- read_excel("bankruptcy.xlsx", sheet = 3)


data(USArrests)
write.csv(USArrests, "USarr.csv")
#############################################

salaries <- read.csv("Salaries.csv", 
                     stringsAsFactors = T)
### Slicing of data frames
salaries[3,] # gets 3rd row
salaries[50,] # gets 50th row
salaries[,3] # gets 3rd column
salaries[2,3]
salaries[c(2,6,19,35,67,90),] # gets few rows
salaries[,c(3,2,5)] # gets few columns

### subsetting the data frames
hsal <- subset(salaries, 
               salary>100000 & rank=="AssocProf")
ss <- subset(salaries, 
               select = c(yrs.service, discipline))
ss <- subset(salaries,salary>100000 & rank=="AssocProf", 
             select = c(yrs.service, discipline))
