# Approach a wall obliquely, turn away from it, and proceed.
# 100%: Maintain forward motion while turning away.

import setup
import RoboPiLib as RPL

front = 16
right = 24

# idea: if reading from right and front, turn off left motor
# and vice versa
# problem: doesn't always sense from both sides.


motorL = 0
motorR = 1
#to run motors
RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 2000)

while True:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    while RPL.digitalRead(16) == 0:
        if RPL.digitalRead(24) == 1: # something ahead and nothing to right, pivot until clear
            RPL.servoWrite(motorR, 1000)
            RPL.servoWrite(motorL, 1000)
        if RPL.digitalRead(24) == 0: # something ahead and to right, pivot until clear
            RPL.servoWrite(motorR, 1000)
            RPL.servoWrite(motorL, 1000)
        if RPL.digitalRead(16) != 0:
            break
    while RPL.digitalRead(16) == 1:
        if RPL.digitalRead(24) == 1: # nothing ahead and nothing to right, go straight
            RPL.servoWrite(motorR, 1000)
            RPL.servoWrite(motorL, 2000)
        if RPL.digitalRead(24) == 0: # nothing ahead but something to right, turn until nothing
            RPL.servoWrite(motorR, 1000)
            RPL.servoWrite(motorL, 0)
        if RPL.digitalRead(16) != 1:
            break

# problem: sensor not picking up walls
# problem: so far only works on right side
