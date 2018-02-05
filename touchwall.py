import setup
import RoboPiLib as RPL
import time

timer = time.time()
close = RPL.digitalRead(16)
x = 1000
y = 2000
s = 1600
w = 100
motorL = 1
motorR = 2

RPL.servoWrite(motorL, x)

while True:
    while RPL.digitalRead(16) == 0:
        RPL.servoWrite(motorR, s)
        RPL.servoWrite(motorL, w)
    while RPL.digitalRead(16) == 1:
        while timer < 5:
            RPL.servoWrite(motorR, x)
            RPL.servoWrite(motorL, y)
        while timer > 5:
            RPL.servoWrite(motorR, 0)
            RPL.servoWrite(motorL, 0)
