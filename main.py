import utils.wifi as wifi
from utils.mqtt import client, MACHINE_ID
import utils.sensors as sensors
import utime
import machine
import math


from machine import Pin
LED = Pin("LED", Pin.OUT)

def blink(times = 3, on = 0.1, off = None):
    if off is None:
        off = on
    for i in range(times):
        LED.value(1)
        utime.sleep(on)
        LED.value(0)
        utime.sleep(off)

def blink_index(ind):
    x = math.floor(math.log10(ind))
    blink(x)


def sos(dash = 1, dot = 0.2, gap = 0.2, space = 0.6):
    blink(3, dot, gap)
    utime.sleep(space)
    blink(3, dash, gap)
    utime.sleep(space)
    blink(3, dot, gap)


def setup():
    wifi.connect()
    client.connect()

def read_and_publish():
    readings = sensors.read_all_json()
    client.publish('sensors/air_quality/' + MACHINE_ID, readings)

def loop(cycle_time = 60):
    try:
        blink(3, 1, 0.1)
        setup()
        blink(3, 0.1, 0.1)
        ind = 0
        while True:
            read_and_publish()
            ind += 1
            blink(1, 0.1, 1)
            blink_index(ind)
            print(ind)
            utime.sleep(cycle_time)
    except Exception as e:
        print(e)
        for i in range(5):
            sos()
            utime.sleep(1)
        machine.reset()

loop(60)
