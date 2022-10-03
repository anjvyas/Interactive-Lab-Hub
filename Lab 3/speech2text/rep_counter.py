import board
import busio
import adafruit_apds9960.apds9960
import time
import os
import json
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_proximity = True

current_command = "none"
curr_count = 0

while current_command != "end":
	prox = sensor.proximity
	with open('summary.json', 'r+') as f:
		info = json.load(f)
		if info["current_command"] != current_command: # the exercise has been changed
			current_command = info["current_command"]
			curr_count = 0

		if current_command == "push ups":
			if prox > 20:
				curr_count += 1
				print(curr_count)
				os.system(f"flite -voice slt -t '{str(curr_count)}'")
				info['num_pushups'] = str(int(info['num_pushups']) + 1)
				f.seek(0)        # <--- should reset file position to the beginning.
				f.truncate() 
				json.dump(info, f, indent=2)
			time.sleep(0.2)
		elif current_command == "squats":
			if prox > 20:
				curr_count += 1
				os.system(f"flite -voice slt -t '{str(curr_count)}'")
				info['num_squats'] = str(int(info['num_squats']) + 1)
				f.seek(0)        # <--- should reset file position to the beginning.
				f.truncate() 
				json.dump(info, f, indent=2)
			time.sleep(0.2)
		elif current_command == "stop":
			curr_count = 0
			time.sleep(0.2)
		elif current_command == "summary":
			p = str(info['num_pushups'])
			s = str(info['num_squats'])
			os.system(f"flite -voice slt -t 'You did {p} pushups and {s} squats, great job!!!'")
			current_command = "end"