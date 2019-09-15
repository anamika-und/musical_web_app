# Imports
from flask import Flask

from src.config import DEBUG

# from musical.weather_service import WeatherService

# Creating a Flask app
app = Flask(__name__)


@app.route('/')
def music_app_homepage():
    pass


@app.route('/api/v1/musicians/data', methods=['GET'])
def music_app_get_musicians():
    pass


@app.route('/api/v1/instruments/no-musicians/data', methods=['GET'])
def music_app_get_instruments():
    pass


@app.route('/api/v1/musicians/multiple-instruments/data', methods=['GET'])
def music_app_get_multiple_instruments():
    pass


@app.route('/api/v1/instruments/multiple-musicians/data', methods=['GET'])
def music_app_get_multiple_musicians():
    pass


# Get setup so that if we call the app directly (and it isn't being imported elsewhere)
# it will then run the app with the debug mode as True
# More info - https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0')
