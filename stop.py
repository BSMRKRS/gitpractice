#This should get the robot to stop
import setup
import RoboPiLib as RPL

motorL = 0
motorR = 1

close = RPL.digitalRead(16)

if close = 0:
    try:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(1, 0)
