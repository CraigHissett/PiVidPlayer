import os, subprocess, sys, string
from ctypes import windll

PlaylistTitle = "Peppa Pig"

def DriveList():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
            SearchDrive(PlaylistTitle, letter +':')
        bitmask >>= 1
    #return drives    

def SearchDrive(PlaylistTitle, DriveLetter):
    #Create a text file, step through folder and copy file locations into text file
    PlaylistText = open(PlaylistTitle + '.txt', "w")
    #print(PlaylistTitle)
    print(DriveLetter)
    for root, dirs, files in os.walk(DriveLetter, topdown=True):
        for name in files:
            if PlaylistTitle in name:
                print(os.path.join(root, name))
                #if file.endswith('.mp4'):
                PlaylistText.write(os.path.join(root, name) + '\n')
        for name in dirs:
            #if PlaylistTitle in name:
            print(os.path.join(root, name))
    PlaylistText.close()

#def LoadPlaylist(PlaylistTitle):
    #For the Selected Playlist loop through the text file and create a list
    #LoadedPlaylist = open(PlaylistTitle + '.txt', 'r')
    #print LoadedPlaylist.read()
    #PlayListText.read().split('\n')
    
def Main():
    DriveList()
    
#if __name__ == '__main__':

Main()
