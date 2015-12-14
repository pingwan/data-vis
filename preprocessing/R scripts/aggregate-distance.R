setwd("/Users/Ping/Desktop/data-visualisation/preprocessing/master_distance")
install.packages("data.table")
library(data.table)
temp = list.files(pattern="*.csv")
myfiles = do.call(rbind, lapply(temp, function(x) read.csv(x, stringsAsFactors = FALSE)))
myfiles = as.data.table(myfiles)
myfiles$Win.Lose = as.factor(myfiles$Win.Lose)
winners = subset(myfiles, myfiles$Win.Lose == "Win")
losers = subset(myfiles, myfiles$Win.Lose == "Lose")
winners_aggregate = winners[,mean(DD),by="tsync"]
losers_aggregate = losers[,mean(DD),by="tsync"]
winners_aggregate$type = "win"
losers_aggregate$type = "lose"
aggregate = rbind(winners_aggregate, losers_aggregate)
names(aggregate) = c("tsync","DD","type")
write.csv(aggregate, file = "aggregate.csv")