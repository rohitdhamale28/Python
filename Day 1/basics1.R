d = 90
class(d)
s = as.integer(d)
class(s)
a = as.character(d)
class(a)
#########################################

a.bgn = 44
########################################
b <- 45
# <- & -> are arrow operators
45 -> b
# alt -
########################################
b <- c(56, 89, 22, 50, 102)
class(b)
length(b)
b[3]
b[2:4]
0.5*b
a <- c(109, 201, 222, 450, 120)
a+b

d <- c(2,5,6)
a+d
#################################
b <- c(56, 89, 22, 50, 102)
a <- c(109, 201, 222, 450, 120)
ab <- rbind(a,b)
ab
ab <- cbind(a,b)
ab
class(ab)
## appending
h <- c(a,b)

# binding of unequal vectors
b <- c(56, 89, 22, 50, 102)
a <- c(109, 201, 222, 450)
ab <- rbind(a,b)
ab
######################################

v <- c(45, 9, "sf", 89)
class(v)
###################################
w <- c(52, 78, 12, 20, 90, 23)
w<50
w[w<50]
####################################
f <- list(p=45, q="FT", r=T, s=9.0)
f[2]
f$q
f <- list(p=45, q=c("FT","IO","IU"),
          r=T, s=list(a=9.0,b=89))
f[2]
f$q
f$s
class(f$r)
names(f)
###################################
# factor
s <- c("m", "f", "f", "m", "m", "f")
class(s)
fs <- factor(s)
class(fs)
fs
as.integer(fs)
# re-order
fs <- factor(s, levels = c("m", "f"))
fs
as.integer(fs)
#########################################
d <- NA
is.na(d)
v <- c(89, NA, 45, 90, NA)
is.na(v)
d+8
#############
b <- 0
a <- 0
s <- a/b
s
b <- 0
a <- 34
s <- a/b
s
is.finite(s)
is.infinite(s)
#####################################
m <- matrix(c(3,6,7,8,2,4), 3,2)
m
m <- matrix(c(3,6,7,8,2,4), 3,2, byrow = T)
m
m <- matrix(c(3,6,7), 3,2, byrow = F)
m
#####################################
a <- array(dim=4)
a[1] <- 2
a[2] <- 7
a

a <- array(c(3,5,6,7),dim=4)
a
####################################
a <- c("a","b","c","d")
b <- c(34, 90, 25, 12)
df <- data.frame(a,b)
df
dim(df)
colnames(df)
names(df)
###############################
# Resident datasets in R
data()
data(airquality)
data("airquality")
dim(airquality)
str(airquality) # meta data
