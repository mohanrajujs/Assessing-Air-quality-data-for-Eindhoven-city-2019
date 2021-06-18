"""
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
