import setup
import RoboPiLib as RPL

close = RPL.digitalRead(16)
motorL = 1
motorR = 0

while close is 0:
    RPL.servoWrite(motorL, 1000)
    RPL.servoWrite(motorR, 2000)
while close is 1:
    RPL.servoWrite(motorL, 0)
    RPL.servoWrite(motorR, 0)
