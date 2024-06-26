import requests
import configparser
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def weather_dashboard():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def render_results():
    zip_code = request.form['zipCode']
    IN = "IN"
    api_key = "1c8868e06a9af40a82a56e23b9046d87"
    data = get_weather_results(zip_code, IN,api_key)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('results.html',
                           location=location, temp=temp,
                           feels_like=feels_like, weather=weather)
#def get_api_key():
    #config = configparser.ConfigParser()
    #config.read('config.ini')
    #return config['openweathermap']['1c8868e06a9af40a82a56e23b9046d87']


def get_weather_results(zip_code,country_code, api_key):
    api_url = "http://api.openweathermap.org/" \
              "data/2.5/weather?zip={},{}&units=imperial&appid={}".format(zip_code,country_code, api_key)
    r = requests.get(api_url)
    return r.json()


if __name__ == '__main__':
    app.run()
