
import pyrebase
import os 
firebaseConfig = {
  "apiKey": "AIzaSyAV1s2J1_bsldfUySJdWUFo9oXDfmYUryw",
  "authDomain": "covid19hack-81596.firebaseapp.com",
  "databaseURL": "https://covid19hack-81596.firebaseio.com",
  "projectId": "covid19hack-81596",
  "storageBucket": "covid19hack-81596.appspot.com",
  "messagingSenderId": "1090178939668",
  "appId": "1:1090178939668:web:2e5d6c5648180f8e486001",
  "measurementId": "G-Z6DMG0ZJWN"
};
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
storage.child("username1/Attempt 8.txt").download( os.path.dirname(os.path.realpath(__file__))+"\attempt8.txt")