import setup
import RoboPiLib as RPL

close = RPL.digitalRead(16)

motorL = 1
motorR = 0
x = 1000
y = 2000

RPL.servoWrite(motorL, x)
RPL.servoWrite(motorR, y)
while True:
    while RPL.digitalRead(16) == 0:
        if x > 0:
            x = x - 0.5
            print "slowing down"
            if x is 0:
                break
                print "broke"
        if y > 0:
            y = y - 1
            print "slowing this one"
            if y is 0:
                break
                print "broken 2x"
    while RPL.digitalRead(16) == 1:
        RPL.servoWrite(motorL, 1000)
        RPL.servoWrite(motorR, 2000)
        print "still goin'"
