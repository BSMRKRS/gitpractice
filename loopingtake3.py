import setup
import RoboPiLib as RPL

close = RPL.digitalRead(16)
motorL = 1
motorR = 0

while close != 1:
    close = RPL.digitalRead(16)
if close is 1:
    try:
        RPL.servoWrite(motorL, 0)
        RPL.servoWrite(motorR, 0)
