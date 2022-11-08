import time
import board
from adafruit_apds9960.apds9960 import APDS9960
import busio

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/AnjaliProximityTest'

i2c = busio.I2C(board.SCL, board.SDA)
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True


while True:
    gesture = apds.gesture()

    if gesture == 0x01:
        print("up")
        client.publish(topic, "up")
    elif gesture == 0x02:
        print("down")
        client.publish(topic, "down")
    elif gesture == 0x03:
        print("left")
        client.publish(topic, "left")
    elif gesture == 0x04:
        print("right")
        client.publish(topic, "right")
