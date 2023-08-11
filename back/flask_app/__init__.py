from flask import Flask
from flaskext.mysql import MySQL
from back.src.ViewModel import Liner
from flask import jsonify

# My SQL object to access db in other parts of code
db = MySQL()


def create_app():
    app = Flask(__name__)

    # secret key that will be used for securely signing the session
    # cookie and can be used for any other security related needs by
    # extensions or your application
    app.config['SECRET_KEY'] = 'D0ntS33Key'

    # set up database to store user data

    # routes
    @app.route('/')
    def hello():
        return 'Hello, World!'

    # locname can be with capitalized or not but real location, or longitude lat, or US/UK/Canadian post code
    # key : current, forecast, or location
    # query: multiple queries available depending on the key
    # location: name, region, country, lat, lon, tz_id, localtime
    # current: last_updated, temp_f, condition, precip_in, cloud, feelslike_f, and more
    # forecast: max_temp, min_temp, avg_temp, daily_chance_of_rain, hourly_temp
        # for forecast I removed the extra data we wouldn't use for ease of navigation
        # but if you want it I can re-work it and add whatever you want back in
    @app.route('/<string:locname>/<string:key>/<string:query>')
    def curr_weather(locname, key, query):
        # set up Viewmodel to retrieve data from API
        vm = Liner(locname)
        vm.fetch_data()

        if key == "current" or key == "forecast" or key == "location":
            return jsonify(vm.parse_weather(key, query))
        else:
            return "Error: No valid key provided"

    return app
