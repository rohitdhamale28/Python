library(tidyverse)
setwd("D:/Training/Academy/R Course (C-DAC)/Datasets/")

survey |> 
  select(Exer,Smoke, Age) |> 
  drop_na() |> 
  group_by(Exer,Smoke) |> 
  summarise(avg_age=mean(Age, na.rm = TRUE),
            .groups = "drop_last") |> 
  pivot_wider(names_from = Exer, values_from = avg_age)
