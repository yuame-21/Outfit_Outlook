import requests # import HTTP request libary

# send a request for data of a location (london in this case)
url = 'http://api.weatherapi.com/v1/current.json?key=7bbdace306904520a56214618232605&q=London&aqi=no'
response = requests.get(url)

# handle the response
if response.status_code == 200:
    data = response.json() # parse response as JSON
    # more stuff can go here to go through data
    print(data)
else:
    print("request failed with status code:", response.status_code)