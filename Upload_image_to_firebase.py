

#Thư viện hỗ trợ
from datetime import datetime
from picamera import PiCamera
from time import sleep
import os
import pyrebase

#api key firebase
firebaseConfig = {
    'apiKey': "AIzaSyBtbt86NZAGdha9EibXs5N2UXdtRCJ25EA",
    'authDomain': "tudiendict.firebaseapp.com",
    'databaseURL': "https://tudiendict-default-rtdb.firebaseio.com",
    'projectId': "tudiendict",
    'storageBucket': "tudiendict.appspot.com",
    'messagingSenderId': "344257519816",
    'appId': "1:344257519816:web:a60248af82e0b1448585fd",
    'measurementId': "G-QHEVM1KB3J"
}

firebase = pyrebase.initialize_app ( firebaseConfig )

storage = firebase.storage ()

camera = PiCamera ()

while True:
    try:
     
            now = datetime.now ()
            dt = now.strftime ( "%d%m%Y%H:%M:%S" )
            name = dt + ".jpg"
            camera.capture ( name )
            print ( name + " saved" )
            storage.child ( name ).put ( name )
            print ( "Image sent" )
            os.remove ( name )
            print ( "File Removed" )
            sleep ( 5 )


    except:
        camera.close ()

