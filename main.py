#This will be my main script, calling all defs from their individual py files.
#
#import standards
import sys, time
import RPi.GPIO as GPIO

#import everything required from my python files:
import GUI, buttons, playlists

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
    buttons.CheckForKeyPress()
    
if __name__ == '__main__': 
   Main() 
