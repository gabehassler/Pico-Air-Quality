import network
from time import sleep

# read 'secrets.json' file

import json
with open('secrets.json') as f:
    secrets = json.load(f)['wifi']





def connect(max_attempts=10):
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets['ssid'], secrets['password'])
    attempts = 1
    while wlan.isconnected() == False and attempts < max_attempts:
        print('Connecting to network... attempt', attempts)
        attempts += 1
        sleep(1)
    print("Connected to WiFi")


connect()

