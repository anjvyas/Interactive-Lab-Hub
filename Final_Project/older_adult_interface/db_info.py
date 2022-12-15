import time
import datetime
import calendar
import os
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

t=1
while t!=0:
    # get prescription info from our DB
    pilldispenser_db = get_database()
    pres_collection = pilldispenser_db['prescriptions']
    pres_info = pres_collection.find_one({"id": 1})

    if pres_info != None:
        medicine_name = pres_info["name"]
        print(medicine_name)
        t=t-1