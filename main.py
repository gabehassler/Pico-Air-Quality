import utils.wifi as wifi
from utils.mqtt import client, MACHINE_ID
import utils.sensors as sensors
import utime

wifi.connect()
client.connect()


while True:
    readings = sensors.read_all_json()
    client.publish('sensors/air_quality', readings)
    utime.sleep(60)

