import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now
futureplus = now

while True:
    future = time.time() + 5
    futureplus = future + 5
    while time.time() < future:
        RPL.servoWrite(0, 2000)
        RPL.servoWrite(1, 1000)
    while time.time() > future and time.time() < futureplus:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(1, 0)
