import pygame, sys, time
from pygame.locals import *
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

def ShowStartScreen():
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Hello, Isaac!', True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 240)
    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
    time.sleep(5)

def DrawPressBtnMsg():
    fontObj = pygame.font.Font('freesansbold.ttf', 24)
    textSurfaceObj = fontObj.render('Press a button to play.', True, DARKGRAY)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 240)
    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
    
def Main():
    ShowStartScreen()
    DrawPressBtnMsg()
#    if CheckForKeyPress():
#        pygame.event.get() # clear event queue
#        return
    while True:
        CheckForKeyPress()

if __name__ == '__main__':
    Main()
