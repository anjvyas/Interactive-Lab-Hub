import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import
import time
from datetime import datetime
from pytz import timezone

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# pylint: disable=line-too-long
# Create the display:
# disp = st7789.ST7789(spi, rotation=90,                            # 2.0" ST7789
# disp = st7789.ST7789(spi, height=240, y_offset=80, rotation=180,  # 1.3", 1.54" ST7789
# disp = st7789.ST7789(spi, rotation=90, width=135, height=240, x_offset=53, y_offset=40, # 1.14" ST7789
# disp = hx8357.HX8357(spi, rotation=180,                           # 3.5" HX8357
# disp = st7735.ST7735R(spi, rotation=90,                           # 1.8" ST7735R
# disp = st7735.ST7735R(spi, rotation=270, height=128, x_offset=2, y_offset=3,   # 1.44" ST7735R
# disp = st7735.ST7735R(spi, rotation=90, bgr=True,                 # 0.96" MiniTFT ST7735R
# disp = ssd1351.SSD1351(spi, rotation=180,                         # 1.5" SSD1351
# disp = ssd1351.SSD1351(spi, height=96, y_offset=32, rotation=180, # 1.27" SSD1351
# disp = ssd1331.SSD1331(spi, rotation=180,                         # 0.96" SSD1331
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)
# pylint: enable=line-too-long

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# hardcoding for testing and video
# 6:20am
# hours = 6
# minutes = 20
# 2am
# hours = 2
# minutes = 0
# 12:55pm
# hours = 12
# minutes = 55
# 12:55am
# hours = 0
# minutes = 55

cur_angle = 0
india_time = False
center_right = True
location = "NYC"

while True:
    # get time values
    hours = int(time.strftime('%-H'))
    minutes = int(time.strftime('%-M'))
    
    # check for button press
    if not buttonA.value or not india_time: # set the timezone to nyc
        hours = int(datetime.now(timezone('EST')).strftime('%-H'))
        minutes = int(datetime.now(timezone('EST')).strftime('%-M'))
        india_time = False
        location = "NYC"
        if not buttonA.value:
            print("NYC Time :D")
        
    if not buttonB.value or india_time: # set the timezone to India
        hours = int(datetime.now(timezone('Asia/Calcutta')).strftime('%-H'))
        minutes = int(datetime.now(timezone('Asia/Calcutta')).strftime('%-M'))
        india_time = True
        location = "India"
        if not buttonB.value:
            print("India Time ^_^")
    
    minutes_10 = minutes // 10
    minutes_0to9 = minutes % 10
    
    center_img = 'Sun'
    hour_img = 'flower.png'
    min_img = 'leaf.png'
    bg_col = (255, 255, 255)
    text_col = (0, 0, 0)
    center_size = 110
    
    # it's nighttime, draw the moon and stars instead!
    if hours < 6 or hours > 18:
        center_img = 'Moon'
        center_size = 100
        hour_img = 'yellow_star.png'
        min_img = 'white-star.png'
        bg_col = (0, 0, 0)
        text_col = (255, 255, 255)
    
    center_img = center_img + str(minutes_0to9) + ".png"
    
    hour_count = hours
    if hours > 12:
        hour_count = hours - 12
    elif hours == 0:
        hour_count = 12
        
    center_image = Image.open(center_img)
    center_image = center_image.resize((center_size, center_size), Image.BICUBIC)
    center_image = center_image.rotate(90, Image.NEAREST, expand=1)
    
    if center_right:
        center_image = center_image.rotate(15, Image.NEAREST, expand=1)
    else:
        center_image = center_image.rotate(-15, Image.NEAREST, expand=1)
        
    center_right = not center_right
    # center the moon / sun
    x_center = width // 2 - center_image.width // 2
    y_center = height // 2 - center_image.height // 2

    # make sure the sky color is in line with the time of day
    draw.rectangle((0, 0, width, height), outline=0, fill=bg_col)
    # paste the center image (sun/moon) onto the background
    image.paste(center_image, (x_center+10, y_center), mask=center_image)

    # add as many hour images as there are hours
    hour_img = Image.open(hour_img)
    hour_img = hour_img.resize((18, 18), Image.BICUBIC)

    x_hour = 10
    y_hour = height // 2 + (hour_count*(1 + hour_img.width)//2) - 20
    for i in range(hour_count):
        # add a small rotation for a fun effect
        hour_img = hour_img.rotate(cur_angle, Image.NEAREST)
        image.paste(hour_img, (x_hour, y_hour), mask=hour_img)
        y_hour -= (1 + hour_img.width)

    # add as many minute images as there are 10 minutes
    min_img = Image.open(min_img)
    min_img = min_img.resize((20, 20), Image.BICUBIC)

    x_min = width - (min_img.width + 10)
    y_min = height // 2 + (minutes_10*(5 + min_img.width)//2) - 20
    for i in range(minutes_10):
        # add a small rotation for a fun effect
        min_img = min_img.rotate(cur_angle, Image.NEAREST)
        image.paste(min_img, (x_min, y_min), mask=min_img)
        y_min -= (5 + min_img.width)
        
        
    # add simple rotation for a fun effect
    time_val = Image.new("RGB", (50, 50), bg_col)
    draw_time = ImageDraw.Draw(time_val)
    draw_time.text((0, 0),location,text_col,font=font)
    rot_im = time_val.rotate(90, expand=False)
    image.paste(rot_im, (60, 30))
    
    disp.image(image)
    if cur_angle == 90:
        cur_angle = 0
    else:
        cur_angle = 90
        
    time.sleep(1)
