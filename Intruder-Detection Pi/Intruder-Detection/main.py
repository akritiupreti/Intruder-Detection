from gpiozero import MotionSensor
from gpiozero import Buzzer
from host import Host
import Full_Face_Recognition
import time

pir = MotionSensor(4)
buzz = Buzzer(15)

credentials = Host()
isHome = credentials.getStatus()

while True:
    pir.wait_for_motion()
    print("Motion detected!")
    status = Full_Face_Recognition.run(isHome, credentials)
    if status == 1:
        print("INTRUDER")
        buzz.beep(0.2,1)
        time.sleep(3)
    elif status == 0:
        print("Welcome")
    else:
        print("Gate is still closed")
    
    pir.wait_for_no_motion()
    buzz.off()
    print("Motion stopped")
    isHome = credentials.getStatus()
    
