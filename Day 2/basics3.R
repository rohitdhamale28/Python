a <- 23000
if(a>25000)
  print("Fine") else
  print("Not Fine")
#or
if(a>25000){
  print("Fine")
} else {
  print("Not Fine")
}
#############################################
for(i in 1:5)
  print(i)
d <- c(3,6,7,9,1)
for( e in d ){
  print(e*e)
}
s <- 0
for( e in d ){
  s <- s + e
}
print(s)
################
s <- 0
i <- 1
while(i<=length(d)){
  s <- s + d[i]
  i <- i + 1
}
print(s)
###################################
b <- seq(2,10)
b
b <- seq(2,10,3)
b
b <- seq(10,2,-3)
b
