# Approach a wall obliquely, turn away from it, and proceed.
# 100%: Maintain forward motion while turning away.

import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

front = 17
right = 23

# idea: if reading from right and front, turn off left motor
# and vice versa
# problem: doesn't always sense from both sides.

motorL = 0
motorR = 2

# R 2000 is forward
# L 1000 is forward

while True:
    RPL.servoWrite(motorR, 2000)
    RPL.servoWrite(motorL, 1000)
    future = time.time() + 1
    if RPL.digitalRead(17) == 0: # or RPL.digitalRead(23) == 0: # something ahead or to right, pivot
        while True:
            RPL.servoWrite(motorL, 2000)
            RPL.servoWrite(motorR, 1600)
            if time.time() > future:
                break
                print "it worked?"


# possible problem: sensor not picking up walls
# problem: so far only works on right side
