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
        RPL.servoWrite(1, 1000)
    while time.time() > future and time.time() < futureplus:
        RPL.servoWrite(1, 0)
    break
