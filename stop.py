#This should get the robot to stop
import setup
import RoboPiLib as RPL

close = RPL.digitalRead(16)
motorL = 1
motorR = 0

thing = 0
while True:
    close == 0
    while True:
        try:
            RPL.servoWrite(motorR, 2000)
            RPL.servoWrite(motorL, 1000)
        except:
            raise ValueError("Something went wrong")
