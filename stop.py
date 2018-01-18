#This should get the robot to stop
import setup
import RoboPiLib as RPL

close = RPL.digitalRead(16)
motorL = 1
motorR = 0

thing = 0
while True:
    if close is 0:
        try:
            RPL.servoWrite(motorR, 0)
            RPL.servoWrite(motorL, 0)
        except:
            raise ValueError("something weird happened")
    elif close is 1:
        try:
            close
            if close is 0:
                try:
                    RPL.servoWrite(motorR, 0)
                    RPL.servoWrite(motorR, 0)
                except:
                    raise ValueError("Ugh")
        except:
            raise ValueError("Hnggg")
