

#Thư viện hỗ trợ
import RPi.GPIO as GPIO
GPIO.setwarnings ( False )
GPIO.setmode ( GPIO.BOARD )
GPIO.setup ( 10 , GPIO.IN , pull_up_down=GPIO.PUD_DOWN )
from datetime import datetime
from picamera import PiCamera
from time import sleep
import os
import pyrebase

#api key firebase
firebaseConfig = {
    'apiKey': "AIzaSyA9RPYldW1Bh6FTxKEpvi6ntrHxTEpZeoc" ,
    'authDomain': "rpi-image-e562d.firebaseapp.com" ,
    'databaseURL': "https://rpi-image-e562d-default-rtdb.firebaseio.com" ,
    'projectId': "rpi-image-e562d" ,
    'storageBucket': "rpi-image-e562d.appspot.com" ,
    'messagingSenderId': "835517945977" ,
    'appId': "1:835517945977:web:15e42f3420a70ae9d8dca8" ,
    'measurementId': "G-HK159X6WJ3"

}

firebase = pyrebase.initialize_app ( firebaseConfig )

storage = firebase.storage ()

camera = PiCamera ()

while True:
    try:
        if GPIO.input ( 10 ) == GPIO.HIGH:
            print ( "pushed" )
            now = datetime.now ()
            dt = now.strftime ( "%d%m%Y%H:%M:%S" )
            name = dt + ".jpg"
            camera.capture ( name )
            print ( name + " saved" )
            storage.child ( name ).put ( name )
            print ( "Image sent" )
            os.remove ( name )
            print ( "File Removed" )
            sleep ( 2 )


    except:
        camera.close ()

