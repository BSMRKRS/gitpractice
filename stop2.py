#This should get the robot to stop
import setup
import RoboPiLib as RPL

motorL = 2
motorR = 0
sense = RPL.digitalRead(16)

RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 2000)

def stop(close):
    if close == 0:
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)
        print "Made it to the stop function"
    return True

goNow = stop(sense)

while True:
    print "made it to the while loop"
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    stop(sense)
    if goNow == 1:
        print "It broke."
        break
