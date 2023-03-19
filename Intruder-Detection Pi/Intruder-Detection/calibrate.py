from gpiozero import MotionSensor
from gpiozero import Buzzer
import time


pir = MotionSensor(4)
buzz = Buzzer(15)

while True:
	pir.wait_for_motion()
	print("Motion detected")
	buzz.beep(0.1,1)
	pir.wait_for_no_motion()
	buzz.off()
	print("Motion stopped")

