#This will be my main script, calling all defs from their individual py files.
#
#import standards
import sys, time

#import everything required from my python files:
import GUI, import, playlists

#import other requirements
from pyomxplayer import OMXPlayer 
from pprint import pprint 

#define any values requred before we crack on!
omx = OMXPlayer('/tmp/video.mp4') 

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


if __name__ == '__main__': 
   Main() 
