import setup
import RoboPiLib as RPL

close = RPL.digitalRead(17)
motorL = 2
motorR = 0

while close is 1:
    RPL.servoWrite(motorL, 1000)
    RPL.servoWrite(motorR, 2000)
    if close is 0:
        break
        print "It broke."
while close is 0:
    RPL.servoWrite(motorL, 0)
    RPL.servoWrite(motorR, 0)
