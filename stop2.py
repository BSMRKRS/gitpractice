#This should get the robot to stop
import setup
import RoboPiLib as RPL

motorL = 1
motorR = 0

RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 2000)



while True:
    while RPL.digitalRead(16) == 0:
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)
        print RPL.digitalRead(16)
        if RPL.digitalRead(16) == 1:
            break
    while RPL.digitalRead(16) == 1:
        RPL.servoWrite(motorR, 1000)
        RPL.servoWrite(motorL, 2000)
        print RPL.digitalRead(16)
        if RPL.digitalRead(16) == 0:
            break
