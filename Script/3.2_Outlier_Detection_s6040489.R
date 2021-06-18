# install.packages("RPostgreSQL")
require("RPostgreSQL")

# create a connection
# save the password that we can "hide" it as best as we can by collapsing it
pw <- {
  "_s6040489_"
}

# loads the PostgreSQL driver
drv <- dbDriver("PostgreSQL")
# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
con <- dbConnect(drv, dbname = "c122",
                 host = "gip.itc.utwente.nl", port = 5434,
                 user = "s6040489", password = pw)
rm(pw) # removes the password

# check for the cartable
dbExistsTable(con, "aireas_data_eindhoven")
# TRUE

boxplot(dem$readingscalibratedPM1)$out
outliers = boxplot(dem$readingscalibratedPM1, plot =FALSE)$out
print(outliers)
dem[which(dem$readingscalibratedPM1 %in% outliers),]
dem = dem[-which(dem$readingscalibratedPM1 %in% outliers),]
boxplot(dem$readingscalibratedPM1)

outlierremoval = cbind(dem$readingscalibratedPM1)[-which(dem$readingscalibratedPM1>5*sd(dem$readingscalibratedPM1)), ]
boxplot(outlierremoval)

