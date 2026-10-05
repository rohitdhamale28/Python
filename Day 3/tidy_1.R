library(tidyverse)
setwd("D:/Training/Academy/R Course (C-DAC)/Datasets/")
cars2018 <- read.csv("cars2018.csv",
                     stringsAsFactors = T)
class(cars2018)
tbl_cars <- as_tibble(cars2018)
class(tbl_cars)
#########################################
survey <- read.csv("survey.csv", 
                   stringsAsFactors = T)
arr1 <- arrange(survey, Pulse )
arr2 <- arrange(survey, Sex, Pulse )
arr2 <- arrange(survey, Sex, desc(Pulse) )
#########################################
sel_1 <- select(survey, Fold, Clap, Smoke, Age)
sel_2 <- select(survey, 2:5)
sel_3 <- select(survey, Fold:Smoke)
sel_4 <- select(survey, starts_with("W"))
sel_5 <- select(survey, ends_with("nd"))
sel_6 <- select(survey, contains("d"))
#########################################
f_1 <- filter(survey, Age>30 & Sex=="Female")
#########################################
r_1 <- rename(survey,Exercise=Exer)
#######################################
## mutate() creates new variable
r_2 <- mutate(survey, r1=Pulse/Height)
##############################################
summarise(survey, avg_age=mean(Age, na.rm=T),
                  sd_age=sd(Age, na.rm = T))
summarise(survey, avg_age=mean(Age, na.rm=T),
                sd_age=sd(Age, na.rm = T),
                md_age=median(Age, na.rm = T))
##############################################
grp_df <- group_by(survey, Sex)
summarise(grp_df, avg_age=mean(Age, na.rm=T),
          sd_age=sd(Age, na.rm = T),
          md_age=median(Age, na.rm = T))
############################################
a <- read.csv("A.csv")
b <- read.csv("B.csv")
inner_join(a, b, by="IdNum")
left_join(a, b, by="IdNum")
right_join(a, b, by="IdNum")
full_join(a, b, by="IdNum")
###########################################
survey %>%
  group_by(Sex) %>%
  summarise(avg_age=mean(Age, na.rm=T),
            sd_age=sd(Age, na.rm = T),
            md_age=median(Age, na.rm = T))

survey |>
  group_by(Sex) |>
  summarise(avg_age=mean(Age, na.rm=T),
            sd_age=sd(Age, na.rm = T),
            md_age=median(Age, na.rm = T))

#################################
sw <- filter(survey, Sex=="Female") 
d <- select(sw, Exer, Pulse)
d_gy <- group_by(d, Exer)
g <- summarise(d_gy, avg_pulse=mean(Pulse, na.rm=T))
#or
h <- survey |> 
        filter(Sex=="Female") |> 
        select(Exer, Pulse) |> 
        group_by(Exer) |> 
        summarise(avg_pulse=mean(Pulse, na.rm=T))


