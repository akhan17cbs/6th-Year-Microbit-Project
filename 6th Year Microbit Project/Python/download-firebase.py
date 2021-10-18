from firebase import firebase
import datetime
import time
import serial

ser = serial.Serial()
ser.baudrate = 115200
ser.port = ('COM7')
ser.open()

fireb_connect = firebase.FirebaseApplication('https://test1-a59b2-default-rtdb.firebaseio.com/', None)

mostrecentKeyID = 0
mostrecentTimestamp = 0


while True:

    myGetResults = fireb_connect.get('/Commands/command/', None)
    
    for keyID in myGetResults:
        if int(int(myGetResults[keyID]['Timestamp']) > mostrecentTimestamp):
               mostrecentTimestamp = int(myGetResults[keyID]['Timestamp'])
               mostrecentKeyID = myGetResults[keyID]
    
    microbitdata = str(myGetResults[keyID]['command'])
    print(microbitdata)
    
    ser.write(microbitdata.encode('UTF-8') + b"\n")
    time.sleep(5)

ser.close()