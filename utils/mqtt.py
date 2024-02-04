import machine
from ubinascii import hexlify
from umqtt.robust2 import MQTTClient
import json

with open('secrets.json') as f:
    secrets = json.load(f)['mqtt']

MACHINE_ID = hexlify(machine.unique_id()).decode('ascii')

# MQTT, password, unencrypted
client = MQTTClient(
    MACHINE_ID,
    secrets['host_ip'],
    port=secrets['port'],
    user=secrets['username'],
    password=secrets['password']
)


# print("A")
# x = client.connect()
# print("B")
# y = client.publish('test', 'Hello, world!')
# print("C")
# # print(client.ping())
# # client.disconnect()
# z = client.publish('test3', 'Hello, worldss!!')
# print("D")

# print(x)
# print(y)
# print(z)

# ind = 0
# while True:
#     client.publish('test', 'Hello, world! ' + str(ind))
#     ind += 1
#     utime.sleep(60)
# print(client.ping())