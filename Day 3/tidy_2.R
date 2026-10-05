library(tidyverse)

table4a
table4a %>% gather(`1999`, `2000`, key= "year",
                   value= "cases")
table4a %>% gather(-country, key= "year",
                   value= "cases")
#or
table4a |> pivot_longer(cols = c(`1999`, `2000`), 
                        names_to = "year", 
                        values_to = "cases")
##################################################
table2
table2 %>% spread(key = "type", value = "count")
#or
table2 |> pivot_wider(names_from = "type",
                      values_from = "count")
#################################################
table3
table3 |> 
  separate(rate, into = c("cases", "population"))
#################################################
table5
table5 |> unite(new,century, year, sep = "" )

table5 |> unite(new,century, year)


