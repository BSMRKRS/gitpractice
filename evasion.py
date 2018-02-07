# Approach a wall obliquely, turn away from it, and proceed.
# 100%: Maintain forward motion while turning away.

import setup
import RoboPiLib as RPL

front = 16
right = 24

# idea: if reading from right and front, turn off left motor
# and vice versa
# problem: doesn't always sense from both sides.

# took out motorR because it never changes

motorL = 2
motorR = 1
#to run motors
RPL.servoWrite(motorR, 2000)
RPL.servoWrite(motorL, 1000)
# R 2000 is forward
# L 1000 is forward

while True:
    RPL.servoWrite(motorR, 2000)
    RPL.servoWrite(motorL, 1000)
    while RPL.digitalRead(16) == 0: # something ahead, pivot
        RPL.servoWrite(motorL, 2000)
    while RPL.digitalRead(16) == 1:
        if RPL.digitalRead(24) == 1: # nothing ahead and nothing to right, go straight
            RPL.servoWrite(motorL, 1000)
        if RPL.digitalRead(24) == 0: # nothing ahead but something to right, turn until nothing
            RPL.servoWrite(motorL, 2000)


# possible problem: sensor not picking up walls
# problem: so far only works on right side

# PROBLEM: motorL not turning on, unless it's going backwards becauase there's something ahead
