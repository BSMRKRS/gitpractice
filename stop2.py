# trying stop but with a function and a while loop
import setup
import RoboPiLib as RPL

close = RPL.digitalRead(16)
motorL = 2
motorR = 0

def stop(close):
    if close is 0:
        try:
            RPL.servoWrite(motorR, 0)
            RPL.servoWrite(motorL, 0)
        except:
            raise ValueError("something weird happened")
    elif close is 1:
        print " "

while motorL is 2:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    stop(close)
