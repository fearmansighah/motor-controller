import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

motor = 1
GPIO.setup(motor, GPIO.OUT)  # output

for i in range(10):
    GPIO.output(motor, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(motor, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()

quit()
