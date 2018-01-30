import setup
import RoboPiLib as RPL

close = RPL.digitalRead(16)
print close

try:
    RPL.servoWrite(0, 2000)
    RPL.servoWrite(1, 1000)
except:
    raise ValueError("something went wrong")

RPL.servoWrite(0, 0)
RPL.servoWrite(1, 0)
print "ding dong haha"

if close is 0:
    print "wha"
elif close is 1:
    print "nooooo"

while close is 0:
    print close
while close is 1:
    break
