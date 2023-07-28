import requests  # import HTTP request library


# send a request for data of a location (london in this case)
# url = 'http://api.weatherapi.com/v1/forecast.json?key=7bbdace306904520a56214618232605&q=London&aqi=no'
# vision
# url = 'http://api.weatherapi.com/v1/forecast.json?key=7bbdace306904520a56214618232605&q=' + USER_INPUT + '&aqi=no'
# response = requests.get(url)

# API service class, not sure if we need but the idea is that it will handle communication
class APIService:
    def __init__(self, loc):
        self.location = loc

    # called by the view model to fetch data from API
    def fetch_data(self):
        url = 'http://api.weatherapi.com/v1/forecast.json?key=7bbdace306904520a56214618232605&q=' + self.location + '&aqi=no'
        response = requests.get(url)
        return response
