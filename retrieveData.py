import requests
import pandas as pd
import csv


#sid = SentimentIntensityAnalyzer()

## One way to retrieve data https://api.tiingo.com/documentation/end-of-day
## Useful for looking at specific dates
## Only returns data for that timeperiod 

headers = {
    'Content-Type': 'application/json'
}
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/F/prices?startDate=1999-01-04&endDate=1999-01-07&token=95ce701a2c7696170cf649554ae5996cbca13380", headers=headers)



#print(requestResponse.json())
with open('output.csv','wb') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    wr.writerows(requestResponse.json())

print(type(requestResponse.json()))
print(type(requestResponse))


## Another way to retrieve data https://www.alphavantage.co/documentation/#daily
## Useful for data that is within 20 years
## However returns all of the data
'''
headers = {
    'Content-Type': 'application/json'
}
requestResponse = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=BRDCY&outputsize=full&apikey=5H639V1HLLHKXM60"
, headers=headers)
print(requestResponse.json())
'''
