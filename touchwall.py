import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now
close = RPL.digitalRead(16)
motorL = 1
motorR = 2
x = 0

RPL.servoWrite(1, 2000)
RPL.servoWrite(2, 1000)

while True:
    future = time.time() + 5
    while RPL.digitalRead(16) == 0:
        while time.time() < future:
            RPL.servoWrite(motorL, 2000)
            RPL.servoWrite(motorR, 1000)
        while time.time() >= future:
            RPL.servoWrite(motorR, 0)
            RPL.servoWrite(motorL, 0)
    while RPL.digitalRead(16) == 1:
        RPL.servoWrite(1, 2000)
        RPL.servoWrite(2, 1000)
