from flask import Flask, render_template, request

import paho.mqtt.client as mqtt
import uuid
import json

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/pill_dispenser'

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

@app.route('/form', methods = ['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('doctor.html')
    if request.method == 'POST':
        json_data = {}
        doctor_data = request.form
        for k, v in doctor_data.items():
            json_data[k] = v
        client.publish(topic, json.dumps(json_data))
        return render_template('doctor.html')