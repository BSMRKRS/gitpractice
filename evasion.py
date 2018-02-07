# Approach a wall obliquely, turn away from it, and proceed.
# 100%: Maintain forward motion while turning away.

import setup
import RoboPiLib as RPL

front = 16
right = 23

# idea: if reading from right and front, turn off left motor
# and vice versa
# problem: doesn't always sense from both sides.

# took out motorR because it never changes

motorL = 2
motorR = 1

# R 2000 is forward
# L 1000 is forward

while True:
    RPL.servoWrite(motorR, 2000)
    RPL.servoWrite(motorL, 1000)
    while RPL.digitalRead(16) == 0: # something ahead or to right, pivot
        RPL.servoWrite(motorL, 2000)
    while RPL.digitalRead(23) == 0:
        RPL.servoWrite(motorL, 2000)


# possible problem: sensor not picking up walls
# problem: so far only works on right side

# PROBLEM: motorL not turning on, unless it's going backwards becauase there's something ahead
