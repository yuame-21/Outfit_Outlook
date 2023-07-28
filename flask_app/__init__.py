from flask import Flask
from flaskext.mysql import MySQL
from src.ViewModel import Liner
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

    @app.route('/weather/<locname>/<string:type>/<string:query>')
    def curr_weather(locname, type, query):
        # set up Viewmodel to retrieve data from API
        vm = Liner(locname)
        vm.fetch_data()

        if type == "current":
            return jsonify(vm.curr_weather(query))
        elif type == "forecast":
            return jsonify(vm.forecast(query))
        elif type == "location":
            return jsonify(vm.location(query))
        else:
            return "Error: No valid type provided"

    # register routes

    return app
