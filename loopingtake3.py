import setup
import RoboPiLib as RPL

close = RPL.digitalRead(16)
motorL = 1
motorR = 0

for x in xrange(0, 1000000000000000000000000000):
    if close is 1:
        RPL.servoWrite(motorR, 2000)
        RPL.servoWrite(motorL, 1000)
        print "this is %d" % x
    elif close is 0:
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)
        print "this is %d stopped" %x
        break
        print "the loop has been broken."
