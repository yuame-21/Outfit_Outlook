# thinking we use Model View ViewModel architecture?
# connects view and model and API stuff
class ViewModel:
    def __init__(self, api_service):
        self.api_service = api_service
        self.data = []  # dynamically create an empty list to store data
        self.weath = 0;
        # fetch API data
        def fetch_data(self, user_input):
            response = self.api_service.fetch_data(user_input)
            if response.status_code == 200:
                self.data = response.json()["items"]
                # CHANGE THE VIEW
            else:
                print("request failed with status code:", response.status_code)

        # parse through data
        # get the weather
        def weather(self):
            w = parsed data
            self.weath = w

        # get the location
        def location(self):

        # analyze it to determine clothing suggestions
        # use sql to query a database of suggestions
