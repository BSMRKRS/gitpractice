import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now
futureplus = now
close = RPL.digitalRead(16)
motorL = 1
motorR = 2
x = 0

RPL.servoWrite(2, 2000)
RPL.servoWrite(1, 1000)

while True:
    while RPL.digitalRead(16) == 0:
        future = time.time() + 5
        futureplus = future + 5
        while time.time() < future:
            RPL.servoWrite(2, 2000)
            RPL.servoWrite(1, 1000)
        while time.time() > future and time.time() < futureplus:
            RPL.servoWrite(2, 0)
            RPL.servoWrite(1, 0)
        x = x + 1
        while x == 10:
            break
    while RPL.digitalRead(16) == 1:
        RPL.servoWrite(2, 2000)
        RPL.servoWrite(1, 1000)
