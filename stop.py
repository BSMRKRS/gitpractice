#This should get the robot to stop
import setup
import RoboPiLib as RPL

close = RPL.digitalRead(16)
motorL = 1
motorR = 0

thing = 0

while thing = 0:
    if close is 0:
        try:
            RPL.servoWrite(motorR, 0)
            RPL.servoWrite(motorL, 0)
        except:
            raise ValueError("something weird happened")
        elif close is 1:
            try:
                RPL.servoWrite(motorR, 1000)
                RPL.servoWrite(motorL, 2000)
            except:
                raise ValueError("something weird happened")
    else:
        try:
            RPL.digitalRead(16)
