#This should get the robot to stop
import setup
import RoboPiLib as RPL

motorL = 2
motorR = 0
sense = RPL.digitalRead(16)

RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 2000)

def stop(close):
    print "Made it to the stop function"
    if close == 0:
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)
    return True

goNow = stop(sense)

print "not broken yet in line 21"

while True:
    print "made it to the while loop"
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    stop(RPL.digitalRead(16))
    print "made it through"
    if goNow == 1:
        print "It broke."
        break

while True:
  signal.setitimer(signal.ITIMER_REAL,SHORT_TIMEOUT) # this sets the alarm
  ch = sys.stdin.read(1) # this reads one character of input without requiring an enter keypress
  signal.setitimer(signal.ITIMER_REAL,0) # this turns off the alarm
  if ch == '*': # pressing the asterisk key kills the process
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # this resets the console settings
    break # this ends the loop
