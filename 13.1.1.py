import setup
import RoboPiLib as RPL

close = RPL digitalRead(16)

if close is 0
  try:
      RPL servoWrite(0,1)
      RPL servoWrite(1,0)

if close is 1
  try:
    RPL servoWrite(0,1000)
    RPL servoWrite(1,1000)
