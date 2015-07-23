import RPi.GPIO as GPIO
import time

# set buttons to use Broadcom naming convention
GPIO.setmode(GPIO.BCM)

# Set up the 9 required button pins
# Using internal pull up resistor; no need for one in circuit
# other pin on buttons to ground
# pins to use
# BCM 14,15 18 - pins 8, 10, 12
# BCM 17, 21, 22 - pins 11, 13, 15
# BCM 10, 9, 11 - pins 19, 21, 13

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
