#This should get the robot to stop
import setup
import RoboPiLib as RPL

motorL = 2
motorR = 0
close = RPL.digitalRead(16)

RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 2000)

def stop(close):
    while close == 0:
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)
        print "There's something"
    return True

while True:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    stop(close)
    if close == 1:
        print "There's nothing"
