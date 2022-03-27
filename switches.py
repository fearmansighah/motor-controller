import time
import RPi.GPIO as GPIO

class gate:
    def __init__(self, GPIOpin, dc, freq):
        self.pins = GPIOpin #gpio#
        self.dc = dc
        self.freq = freq


    def add_delay(self):
        self.delay = 1/self.freq*self.dc


    def begin(self):
        self.setmode = GPIO.setmode(GPIO.BCM) # refers to GPIO#
        
        self.setup= GPIO.setup(self.pin, GPIO.OUT) # using pins as a GPIO out pin
        
        self.pwm = GPIO.pwm(self.pin, self.freq) # create pwm signal
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
        
    
    def set_dc(self, dc_change):
        if dc_change
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
                

pins = [12, 13, 18]
a = gate(pin=12, dc=50, freq=6) 
b = gate(13, 50, 6)
c = gate(13, 50, 6)
gates = [a, b, c]

while True:
    print('''
    1 - begin
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
        for gate in gates:
            gate.begin()
            gate.add_delay()

    elif cmd == '2':
        for gate in gates:
            gate.stop()
    
    elif cmd == 'w':
        for gate in gates:
            gate.set_freq('inc')
            gate.add_delay()

    elif cmd == 's':
        for gate in gates:
            gate.set_freq('inc')
            gate.add_delay()

    elif cmd == 'a':
        for gate in gates:
            gate.set_freq('inc')
            gate.add_delay()
    
    elif cmd == 'd':
        for gate in gates:
            gate.set_freq('inc')
            gate.add_delay()
    
    elif cmd == '3':
        new_freq = float(input('new freq (Hz) 0.1 < f < 1000 : '))
        for gate in gates:
            gate.set_freq(new_freq)
            
    elif cmd == '4':
        new_dc = float(input('new dc (%) 0 < dc < 100: '))
        for gate in gates:
            gate.set_dc(new_dc)

    else:
        print('try again')

    
    

