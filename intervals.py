import setup
import RoboPiLib as RPL
import time
timer = time.time()

while True:
    if timer % 5:
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
