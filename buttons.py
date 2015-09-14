import RPi.GPIO as GPIO
import pygame, sys, time
import player

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
                #print(pin)
                print pin
                return pin
            time.sleep(0.2)

def CheckForKeyPress():
    global player
    #Escape button on keyboard closes, for debug purposes
    #The For event below to be edited to capture GPIO buttons
    #explore setting up buttons.py as defs to be called and a value returned etc?
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key
    if pressed==0:
      #Do nothing
      return
    elif pressed==LB1:
      #Select Playlist1, Load video 1
      player = player.Player("Peppa.txt")
    elif pressed==LB2:
      #Select Playlist2
      player = player.Player("Barney.txt")
    elif pressed==LB3:
      #Select Playlist3
      player = player.Player("Minions.txt")
    elif pressed==RB1:
      #Select Playlist1, Load video 1
      player = player.Player("Peppa.txt")
    elif pressed==RB2:
      #Select Playlist2
      player = player.Player("Barney.txt")
    elif pressed==RB3:
      #Select Playlist3
      player = player.Player("Minions.txt")
    elif pressed==CB1: 
      #Select previous video
      player.Player.prev()
    elif pressed==CB2:
      #Play/Pause
      player.Player.Play()
      return
    elif pressed==CB3:
      #Select next video
      player.Player.Next()

#   Further events handling - to be integrated
#Look for mouse functions too - use touch screen for input!
#    for event in pygame.event.get(): 
#        if event.type == QUIT:
#            terminate()
#        elif event.type == KEYDOWN:
#            if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
#                direction = LEFT
#            elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
#                direction = RIGHT
#            elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
#                direction = UP
#            elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
#                direction = DOWN
#            elif event.key == K_ESCAPE:
#                terminate()

def terminate():
    pygame.quit()
    sys.exit()
 
# Add below line to reset all pin status on close       
GPIO.cleanup()

if __name__ == '__main__': 
   pressed() 


