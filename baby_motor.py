import time
import RPi.GPIO as GPIO

for i in range(0,5):
    time.sleep(1)
    print(5-i)

# Broadcom chip-specific pin numbers.
# These pin numbers follow the lower-level numbering system defined by
# the Raspberry Pi's Broadcom-chip brain.
GPIO.setmode(GPIO.BCM) 

motor = 4 # GPIO04
GPIO.setup(motor, GPIO.OUT)

starting_freq = 0.5
starting_dc = 10
m = GPIO.PWM(motor, starting_freq)

print('starting')
m.start(starting_dc)

for i in range(1,11):
    #t1.ChangeDutyCycle(i*10) # arguement will be the new dc
    #print('current dc: ', i*10)
    
    #t1.ChangeFrequency(i) # arguement will be the new frequency
    #print('current freq: ', starting_freq + i)
    
    time.sleep(2)
    print(11-i)
    
# exception handler for
# 0Hz < f < 15kHz
# 0 < dc < 100

# input to allow:
# increase speed
# decrease speed
# ready/on may need to spin motor first 
# off

m.stop()
print('stopped')

GPIO.cleanup()
quit()
