from locale import dcgettext
import time
import RPi.GPIO as GPIO

class motor:
    def __init__(self, GPIOpin, dc, freq):
        self.pin = GPIOpin # gpio 12
        self.dc = dc
        self.freq = freq

        # attach methods
        self.setmode = GPIO.setmode
        self.setup = GPIO.setup
        self.pwm = GPIO.pwm

    def start(self):
        self.setmode(GPIO.BCM) # refers to GPIO#
        self.setup(self.pin, GPIO.OUT) # using pin as a GPIO out pin
        self.pwm(self.pin, self.freq) # create pwm signal
        self.pwm.start(self.dc) # begin signal

    def stop(self):
        self.pwm.stop()
        GPIO.cleanup() # turn off all pin
        quit() # end program
    
    def set_freq(self, freq_change):
        if freq_change == 'inc':
            self.freq += 1
            self.pwm.ChangeFrequency(self.freq)
        elif freq_change == 'dec':
            self.freq -= 1
            self.pwm.ChangeDutyCycle(self.freq)
        elif isinstance(freq_change, int) == True:
            self.freq = freq_change
            self.pwm.ChangeDutyCyle(freq_change)
        else:
            print('invalid input try again')
        print(self.freq, ' Hz')
    
    def set_dc(self, dc_change):
        if dc_change == 'inc':
            self.dc += 1
            self.pwm.ChangeDutyCycle(self.dc)
        elif dc_change == 'dec':
            self.dc -= 1
            self.pwm.ChangeDutyCycle(self.dc)
        elif isinstance(dc_change, int) == True:
            self.freq = dc_change
            self.pwm.ChangeDutyCyle(dc_change)
        else:
            print('invalid input try again')
        print(self.dc, ' %')

    
m = motor(pin=12, dc=15, freq=55)

while True:
    print('''
    1 - start
    2 - stop
    w - increase frequency by 1 Hz 
    s - decrease frequency
    a - decrease duty cycle
    d - increase duty cycle  
    3 - set frequency
    4 - set duty cycle
    ''')
    cmd = input()
    if cmd == '1':
        m.start()
    elif cmd == '2':
        m.stop()
    elif cmd == 'w':
        m.set_freq('inc')
    elif cmd == 's':
        m.set_freq('dec')
    elif cmd == 'a':
        m.set_dc('dec')
    elif cmd == 'd':
        m.set_dc('inc')
    elif cmd == '3':
        m.set_freq(int(input('new freq (Hz) 30 < f < 1000 : ')))
    elif cmd == '4':
        m.set_dc(int(input('new dc (%) 0 < dc < 100: ')))
    
    

