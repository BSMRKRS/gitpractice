import setup
import RoboPiLib as RPL

close = RPL.digitalRead(16)
motorL = 2
motorR = 0

thing = 0
while thing is 0:
    if close is 0:
        RPL.servoWrite(motorL, 1000)
        RPL.servoWrite(motorR, 2000)
        print "go"
    if close is 1: # perpetually prints "stop", is always reading 1
        try:
            RPL.servoWrite(motorL, 0)
            RPL.servoWrite(motorR, 0)
        except:
            print "stop"
