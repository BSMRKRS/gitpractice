import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

front = 16
right = 23

# idea: if reading from right and front, turn off left motor
# and vice versa
# problem: doesn't always sense from both sides.

motorL = 1
motorR = 2

# R 2000 is forward
# L 1000 is forward

while True:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    future = time.time() + 2
    if RPL.digitalRead(16) == 0 or RPL.digitalRead(23) == 0: # something ahead or to right, pivot
        RPL.servoWrite(motorL, 0)
        RPL.servoWrite(motorR, 0)
        while time.time() < future:
            RPL.servoWrite(motorR, 2000)



# possible problem: sensor not picking up walls
# problem: so far only works on right side
