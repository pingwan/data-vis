#### Create avaiable match list with match and tier ####

install.packages("data.table") 
library(data.table)
setwd("/Users/Ping/Desktop")   #Change this to the correct working directory
master_zone = fread("master-zones.csv")

X <- split(master_zone, master_zone$match)

temp  <- X[[1]]
temp  <- as.data.frame(temp)
names  <- temp[c("match","tier")][1,]

for (i in 2:length(X)){
  temp  <- X[[i]]
  temp  <- as.data.frame(temp)
  name  <- temp[c("match","tier")][1,]
  names  <- rbind(names,name)
}

names  <- as.data.frame(names)
write.table(x=names, file= "avaiable_matches.csv", sep=",", row.names=F)

#### Split the master_zone.csv for each match ####

for (i in 1:length(X)){
  temp  <- X[[i]]
  temp  <- as.data.frame(temp)
  name  <- temp[1,1]
  name  <- toString(name)
  write.csv(file= paste(name, ".csv", sep=""), x=temp, col.names=T)
}

#### Split the master_distance.csv for each match ###

master_distance = fread("master-distance.csv")

Y <- split(master_distance, master_distance$match)

for (i in 1:length(Y)){
  temp  <- Y[[i]]
  temp  <- as.data.frame(temp)
  name  <- temp[1,1]
  name  <- toString(name)
  write.csv(file= paste(name, ".csv", sep=""), x=temp, col.names=T)
}