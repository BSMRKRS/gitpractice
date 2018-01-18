import setup
import RoboPiLib as RPL

numbers = []
thing < 1000
while True:
    thing = thing + 1
    numbers.append(thing)
if thing % 4:
    try:
        RPL.servoWrite(0, 2000)
        RPL.servoWrite(1, 1000)
    except:
        raise ValueError("something went wrong")
else:
    try:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(1, 0)
    except:
        raise ValueError("something went wrong")
