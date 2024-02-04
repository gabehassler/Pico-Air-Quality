import time
import board
import busio
import adafruit_bme680
import adafruit_scd30
from adafruit_pm25.i2c import PM25_I2C
import json

class Measurement:
    def __init__(self, name, sensor, unit, value):
      self.name = name
      self.sensor = sensor
      self.unit = unit
      self.value = value


    def __repr__(self):
        return f"{self.name}: {self.value} {self.unit}"

    def __str__(self):
        return f"{self.name}: {self.value} {self.unit}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "sensor": self.sensor,
            "unit": self.unit,
            "value": self.value
        }



def read_all_json():
    measurements = read_all()
    return json.dumps([m.to_dict() for m in measurements])

    

def read_bme680():
    return [Measurement("Temperature", "BME680", "C", BME680.temperature),
            Measurement("Relative Humidity", "BME680", "%", BME680.relative_humidity), 
            Measurement("Pressure", "BME680", "hPa", BME680.pressure), 
            Measurement("Gas", "BME680", "ohm", BME680.gas)]

def read_scd30():
    return [Measurement("Temperature", "SCD30", "C", SCD30.temperature),
            Measurement("Relative Humidity", "SCD30", "%", SCD30.relative_humidity), 
            Measurement("CO2", "SCD30", "PPM", SCD30.CO2)]

def read_pm25():
   aqdata = PM25.read()
   return [
        Measurement("PM 1.0 Standard", "PM25", "ug/m3", aqdata["pm10 standard"]),
        Measurement("PM 2.5 Standard", "PM25", "ug/m3", aqdata["pm25 standard"]), 
        Measurement("PM 10 Standard", "PM25", "ug/m3", aqdata["pm100 standard"]),
        Measurement("PM 1.0 Environmental", "PM25", "ug/m3", aqdata["pm10 env"]),
        Measurement("PM 2.5 Environmental", "PM25", "ug/m3", aqdata["pm25 env"]),
        Measurement("PM 10 Environmental", "PM25", "ug/m3", aqdata["pm100 env"]),
        Measurement("Particles > 0.3um / 0.1L air", "PM25", "count", aqdata["particles 03um"]),
        Measurement("Particles > 0.5um / 0.1L air", "PM25", "count", aqdata["particles 05um"]),
        Measurement("Particles > 1.0um / 0.1L air", "PM25", "count", aqdata["particles 10um"]),
        Measurement("Particles > 2.5um / 0.1L air", "PM25", "count", aqdata["particles 25um"]),
        Measurement("Particles > 5.0um / 0.1L air", "PM25", "count", aqdata["particles 50um"]),
        Measurement("Particles > 10 um / 0.1L air", "PM25", "count", aqdata["particles 100um"])
    ]

# SENSORS = ["BME680", "SCD30", "PM25"]

# def read_sensor(sensor):
#     if sensor == "BME680":
#         return read_bme680()
#     elif sensor == "SCD30":
#         return read_scd30()
#     elif sensor == "PM25":
#         return read_pm25()
#     else:
#         raise ValueError(f"Unknown sensor: {sensor}")

def read_all(): 
    return read_bme680() + read_scd30() + read_pm25()

def print_all():
    for m in read_all():
        print(str(m))

def test_sensors():
    while True:
        print("Testing sensors...")
        print_all()
        time.sleep(5)
   

i2c = busio.I2C(board.GP17, board.GP16)

# VOC sensor
BME680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
BME680.sea_level_pressure = 1013.25

# CO2 sensor
SCD30 = adafruit_scd30.SCD30(i2c)

# PM sensor
PM25 = PM25_I2C(i2c, None)
