import RPi.GPIO as GPIO                                           
import time

def Led():
    LedGpio = 18
    WaitTime = 1

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedGpio,GPIO.OUT)

    for i in range(10):
        GPIO.output(LedGpio,True)  # 点灯
        time.sleep(WaitTime)  # 1秒間点灯
        GPIO.output(LedGpio,False) # 消灯
        time.sleep(WaitTime)  # 1秒間消灯

    GPIO.cleanup()
