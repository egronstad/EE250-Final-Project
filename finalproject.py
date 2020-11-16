import requests
import sys
import time

sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')
sys.path.append('../../Software/Python/')
sys.path.append('../../Software/Python/grove_rgb_lcd')
sys.path.append('../../Software/Python/grove_dht_pro_filter')

import grovepi
import grove_rgb_lcd as lcd
import grove_dht_pro_filter as dht

# Modules for my apps
import my_weather

PORT_BUTTON = 2
dht_pin = 4     # D4

LCD_LINE_LEN = 16

# Setup
grovepi.pinMode(PORT_TEMP_AND_HUM, "INPUT")
grovepi.pinMode(PORT_BUTTON, "INPUT")

lcd.setRGB(0, 128, 0)

# Installed Apps!
APPS = [
    my_weather.WEATHER_APP,
]

# Cache to store values so we save time and don't abuse the APIs
CACHE = [''] * len(APPS)
for i in range(len(APPS)):
    # Includes a two space offset so that the scrolling works better
    CACHE[i] = '  ' + APPS[i]['init']()

app = 0     # Active app
ind = 0     # Output index
ind2 = 0    # Other output index

while True:
    try:
        temperature, humidity = dht_sensor.feedMe()

        time.sleep(0.1)
        # Display app name
        lcd.setText_norefresh('Temp: ' + temperature + '\nHum: ' + humidity)
        
        # Scroll output
        lcd.setText_norefresh('\n' + CACHE[app][ind:ind+LCD_LINE_LEN])
        # TODO: Make the output scroll across the screen (should take 1-2 lines of code)
        ind+=1
        ind%=len(CACHE[app])

    except KeyboardInterrupt:
        # Gracefully shutdown on Ctrl-C
        lcd.setText('')
        lcd.setRGB(0, 0, 0)

        break

    except IOError as ioe:
        if str(ioe) == '121':
            # Retry after LCD error
            time.sleep(0.25)

        else:
            raise