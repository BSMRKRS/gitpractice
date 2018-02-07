import setup
import RoboPiLib as RPL
import time

timer = time.time()
close = RPL.digitalRead(16)
motorL = 1
motorR = 2

RPL.servoWrite(motorL, 2000)
RPL.servoWrite(motorR, 1000)

while True:
    while RPL.digitalRead(16) == 0:
        while timer < 1000:
            RPL.servoWrite(motorL, 1600)
            RPL.servoWrite(motorR, 100)
            print timer
        while timer >= 1000:
            RPL.servoWrite(motorL, 0)
            RPL.servoWrite(motorR, 0)
            print timer
    while RPL.digitalRead(16) == 1:
        RPL.servoWrite(motorL, 2000)
        RPL.servoWrite(motorR, 1000)
