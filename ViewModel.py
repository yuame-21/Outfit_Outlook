# thinking we use Model View ViewModel architecture?
# connects view and model and API stuff


class ViewModel:
    def __init__(self, api_service):
        self.api_service = api_service
        self.data = []  # dynamically create an empty list to store data
        self.weath = 0;

    # fetch all API data and store within a dictionary
    def fetch_data(self, user_input):
        response = self.api_service.fetch_data(user_input)
        if response.status_code == 200:
            # turn json into a giant dictionary and store in self.data
            self.data = response.json()
        else:
            print("request failed with status code:", response.status_code)

    # parse through data
    # get the current weather in F
    def curr_weather(self):
        print(self.data["current"]["temp_f"])

    # get the location
    def location(self):
        print(self.data["location"]["name"] + self.data["location"]["country"])

# analyze it to determine clothing suggestions
# use sql to query a database of suggestions
