# motor-controller

## Activating Raspberry Pi:
1. Connect a keyboard and mouse to it
2. Connect the HDMI cable
3. Connect power cable - the screen should show that it is on
4. If step 3 doesn't work, remove all cables, take out memory card and put it back it. And repeat 1 -3.

## Prepare Raspberry Pi for ESC:
![image](https://user-images.githubusercontent.com/66765258/159859363-cb2fc7d4-db14-47d5-8dcf-b5d654f29725.png)
1. Connect GPIO4 to the Yellow female plug of ESC (signal wire)
2. Connect GND to the Brown female plug of the ESC (ground)

## Download Pigs
'sudo apt-get update
sudo apt-get install pigpio python-pigpio python3-pigpio'

## Running Code for Raspberry Pi:
1. motor-controller -> baby_motor.py
3. Change the duty cycle and frequency as required (I have set them as per a sample code I found online, but we might need to change it) 
4. Might want to try keeping the duty cycle at 100 (100%) and lowering the frequency to make sure that there is current flowing into the motor by feeling wheter the rotor is experiencing any forces or with a multimeter. This should turn the system to a single-phase DC supply.
5. Adjust the countdown as required
6. Connect the power supply to ESC (based on tests, the motor needs around 11V through it to have a noticable effect.
7. Run code
