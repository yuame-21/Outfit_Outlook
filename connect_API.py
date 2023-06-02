import requests  # import HTTP request library

'''
# send a request for data of a location (london in this case)
url = 'http://api.weatherapi.com/v1/current.json?key=7bbdace306904520a56214618232605&q=London&aqi=no'
# vision
# url = 'http://api.weatherapi.com/v1/current.json?key=7bbdace306904520a56214618232605&q=' + USER_INPUT + '&aqi=no'
response = requests.get(url)

# handle the response
if response.status_code == 200:  # 200 means success
    data = response.json()  # parse response as JSON
    # more stuff can go here to go through data
    print(data)
else:
    print("request failed with status code:", response.status_code)
'''

# API service class, not sure if we need but the idea is that it will handle communication
class APIService:
    # called by the view model to fetch data from API
    def fetch_data(self, user_input):
        # self.data = user input; not sure how it all connects yet
        url = 'http://api.weatherapi.com/v1/current.json?key=7bbdace306904520a56214618232605&q=' + user_input + '&aqi=no'
        response = requests.get(url)
        return response