#This will be my main script, calling all defs from their individual py files.
#
#import standards
import sys, time

#import everything required from my python files:
import GUI, import, playlists

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
  GUI.load("PressAnyKey")
  #Start to monitor buttons
  while True:
    if buttons.pressed==0
      #Do nothing
      return
    elif buttons.pressed==LB1
      #Select Playlist1, Load video 1
      playlist="Peppa.txt"
      omx=OMXPlayer(playlist.select(playlist, 1))
    elif buttons.pressed==LB2
      #Select Playlist2
      playlist="Barney.txt"
      omx=OMXPlayer(playlist.select(playlist, 1))
    elif buttons.pressed==LB3
      #Select Playlist3
      playlist="Minions.txt"
      omx=OMXPlayer(playlist.select(playlist, 1))     
    elif buttons.pressed==RB1
      #Select Playlist1, Load video 1
      playlist="Peppa.txt"
      omx=OMXPlayer(playlist.select(playlist, 1))
    elif buttons.pressed==RB2
      #Select Playlist2
      playlist="Barney.txt"
      omx=OMXPlayer(playlist.select(playlist, 1))
    elif buttons.pressed==RB3
      #Select Playlist3
      playlist="Minions.txt"
      omx=OMXPlayer(playlist.select(playlist, 1))
    elif buttons.pressed==CB1
      #Select previous video
      omx=OMXPlayer(playlist.select(playlist, -1))
    elif buttons.pressed==CB1
      #Play/Pause
      omx.toggle_pause()
      return
    elif buttons.pressed==CB3
      #Select next video
      omx=OMXPlayer(playlist.select(playlist, +1))
    
    
    
if __name__ == '__main__': 
   Main() 
