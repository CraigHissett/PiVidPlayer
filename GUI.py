import pygame, sys, time
from pygame.locals import *
import buttons, playlists
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 480))
pygame.display.set_caption('PiVidPlayer')

#Colours setup
#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

def load(ScreenName, ScreenText):
    if ScreenName == "StartScreen":
        fontObj1 = pygame.font.Font('freesansbold.ttf', 42)
        fontObj2 = pygame.font.Font('freesansbold.ttf', 12)
        textSurfaceObj1 = fontObj1.render('Hello, Isaac!', True, GREEN, BLACK)
        textSurfaceObj2 = fontObj2.render(ScreenText, True, GREEN, BLACK)
        textRectObj1 = textSurfaceObj1.get_rect()
        textRectObj2 = textSurfaceObj2.get_rect()
        textRectObj1.center = (400, 240)
        textRectObj2.center = (500, 240)
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
        DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
        pygame.display.update()
    elif ScreenName == "PressAnyKey":
        fontObj1 = pygame.font.Font('freesansbold.ttf', 24)
        fontObj2 = pygame.font.Font('freesansbold.ttf', 12)
        textSurfaceObj1 = fontObj1.render('Press a button to play.', True, DARKGRAY)
        textSurfaceObj2 = fontObj2.render(ScreenText, True, DARKGRAY)
        textRectObj1 = textSurfaceObj1.get_rect()
        textRectObj2 = textSurfaceObj2.get_rect()
        textRectObj1.center = (400, 240)
        textRectObj2.center = (500, 240)
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
        DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
        pygame.display.update()

def CheckForKeyPress():
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
    if buttons.pressed==0
      #Do nothing
      return
    elif buttons.pressed==LB1
      #Select Playlist1, Load video 1
      playlists.play("Peppa.txt", 1)
    elif buttons.pressed==LB2
      #Select Playlist2
      playlists.play("Barney.txt", 1)
    elif buttons.pressed==LB3
      #Select Playlist3
      playlists.play("Minions.txt", 1)
    elif buttons.pressed==RB1
      #Select Playlist1, Load video 1
      playlists.play("Peppa.txt", 1)
    elif buttons.pressed==RB2
      #Select Playlist2
      playlists.play("Barney.txt", 1)
    elif buttons.pressed==RB3
      #Select Playlist3
      playlists.play("Minions.txt", 1)
    elif buttons.pressed==CB1  
      #Select previous video
      playlists.skip(-1)
    elif buttons.pressed==CB2
      #Play/Pause
      playlists.playpause()
      return
    elif buttons.pressed==CB3
      #Select next video
      playlists.skip(+1)
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


def Main():
    load("StartScreen","")
    time.sleep(5)
    load("PressAnyKey","")
    while True:
        CheckForKeyPress()

if __name__ == '__main__':
    Main()
