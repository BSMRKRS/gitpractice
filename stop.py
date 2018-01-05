#This should get the robot to stop
import setup
import RoboPiLib as RPL

motorL = 1
motorR = 0

close = RPL.digitalRead(16)

if close is 0:
    try:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(1, 0)
    except:
        raise ValueError("something weird happened")
elif close is 1:
    try:
        RPL.servoWrite(motorR, 2000)
        RPL.servoWrite(motorL, 1000)
    except:
        raise ValueError("something weird happened")
else:
    raise ValueError("what")
