import urllib, logging

from pip._vendor import requests

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/city')
def get_weather(city):
    api_key = "f2930ef51ab2bb7703d10298316a4efd"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + str(city)

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = x["weather"][0]["description"]

        # print following values

        # unsplash section get photo related to the weather description
        # access = "ldLo3U8Kn45vDQWNG_29eUidYZ6oUd_aTUyZtQpEp98"
        # baseurl = "https://api.unsplash.com/search/photos?query=?"
        # params = {'query': city_name, 'client_id': access}
        # routeURL = baseurl + urllib.parse.urlencode(params)
        #
        # request = urllib.request.Request(routeURL)
        # response = urllib.request.urlopen(request)
        # results = response.read()
        # urls = []
        # count = 0
        # for result in results['results']:
        #     urls.append(result['url']['small'])
        #     count += 1
        #     if count > 10:
        #         break
        #
        # print(urls)
        location = city.replace(' ', '+')
        description = weather_description.replace(' ', '+')
        # daily photos

        dailylocation = "https://source.unsplash.com/daily?" + location
        dailyweather = "https://source.unsplash.com/daily?" + description
        # weekly photos

        url = "https://source.unsplash.com/weekly?" + location
        weatherURL = "https://source.unsplash.com/weekly?" + description

        data = {'current_temperature': y["temp"], 'current_pressure': y["pressure"], 'current_humidity': y["humidity"],
                'weather_description': x["weather"][0]["description"],'dailylocation': dailylocation, 'dailyweather': dailyweather, 'url': url, 'weatherURL': weatherURL  }
        return data
    else:
        print(" City Not Found ")




# bing api
# def get_directions():
#     bingMapsKey = "AgHWyvUWjNBRoCQx_GTK2wS-veIshA1Kq-STZkgS6wcG4XlbPyFZqs76msTBw2J-"
#     longitude = input("Longitude: ")
#     latitude = input("Latitude: ")
#     destination = input("Address of destination: ")
#
#     encodedDest = urllib.parse.quote(destination, safe='')
#
#     routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + str(latitude) + "," + str(
#         longitude) + "&wp.1=" + encodedDest + "&key=" + bingMapsKey
#
#     request = urllib.request.Request(routeUrl)
#     response = urllib.request.urlopen(request)
#     print(response.read())


# @app.route('/')
# def index():
#     city = request.args.get('city')
#     get_weather(city)
#     return render_template('template.html',)

# two html docs
@app.route('/')
def index():
    return render_template('gresponse.html')


@app.route("/weatherdata")
def getdata():
    city = request.args.get('city')
    data = get_weather(city)
    app.logger.info(city)
    return render_template('weatherdata.html', city_name=city, current_temperature=data['current_temperature'], current_pressure=data['current_pressure'], current_humidity=data['current_humidity'], weather_description=data['weather_description'], dailylocation=data['dailylocation'], dailyweather=data['dailyweather'], url=data['url'], weatherURL=data['weatherURL'])


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
