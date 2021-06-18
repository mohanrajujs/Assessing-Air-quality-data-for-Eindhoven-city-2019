# Assessing-Air-quality-data-for-Eindhoven-city-Netherlands-2019
#### PROBLEM AT HAND
The city of Eindhoven aims to become a healthy city and has implemented a system to monitor outdoor air quality and take measurements of air pollution. Air quality sensors are distributed over the city to collect data. Through this exercise, data will be analysed in order to answer questions like: 
- What is the quality of the air in the city currently? (PM10, PM2.5, PM1), ozone (O3), and nitrogen dioxide (NO2)
- How has this changed with time? 
- What is the rate of change of the air quality? Are patterns (temporal, spatial) detectable in the data? Could one perhaps point at causes of poor air quality levels?

#### DATA SOURCES
 - The AiREAS website has a locations map and offers near real-time measurements: http://www.aireas.com/
 - RIVM download data can be obtained via: https://www.luchtmeetnet.nl/download
 - KNMI (weather) data can be found at: http://projects.knmi.nl/klimatologie/uurgegevens/selectie.cgi

#### DATA PREPROCESSING
 - Acquiring : A python script was developed to extract all the data of 36 stations from the API URL in order to store them in a single, incremental .json format. At this stage, all the responses from the URL's (35 airboxes data) were stored in a single data frame.
 - Curation : Converted Epoch time to GMT time +0 & corrected the GPS information
 - Ingestion : Database was created usig POSTRESQL, schmea was created and finaly using ```ogr2ogr command``` the road network, .geojson file was successfully ingested to database.
  ```
This code uses Aireas API to retreive json data. Using For loop, 
the URL increments one number at each iteration and save json response in data frame. 
This is iterated over 35 airboxes and saves in a data frame.
"""
#Code - 01 
import csv #CSV Import
import json #JSon Import
import requests
import pandas as pd #Import Pandas

with open('output.csv', 'w') as f:
    csvfile = csv.writer(f)
    for i in range(1, 35):
		#Split URL and use i as incrementor
        url = 'http://data.aireas.com/api/v2/airboxes/history/' + str(i) + '/1451606400/1452816000' 
        data = requests.get(url=url)
        output = json.loads(data.content)
        output1 = pd.DataFrame(output)
        output1.to_csv("output.csv" , mode='a',  header=False)
   

#Converting String to Dictionary
def str_to_dict(output1):
    import re
    from collections import defaultdict
    d = defaultdict(int)
    for k, v in zip(re.findall('[A-Z]', outputt), re.findall('\d+', outputt)):
        d[k] += int(v)
    return d
	
#Code - 02 | Converting Epoch time to Human readable
from datetime import datetime
from tzlocal import get_localzone # $ pip install tzlocal

# get local timezone    
local_tz = get_localzone() 

print local_tz.localize(datetime(2012, 1, 15))
# -> 2012-01-15 00:00:00+04:00 # current utc offset
print local_tz.localize(datetime(2000, 1, 15))
# -> 2000-01-15 00:00:00+03:00 # past utc offset (note: +03 instead of +04)
print local_tz.localize(datetime(2000, 6, 15))
# -> 2000-06-15 00:00:00+04:00 # changes to utc offset due to DST

#Code - 03 | Transformation from EPSG 84 to 28996
from pyproj import Proj, transform

inProj = Proj(init='epsg:4326')
outProj = Proj(init='epsg:28992')
x1,y1 = read.csv("lat-long.csv")
x2,y2 = transform(inProj,outProj,x1,y1)
print x2,y2

 ```

#### DATA ANALYTICS (Descriptive Statistics, Regression and Spatial Data Quality)
 - Choice of Pollutant (PM10, PM2.5, PM1)
```
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

```
#### FURTHER IMPROVEMENTS ON THE CODE & METHODOLOGY
 - Above code is not end to end solution ,there are intermeidate steps that tends to complicate the process.
 - Combining the code by creating function and commanding the function whenever it is required.
 - Feeding output of one program as input to another program, thereby formulating a cascade of steps.
