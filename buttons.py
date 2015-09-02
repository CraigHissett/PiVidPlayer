import RPi.GPIO as GPIO
import time

# set buttons to use Broadcom naming convention
GPIO.setmode(GPIO.BOARD)

# Set up the button pins, 3 banks of 3

LB1 = 8
LB2 = 10
LB3 = 12
RB1 = 11
RB2 = 13
RB3 = 15
CB1 = 19
CB2 = 21
CB3 = 23

pins = [LB1, LB2, LB3, RB1, RB2, RB3, CB1, CB2, CB3]
# Using internal pull up resistor; no need for one in circuit; other pin on buttons to ground

for pin in pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def pressed():
    while True:
        for pin in pins:
            input_state = GPIO.input(pin)
            if input_state == False:
                print pin
                return pin
            time.sleep(0.2)
 
# Add below line to reset all pin status on close       
GPIO.cleanup()

if __name__ == '__main__': 
   pressed() 


