#This should get the robot to stop
import setup
import RoboPiLib as RPL

motorL = 2
motorR = 0

RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 2000)

def stop(close):
    if close is 0:
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)

goNow = stop(RPL.digitalRead(16))

while motorL == 2:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    stop(RPL.digitalRead(16))
    if goNow == 1:
        print "It broke."
        break
