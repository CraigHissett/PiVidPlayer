#This will be my main script, calling all defs from their individual py files.
#
#import standards
import sys, time

#import everything required from my python files:
import GUI, buttons, playlists

#import other requirements
from pyomxplayer import OMXPlayer 
from pprint import pprint 

#define any values required before we crack on!
#omx = OMXPlayer('/tmp/video.mp4') 

def Main():
  #Display 'Welcome screen', with no secondary text
  GUI.load("StartScreen","")
  time.sleep(5)
  #Configure playlists - update secondary text to update user 
  GUI.load("StartScreen", "Loading Playlists")
  playlists.refresh("All")
  GUI.load("StartScreen", "Playlists Loaded")
  time.sleep(1)
  #Display Message to indicate ready to go
  GUI.load("PressAnyKey","")
  #Start to monitor buttons
  while True:
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
  
    
    
if __name__ == '__main__': 
   Main() 
