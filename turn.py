import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

front = 17
right = 23

motorL = 2
motorR = 1

while True:
  RPL.servoWrite(motorR, 2000)
  RPL.servoWrite(motorL, 1000)
  future = time.time() + 2
  if RPL.digitalRead(front) == 0:
    while True:
      RPL.servoWrite(motorL, 2000)
      if time.time() > future:
          break
          print "it worked?"
