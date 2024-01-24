# Lab 3 – Pyrebase example code 
import pyrebase 
import random 
import time 

# Config will contain the information needed to connect to your firebase 
#   The API KEY and Project ID are found in your project settings 
#   The DB URL can be found under the Realtime Database tab 
config = { 
  "apiKey": "YOUR API_KEY", 
  "authDomain": "YOUR_PROJECT_ID.firebaseapp.com", 
  "databaseURL": "YOUR_DATABASE_URL", 
  "storageBucket": "YOUR_PROJECT_ID.appspot.com" 
} 

# Connect using your configuration 
firebase = pyrebase.initialize_app(config) 
db = firebase.database() 
dataset = "sensor1" 
username = "YOUR_USERNAME" 

# Write 10 data entries to the DB in a loop 
key = 0 
while(key<10): 
  # You can use your senseHAT to read in sensor data 
  # We will just use a random number for this demo 
  sensorData = random.random()
  
  # When writing to your DB each child is a JSON key:value pair 
  db.child(username).child(dataset).child(key).set(sensorData) 

  # The above command will add a JSON string to your DB in the form: 
  # { 
  #   "YOUR_USERNAME":{ 
  #     "sensor1":{ 
  #       "<key_VALUE>":"<sensorData_VALUE>" 
  #     } 
  #   } 
  # } 
  # Increment the key and loop 

  key += 1 
  
  # After running the above while loop your DB should look something like this:
  # { 
  #   "YOUR_USERNAME":{ 
  #     "sensor1":{ 
  #       "0":"0.6335737283" 
  #       "1":"0.3235343823" 
  #       "2":"0.4263353683" 
  #       "3":"0.2394958673" 
  #       ... 
  #       "9":"0.8472648495" 
  #     } 
  #   } 
  # } 

# Next, we will retrieve the data we wrote to the DB 
# This code will read all sensor data as a Python dictionary, 
# convert it to a list, extract the final entry, and print its  
# key and value pair 

mySensorData = db.child(username).child(dataset).get() 

print("Parent Key:{}".format(mySensorData.key())) 
print("Parent Value: {}".format(mySensorData.val()))   

# Returns the dictionary as a list 
mySensorData_list = mySensorData.each() 

# Takes the last element of the list 
lastDataPoint = mySensorData_list[-1] 

print("Child Key: {}".format(lastDataPoint.key())) 
print("Child Value: {}\n".format(lastDataPoint.val())) 
