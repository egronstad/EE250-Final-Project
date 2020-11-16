import requests
import json

# OpenWeatherMap API: https://openweathermap.org/current

# TODO: Sign up for an API key
OWM_API_KEY = '0a9b4699a053ea77dd1fab6e7d062612'  # OpenWeatherMap API Key

DEFAULT_ZIP = 90089

def get_weather(zip_code):
    zip_and_country = zip_code, 'us'
    params = {
        'appid': OWM_API_KEY,
        # TODO: referencing the API documentation, add the missing parameters for zip code and units (Fahrenheit)
        'zip': zip_and_country,
        'units': 'imperial'
    }

    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params)

    if response.status_code == 200: # Status: OK
        data = response.json()

        # TODO: Extract the temperature & humidity from data, and return as a tuple
        main = data['main']
        take_temp = main['temp']
        take_hum = main['humidity']
        return take_temp, take_hum

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return 0.0, 0.0

def weather_init():
    zip_code = DEFAULT_ZIP
    temp, hum = get_weather(zip_code)
    
    output = '{:.1f}F, {:>.0f}% humidity'.format(temp, hum)
    print('weather for {}: {}'.format(zip_code, output))

    return output


WEATHER_APP = {
    'name': 'Weather',
    'init': weather_init
}


if __name__ == '__main__':
    weather_init()
