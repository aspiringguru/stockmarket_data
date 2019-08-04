import requests
import config
token = config.API_KEY
print("token:", token)

headers = {
        'Content-Type': 'application/json'
        }

requestResponse = requests.get("https://api.tiingo.com/api/test?token="+token,
                                    headers=headers)
print(requestResponse.json())

# works
