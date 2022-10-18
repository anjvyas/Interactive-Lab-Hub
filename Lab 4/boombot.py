# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import os

from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True

# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE

while True:
    gesture = apds.gesture()

    if gesture == 0x01:
        print("up")
        os.system("aplay G.wav")
    elif gesture == 0x02:
        print("down")
        os.system("aplay D_sharp.wav")
    elif gesture == 0x03:
        print("left")
        os.system("aplay F.wav")
    elif gesture == 0x04:
        print("right")
        os.system("aplay D.wav")
    