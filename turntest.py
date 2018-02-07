import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now
futureplus = now

while True:
    future = time.time() + 2
    futureplus = future + 2
    while time.time() < future:
        RPL.servoWrite(1, 1000)
    while time.time() > future and time.time() < futureplus:
        RPL.servoWrite(1, 0)
    break

while True:
    future = time.time() + 2
    futureplus = future + 2
    while time.time() < future:
        RPL.servoWrite(1, 1000)
        RPL.servoWrite(2, 1000)
    while time.time() > future and time.time() < futureplus:
        RPL.servoWrite(1, 0)
        RPL.servoWrite(2, 0)
    break
