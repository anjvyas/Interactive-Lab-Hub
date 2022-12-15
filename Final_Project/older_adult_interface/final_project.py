import cv2
import pytesseract
from pytesseract import Output
import os
import time
import board
from adafruit_apds9960.apds9960 import APDS9960
import busio
import adafruit_mpr121
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
#Get info from Database
import datetime
import calendar
import json
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Database connection + fetching function
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   db_pwd = os.getenv("DB_PWD")
   CONNECTION_STRING = f"mongodb+srv://anjali:{db_pwd}@cluster0.sea1mts.mongodb.net/?retryWrites=true&w=majority"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['pill_dispenser']

#Get data from Proximity Sensor

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

i2c = board.I2C()
apds = APDS9960(i2c)

apds.enable_proximity = True
obj_not_detected = True
while obj_not_detected:
    print("Distance: ",apds.proximity)
    time.sleep(0.2)
    obj_not_detected = False

#Turn on Camera for OCR function
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
med_list=[]
txt_not_detected = True

while txt_not_detected and not(obj_not_detected):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    d = pytesseract.image_to_data(frame, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (text, x, y, w, h) = (d['text'][i], d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            # don't show empty text
            if text and text.strip() != "":
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                frame = cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
                if (text=='Vitamin') or (text=='ONCE'):
                    med_name1 = "Vitamin D3"
                   # print(med_name1)
                    print("Med Distance: ",apds.proximity)
                    detected_med="The detected medicine is "+ med_name1 
                    os.system(f"flite -voice slt -t '{detected_med}'")
                    os.system("python3 oled.py")
                    med_list.append(med_name1)
                    txt_not_detected=False
                    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Dispensing
os.system(f"flite -voice slt -t 'How do you want to consume your pill? Click on the buttons below'")
os.system("python3 cap_test.py")
pilldispenser_db = get_database()
pres_collection = pilldispenser_db['prescriptions']
pres_info = pres_collection.find_one({"id": 1})

if pres_info != None:
    medicine_name = pres_info["name"]
    print(medicine_name)
    
if med_name1 in medicine_name:
    print(med_name1," is a prescribed medicine")
else:
    print(med_name1, " is not a prescribed medicine")
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
