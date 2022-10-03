#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(), '["push ups", "squats", "planks", "summary", "stop", "[unk]"]')

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        if "push ups" in rec.Result():
            print("Pushup rep counting started!")
            with open('summary.json', 'r+') as f:
                info = json.load(f)
                info['current_command'] = "push ups"
                f.seek(0)        # <--- should reset file position to the beginning.
                f.truncate() 
                json.dump(info, f, indent=2)
            break
        elif "squats" in rec.Result():
            print("Squat rep counting started!")
            with open('summary.json', 'r+') as f:
                info = json.load(f)
                info['current_command'] = "squats"
                f.seek(0)        # <--- should reset file position to the beginning.
                f.truncate() 
                json.dump(info, f, indent=2)
            break
        elif "summary" in rec.Result():
            print("Summarizing workout")
            with open('summary.json', 'r+') as f:
                info = json.load(f)
                info['current_command'] = "summary"
                f.seek(0)        # <--- should reset file position to the beginning.
                f.truncate() 
                json.dump(info, f, indent=2)
            break
        elif "stop" in rec.Result():
            print("Stopping count for current workout")
            with open('summary.json', 'r+') as f:
                info = json.load(f)
                info['current_command'] = "stop"
                f.seek(0)        # <--- should reset file position to the beginning.
                f.truncate() 
                json.dump(info, f, indent=2)
            break
    else:
        if "push ups" in rec.PartialResult():
            print("Pushup rep counting started!")
            with open('summary.json', 'r+') as f:
                info = json.load(f)
                info['current_command'] = "push ups"
                f.seek(0)        # <--- should reset file position to the beginning.
                f.truncate() 
                json.dump(info, f, indent=2)
            break
        elif "squats" in rec.PartialResult():
            print("Squat rep counting started!")
            with open('summary.json', 'r+') as f:
                info = json.load(f)
                info['current_command'] = "squats"
                f.seek(0)        # <--- should reset file position to the beginning.
                f.truncate() 
                json.dump(info, f, indent=2)
            break
        elif "summary" in rec.PartialResult():
            print("Summarizing workout")
            with open('summary.json', 'r+') as f:
                info = json.load(f)
                info['current_command'] = "summary"
                f.seek(0)        # <--- should reset file position to the beginning.
                f.truncate() 
                json.dump(info, f, indent=2)
            break
        elif "stop" in rec.PartialResult():
            print("Stopping count for current workout")
            with open('summary.json', 'r+') as f:
                info = json.load(f)
                info['current_command'] = "stop"
                f.seek(0)        # <--- should reset file position to the beginning.
                f.truncate() 
                json.dump(info, f, indent=2)
            break

print(rec.FinalResult())
