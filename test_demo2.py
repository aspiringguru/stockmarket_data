import requests
import config
token = config.API_KEY
print("token:", token)


headers = {
        'Content-Type': 'application/json',
        'Authorization' : 'Token '+token
        }
requestResponse = requests.get("https://api.tiingo.com/api/test/",
                                    headers=headers)
print(requestResponse.json())

#works
