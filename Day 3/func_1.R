fah <- 100
cel <- (fah-32)*5/9
cel

fah_to_cel <- function(fh){
  cel <- (fh-32)*5/9
  cel
}
fah_to_cel(100)
############################################

fahToCel <- function(fah) {
  cel <- (fah-32)*5/9
  cel
}
#########################################
p <- 100000
n <- 5
r <- 8.9
calc_interest <- function(p, r, n) {
  ci <- p*(1+(r/100))**n - p
  ci
}
calc_interest(100000, 8.9, 5)
#######################################
mean_sd <- function(col_name) {
  avg <- mean(col_name, na.rm = T)
  sdev <- sd(col_name, na.rm = T)
  ans <- c(am = avg, std_dev = sdev)
  ans
}
mean_sd(survey$Pulse)
#######################################




















