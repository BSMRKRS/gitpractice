#This should get the robot to stop
import setup
import RoboPiLib as RPL

motorL = 2
motorR = 0
close = RPL.digitalRead(16)

RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 2000)

# def stop(close):
#    while close == 0:
#        RPL.servoWrite(motorR, 0)
#        RPL.servoWrite(motorL, 0)
#        print "There's something"
#    return True

while True:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    if close == 0:
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)
        print "there's something."
    ch = sys.stdin.read(1) # this reads one character of input without requiring an enter keypress
    if ch == '*': # pressing the asterisk key kills the process
      break # this ends the loop
