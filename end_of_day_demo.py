'''
https://api.tiingo.com/documentation/end-of-day
'''

import requests
import config
token = config.API_KEY
print("token:", token)


headers = {
        'Content-Type': 'application/json',
        'Authorization' : 'Token '+token
        }

# Meta Data
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/TSLA",
                                    headers=headers)
print(requestResponse.json())

# Latest Price
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/TSLA/prices",
                                    headers=headers)
print(requestResponse.json())


# Historical Prices
# date format YYYY-MM-DD
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/TSLA/prices?startDate=2016-6-1&endDate=2016-7-1",
                                    headers=headers)
result = requestResponse.json()
type(result) #list
result[0].keys()

#works
