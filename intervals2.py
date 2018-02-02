import setup
import RoboPiLib as RPL
import time
timer = time.time()

def on():
    RPL.servoWrite(0, 2000)
    RPL.servoWrite(1, 1000)
def off():
    RPL.servoWrite(0, 0)
    RPL.servoWrite(1, 0)

while True:
    t = Timer(5.0, on)
    t.start()
    t = Timer(5.0, off)
    t.start()
