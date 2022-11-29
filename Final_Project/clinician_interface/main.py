from flask import Flask, render_template, request

from pymongo import MongoClient
from dotenv import load_dotenv
import os

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

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

@app.route('/form', methods = ['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('doctor.html')
    if request.method == 'POST':
        doctor_data = request.form
        
        pilldispenser_db = get_database()
        pres_collection = pilldispenser_db['prescriptions']
        
        # add the prescription information to our DB!
        pres_info = pres_collection.find_one({"id": 1})

        to_add = {"id": 1}

        for k, v in doctor_data.items():
            to_add[k] = v.split(",")

        if pres_info != None:
            pres_collection.replace_one({"id": 1}, to_add)
        else:
            pres_collection.insert_one(to_add)

        return render_template('doctor.html')