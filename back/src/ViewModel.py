# thinking we use Model View ViewModel architecture?
# connects view and model and API stuff
import back.src.connect_API


class Liner:
    def __init__(self, loc):
        self.api_service = back.src.connect_API.APIService(loc)
        self.data = {}  # dynamically create an empty dictionary to store data

    # fetch all API data and store within a dictionary
    def fetch_data(self):
        response = self.api_service.fetch_data()
        if response.status_code == 200:
            # turn json into a giant dictionary and store in self.data
            self.data = response.json()
        else:
            print("request failed with status code:", response.status_code)

    # parse through data - key will be given as current, forecast, or location
    # get any data related to the current weather dictionary
    def parse_weather(self, key, q):
        d = self.data[key]
        try:
            return d[q]
        except KeyError:
            return "Incorrect key given"

# analyze it to determine clothing suggestions
# use sql to query a database of suggestions
