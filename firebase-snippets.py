import pyrebase
import random
import time

# Create new Firebase config and database object
config = {
  "apiKey": "YOUR_API_KEY",
  "authDomain": "YOUR_PROJECT_ID.firebaseapp.com",
  "databaseURL": "YOUR_DATABASE_URL",
  "storageBucket": "YOUR_PROJECT_ID.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
dataset = "sensor1"

# Write random numbers to database
def writeData():
  key = 0

  while True:
    # I'm using dummy sensor data here, you could use your senseHAT
    sensorData = random.random()

    # Will be written in this form:
    # {
    #   "sensor1" : {
    #     "0" : 0.6336863763908736,
    #     "1" : 0.33321038818190285,
    #     "2" : 0.6069185320998802,
    #     "3" : 0.470459178006184,
    #   }
    # }
    # Each 'child' is a JSON key:value pair
    db.child(dataset).child(key).set(sensorData)

    key = key + 1
    time.sleep(1)

def readData():
  # Returns the entry as an ordered dictionary (parsed from json)
  mySensorData = db.child(dataset).get()

  print("Parent Key: {}".format(mySensorData.key()))
  print("Parent Value: {}\n".format(mySensorData.val()))

  # Returns the dictionary as a list
  mySensorData_list = mySensorData.each()
  # Takes the last element of the list
  lastDataPoint = mySensorData_list[-1]

  print("Child Key: {}".format(lastDataPoint.key()))
  print("Child Value: {}\n".format(lastDataPoint.val()))

