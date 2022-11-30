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

def findDay():
    born = datetime.datetime.strptime(str(datetime.date.today()), '%Y-%m-%d').weekday()
    return (calendar.day_name[born])

keep_going = True

while keep_going:
    # get the current day and time
    currentDay = findDay()
    current_time = datetime.datetime.now()

    # get prescription info from our DB
    pilldispenser_db = get_database()
    pres_collection = pilldispenser_db['prescriptions']
    pres_info = pres_collection.find_one({"id": 1})

    if pres_info != None:
        times = pres_info[currentDay]
        medicine_name = pres_info["name"][0]
        if len(times) > 0:
            for t in times:
                time_data = t.split(":")
                h = time_data[0]
                m = time_data[1]

                if m[0] == '0':
                    m = m[1:]

                if str(current_time.hour) == h and str(current_time.minute) == str(m):
                    # for mac testing
                    # os.system(f"say 'Hi there! It's time to take {medicine_name}'")
                    # os.system(f"say 'How do you want to consume your pill? Click on a button below'")
                    # # for pi testing
                    os.system(f"flite -voice slt -t 'Hi there, it is time to take {medicine_name}'")
                    time.sleep(0.2)
                    os.system(f"flite -voice slt -t 'How do you want to consume your pill? Click on a button below'")
                    keep_going = False
    else:
        os.system(f"flite -voice slt -t 'The prescription has not been loaded yet'")

    time.sleep(1)