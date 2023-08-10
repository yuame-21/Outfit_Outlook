import requests  # import HTTP request library


# send a request for data of a location (london in this case)
# url = 'http://api.weactherapi.com/v1/forecast.json?key=7bbdace306904520a56214618232605&q=London&aqi=no'
# vision
# url = 'http://api.weatherapi.com/v1/forecast.json?key=7bbdace306904520a56214618232605&q=' + USER_INPUT + '&aqi=no'
# response = requests.get(url)

# API service class, not sure if we need but the idea is that it will handle communication
class APIService:
    def __init__(self, loc):
        self.location = loc

    # called by the view model to fetch data from API
    # adjust/clean the data from API to better serve our app
    def fetch_data(self):
        url = 'http://api.weatherapi.com/v1/forecast.json?key=7bbdace306904520a56214618232605&q=' + self.location + '&aqi=no'
        response = requests.get(url)
        return response

    def clean_data(self, response):
        # parse json response to a native python object
        response = response.json()

        # clean current
        condition_text = response["current"]["condition"]["text"]
        response["current"].pop("condition")
        response["current"]["condition"] = condition_text

        # clean forecast
        fore_day = response["forecast"]["forecastday"]

        fore_day = fore_day[0]

        day_avg = fore_day["day"]

        max_temp = day_avg["maxtemp_f"]
        min_temp = day_avg["mintemp_f"]
        avg_temp = day_avg["avgtemp_f"]
        daily_chance_of_rain = day_avg["daily_chance_of_rain"]

        response["forecast"]["max_temp"] = max_temp
        response["forecast"]["min_temp"] = min_temp
        response["forecast"]["avg_temp"] = avg_temp
        response["forecast"]["daily_chance_of_rain"] = daily_chance_of_rain

        hourly = fore_day["hour"]
        # hourly data starts at 00:00
        # edit hourly data to return a list for temp at every hour
        hour_forecast = []

        for hour in hourly:
            hour_forecast.append(hour['temp_f'])

        response["forecast"]["hourly_temp"] = hour_forecast

        # no need extra data
        response["forecast"].pop("forecastday")

        return response

