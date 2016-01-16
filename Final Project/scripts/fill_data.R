getwd()
setwd("/Users/ka-pingwan/Desktop/datavismap")

install.packages("data.table")
library(data.table)
data <- fread("co2_emissions.csv")
names(data)[1] = "Country Name"
data <- as.data.frame(data)
data[,"V61"] <- NULL

countries <- c("AFG", "AGO", "ALB", "ARE", "ARG", "ARM", "ATA", "ATF", "AUS", "AUT", "AZE", "BDI", "BEL", "BEN", "BFA", "BGD", "BGR", "BHS", "BIH", "BLR", "BLZ", "BOL", "BRA", "BRN", "BTN", "BWA", "CAF", "CAN", "CHE", "CHL", "CHN", "CIV", "CMR", "COD", "COG", "COL", "CRI", "CUB", "-99", "CYP", "CZE", "DEU", "DJI", "DNK", "DOM", "DZA", "ECU", "EGY", "ERI", "ESP", "EST", "ETH", "FIN", "FJI", "FLK", "FRA", "GAB", "GBR", "GEO", "GHA", "GIN", "GMB", "GNB", "GNQ", "GRC", "GRL", "GTM", "GUY", "HND", "HRV", "HTI", "HUN", "IDN", "IND", "IRL", "IRN", "IRQ", "ISL", "ISR", "ITA", "JAM", "JOR", "JPN", "KAZ", "KEN", "KGZ", "KHM", "KOR", "-99", "KWT", "LAO", "LBN", "LBR", "LBY", "LKA", "LSO", "LTU", "LUX", "LVA", "MAR","MDA", "MDG", "MEX", "MKD", "MLI", "MMR", "MNE", "MNG", "MOZ", "MRT", "MWI", "MYS", "NAM", "NCL", "NER", "NGA", "NIC", "NLD", "NOR", "NPL", "NZL", "OMN", "PAK", "PAN", "PER", "PHL", "PNG", "POL", "PRI", "PRK", "PRT", "PRY", "QAT", "ROU", "RUS", "RWA", "-99", "SAU", "SDN", "SDS", "SEN", "SLB", "SLE", "SLV", "-99", "SOM", "SRB", "SUR", "SVK", "SVN", "SWE", "SWZ", "SYR", "TCD", "TGO", "THA", "TJK", "TKM", "TLS", "TTO", "TUN", "TUR", "TWN", "TZA", "UGA", "UKR", "URY", "USA", "UZB", "VEN", "VNM", "VUT", "PSE", "YEM", "ZAF", "ZMB", "ZWE")
all_countries <- data[,"Country Code"]
all_countries

indices <- which(all_countries %in% countries)

main_countires <- data[indices,]
main_countires_temp <- main_countires
main_countires_temp[main_countires_temp==""] <- NA
main_countires_temp[,"2012"] <- NULL
main_countires_temp[,"2013"] <- NULL
main_countires_temp[,"2014"] <- NULL
main_countires_temp[,"2015"] <- NULL
main_countires_temp <-  na.omit(main_countires_temp)

for (i in 1960:2011){
  main_countires_temp[,as.character(i)] <-  as.numeric(main_countires_temp[,as.character(i)])    
}

colmeans <- colMeans(main_countires_temp[,-c(1,2,3,4)])
colmeans["1960"]

main_countires[main_countires ==""] <- NA
na_position <- which(is.na(main_countires))

colmeans["1960"]

for (i in 1960:2011){
  #testje <- which(is.na(main_countires[,as.character(i)]))
  is.na(main_countires[,as.character(i)])
  testje
  #main_countires[testje,as.character(i)] <- colmeans[as.character(i)]
}

tempje <- main_countires[c("2012","2013","2014","2015")]
tempje <-  na.omit(tempje)

for (i in 2012:2015){
  tempje[,as.character(i)] <-  as.numeric(tempje[,as.character(i)])    
}

colmeans2 <- colMeans(tempje[,c("2012","2013","2014","2015")])

main_countires[is.na(main_countires)] <- 56038

write.csv(main_countires, file = "emission_data.csv",row.names=FALSE)

