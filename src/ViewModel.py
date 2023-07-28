# thinking we use Model View ViewModel architecture?
# connects view and model and API stuff
import src.connect_API


class Liner:
    def __init__(self, loc):
        self.api_service = src.connect_API.APIService(loc)
        self.data = {}  # dynamically create an empty dictionary to store data

    # fetch all API data and store within a dictionary
    def fetch_data(self):
        response = self.api_service.fetch_data()
        if response.status_code == 200:
            # turn json into a giant dictionary and store in self.data
            self.data = response.json()
        else:
            print("request failed with status code:", response.status_code)

    # parse through data
    # get any data related to the current weather dictionary
    def curr_weather(self, q):
        d = self.data["current"]
        return d[q]

    # Handles all calls to location based dictionary
    def location(self, q):
        d = self.data["location"]
        return d[q]

    # Handles all calls to forecast based dictionary
    def forecast(self, q):
        d = self.data["forecast"]
        return d[q]
# analyze it to determine clothing suggestions
# use sql to query a database of suggestions
