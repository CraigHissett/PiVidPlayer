import pygame, sys, time
from pygame.locals import *
import buttons, playlists, player
player = None
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

def Main():
    load("StartScreen","")
    time.sleep(5)
    load("PressAnyKey","")
    while True:
        buttons.CheckForKeyPress()

if __name__ == '__main__':
    Main()
