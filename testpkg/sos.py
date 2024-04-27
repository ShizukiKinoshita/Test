import RPi.GPIO as GPIO                                           
import time

class LED():
    def sos(self,LedGpio = 18,n = 10): #モールス信号SOS　好きな光でモールス信号を出す
        
        WaitTime = 1

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LedGpio,GPIO.OUT)

        for i in range(n):
            for i in range(3):
                GPIO.output(LedGpio,True)  # 点灯
                time.sleep(WaitTime)  # 1秒間点灯
                GPIO.output(LedGpio,False) # 消灯
                time.sleep(WaitTime*0.5)  # 1秒間消灯
            for i in range(2):
                GPIO.output(LedGpio,True)  # 点灯
                time.sleep(WaitTime*2)  # 1秒間点灯
                GPIO.output(LedGpio,False) # 消灯
                time.sleep(WaitTime*0.5)  # 1秒間消灯
            for i in range(3):
                GPIO.output(LedGpio,True)  # 点灯
                time.sleep(WaitTime)  # 1秒間点灯
                GPIO.output(LedGpio,False) # 消灯
                time.sleep(WaitTime*0.5)  # 1秒間消灯  

        GPIO.cleanup()