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

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
#font = ImageFont.load_default()
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)
c=4
while c!=0:
    for i in range(12):
        if mpr121[i].value:
            print(f"Twizzler {i} touched!")
            c=c-1
    time.sleep(0.25)  # Small delay to keep from spamming output messages.

i2c = board.I2C()
apds = APDS9960(i2c)

apds.enable_proximity = True
obj_not_detected = True
while obj_not_detected:
    print("Distance: ",apds.proximity)
    time.sleep(0.2)
    obj_not_detected = False

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
                print(text)
                if (text=='Vitamin') or (text=='ONCE'):
                    med_name1 = "Vitamin D3"
                    print(med_name1)
                    print("Med Distance: ",apds.proximity)
                    detected_med="The detected medicine is "+ med_name1 
                    os.system(f"flite -voice slt -t '{detected_med}'")
                  #  os.system("python3 oled_test.py")
                    med_list.append(med_name1)
                    draw.rectangle((0,0,width,height), outline=0, fill=0)
                    draw.text((x, top),med_name1,  font=font, fill=255)
                    # Display image.
                    disp.image(image)
                    disp.display()
                    sleep(.1)
                    txt_not_detected=False
                    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()