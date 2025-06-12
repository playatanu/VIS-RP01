import RPi.GPIO as GPIO
import time 

from core.detection import color, text, object
from core import datetime

BUTTON_PIN_1 = 17 #11
BUTTON_PIN_2 = 27 #13
BUTTON_PIN_3 = 22 #15
BUTTON_PIN_4 = 23 #16
BUTTON_PIN_5 = 24 #18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("waiting for button press..")

try:
    while True:
        if GPIO.input(BUTTON_PIN_1) == GPIO.LOW:
            print("1st button pressed!")
            color.detect()
            time.sleep(1)
        
        if GPIO.input(BUTTON_PIN_2) == GPIO.LOW:
            print("2st button pressed!")
            text.detect()
            time.sleep(1)
            
        if GPIO.input(BUTTON_PIN_3) == GPIO.LOW:
            print("3rd button pressed!")
            object.detect()
            time.sleep(1)
            
        if GPIO.input(BUTTON_PIN_4) == GPIO.LOW:
            print("4th button pressed!")
            datetime.current_time()
            time.sleep(1)
        
        if GPIO.input(BUTTON_PIN_5) == GPIO.LOW:
            print("4th button pressed!")
            datetime.current_date()
            time.sleep(1)
            
except KeyboardInterrupt:
    GPIO.cleanup
