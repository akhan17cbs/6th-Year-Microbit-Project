# py -3.6 -m pip install firebase, pyserial, python_jwt, pycryptodome, sseclient, gcloud
from firebase import firebase
import datetime
import time
import serial

ser = serial.Serial()
ser.baudrate = 115200
ser.port = ('COM5')
ser.open()

fireb_connect = firebase.FirebaseApplication('https://test1-a59b2-default-rtdb.firebaseio.com/', None)


while True:

    microbitdata = str(ser.readline())

    temperature = microbitdata[2:]
    temperature = temperature.replace(" ","")
    temperature = temperature.replace("\\r\\n","")
    temperature = temperature.replace("'","")
    temperature = int(temperature)
    
    now = int(datetime.datetime.today().strftime("%Y%m%d%H%M%S"))

    data_to_upload = {
        'Temp' : temperature,
        'Timestamp' : now
    }

    fireb_result = fireb_connect.post('/temperature/temp', data_to_upload)
    print(temperature)
    print(fireb_result)

    time.sleep(5)

ser.close()