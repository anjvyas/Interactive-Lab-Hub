import time
import board
import busio
import os
import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)
flag=3
while flag!=0:
    for i in range(12):
        if mpr121[i].value:
            if i==1:
                print(i)
                print("Split")
                os.system("python3 oled_split.py")
                os.system(f"flite -voice slt -t 'Dispensing the pill in Split form'")
                os.system("python3 servo_test_split.py")
                flag-=1
            if i==3:
                print(i)
                print("Whole")
                os.system("python3 oled_whole.py")
                os.system(f"flite -voice slt -t 'Dispensing the pill in Whole form'")
                os.system("python3 servo_test_whole.py")
                flag-=1
            if i==5:
                print(i)
                print("Powdered")
                os.system("python3 oled_powdered.py")
                os.system(f"flite -voice slt -t 'Dispensing the pill in Powdered form'")
                os.system("python3 servo_test_powdered.py")
                flag-=1
    time.sleep(0.25)  # Small delay to keep from spamming output messages.
