import RPi.GPIO as GPIO
import time

# set buttons to use Broadcom naming convention
GPIO.setmode(GPIO.BCM)

# Set up the button pins, 3 banks of 3

LB1 = 14    # Actual pin 8 
LB2 = 15    # Actual pin 10
LB3 = 18    # Actual pin 12
RB1 = 17    # Actual pin 11
RB2 = 21    # Actual pin 13
RB3 = 22    # Actual pin 15
CB1 = 10    # Actual pin 19
CB2 = 9    # Actual pin 21
CB3 = 11    # Actual pin 13

pins = [LB1, LB2, LB3, RB1, RB2, RB3, CB1, CB2, CB3]
# Using internal pull up resistor; no need for one in circuit; other pin on buttons to ground

for pin in pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    for pin in pins:
        input_state = GPIO.input(pin)
        if input_state == False:
            print('Button ' & pin & ' Pressed')
            time.sleep(0.2)
 
# Add below line to reset all pin status on close       
#GPIO.cleanup()
