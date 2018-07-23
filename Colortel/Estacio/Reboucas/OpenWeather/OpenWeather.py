import requests
import json
import argparse
import sys, getopt
from datetime import datetime
#!/usr/bin/python
#
# Function to Get the Temperature of cityLocation
#
def GetTemp(cityLocation,jsonData):

                tempPosition = jsonData.find('"temp":') + 7
                pressPosition = jsonData.find('"pressure":') - 1
                tempValue = jsonData[tempPosition:pressPosition]
                return tempValue;
#
# Function to Get the Temperature of cityLocation
#
def GetHumi(cityLocation,jsonData):

                humiPosition = jsonData.find('"humidity":') + 11
                dtPosition = jsonData.find('"temp_min":') - 1
                humiValue = jsonData[humiPosition:dtPosition]
                return humiValue;
#
# Function to Get the Weather Condition of cityLocation
#
def GetCond(cityLocation,jsonData):

                condPosition = jsonData.find('"weather":[{"id":') + 29
                descriptionPosition = jsonData.find(',"description":') - 1
                condValue = jsonData[condPosition:descriptionPosition]
                return condValue;
#
# Get City Name from User
#
parser = argparse.ArgumentParser()
parser.add_argument("city")
args = parser.parse_args()
#
cityName = args.city
#
cityLocation = '"' + cityName + '"'
#
url = "http://api.openweathermap.org/data/2.5/weather"

querystring = {"q":"Rio de Janeiro","appid":"69bcbdf7127ff907e6109f3a17c63fe7","units":"metric"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "f2b6a459-21ef-9d69-1ca0-8e77a802f1a8"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)
jsonData = (response.text)
#
#print jsonData
#
tempValue = GetTemp(cityLocation,jsonData);
#print tempValue
humiValue = GetHumi(cityLocation,jsonData);
#print humiValue
condValue = GetCond(cityLocation,jsonData);
#print condValue
#
# Getting Local Date and Time
#
dateTime = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
#
print '{'+'"cityname":'+'"'+cityName+'"'+',"temp":'+'"'+tempValue+'"'+',"condition":'+'"'+condValue+'"'+',"humidity":'+'"'+ humiValue+'"'+','+ '"dateTime"'+":"+'"'+dateTime+'"'+ '}'


