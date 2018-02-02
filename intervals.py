import setup
import RoboPiLib as RPL
import time
timer = time.time()
motorL = 1
motorR = 0

while time < 5:
    try:
        RPL.servoWrite(motorL, 1000)
        RPL.servoWrite(motorR, 2000)
    except:
        raise ValueError("something happened")
    if time > 5:
        break
while time > 5:
    try:
        RPL.servoWrite(motorL, 0)
        RPL.servoWrite(motorR, 0)
    except:
        raise ValueError("something happened")
    if time is 10:
        time = 0
        break
