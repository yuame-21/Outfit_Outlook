from flask import Flask
from flaskext.mysql import MySQL
import ViewModel

# My SQL object to access db in other parts of code
db = MySQL()

def create_app():
    app = Flask(__name__)

    # secret key that will be used for securely signing the session
    # cookie and can be used for any other security related needs by
    # extensions or your application
    app.config['SECRET_KEY'] = 'D0ntS33Key'

    # set up database to store user data

    # set up Viewmodel to retrieve data from API
    vm = ViewModel()

    # routes
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/current/weather/<locname>')
    def curr_weather(locname):
        out = vm.curr_weather()

    # register routes

    return app