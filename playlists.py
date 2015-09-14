import os, subprocess, sys, string, platform, time
from pyomxplayer import OMXPlayer
from pprint import pprint

def refresh(playlist):
    #define sequence for geting started
    if playlist=="All":
        FindPlaylistNames()
    
def FindPlaylistNames():
    PlaylistNames = open("PlaylistDefs.txt", 'r')
    for PlaylistTitle in PlaylistNames.readlines():
        PlaylistTitle = PlaylistTitle.strip()
        print(PlaylistTitle + " searching...")
        SearchDrives(PlaylistTitle)
        print(PlaylistTitle + " complete")

def SearchDrives(PlaylistTitle):
    #Create a text file, step through folder and copy file locations into text file
    PlaylistText = open(PlaylistTitle + '.txt', "w")
    if platform.system == "Windows":
        from ctypes import windll
        bitmask = windll.kernel32.GetLogicalDrives()
        for DriveLetter in string.ascii_uppercase:
            if bitmask & 1:
                for root, dirs, files in os.walk(DriveLetter +':', topdown=True):
                    for name in files:
                        if PlaylistTitle in name:
                            #Finds Playlist Name in Filename
                            print(os.path.join(root, name))
                            #if file.endswith('.mp4'):
                            PlaylistText.write(os.path.join(root, name) + '\n')
                    for name in dirs:
                        if PlaylistTitle in name:
                            print(os.path.join(root, name))
                            #PlaylistText.write(os.path.join(root, name) + '\n')
            bitmask >>= 1
    elif platform.system == "Linux":
        for root, dirs, files in os.walk('/home/pi', topdown=True):
            for name in files:
                if PlaylistTitle in name:
                    #Finds Playlist Name in Filename
                    print(os.path.join(root, name))
                    #if file.endswith('.mp4'):
                    PlaylistText.write(os.path.join(root, name) + '\n')
            for name in dirs:
                if PlaylistTitle in name:
                    print(os.path.join(root, name))
                    #PlaylistText.write(os.path.join(root, name) + '\n')
        for root, dirs, files in os.walk('/media', topdown=True):
            for name in files:
                if PlaylistTitle in name:
                    #Finds Playlist Name in Filename
                    print(os.path.join(root, name))
                    #if file.endswith('.mp4'):
                    PlaylistText.write(os.path.join(root, name) + '\n')
            for name in dirs:
                if PlaylistTitle in name:
                    print(os.path.join(root, name))
                    #PlaylistText.write(os.path.join(root, name) + '\n')

    PlaylistText.close()


if __name__ == '__main__':
    refresh("All")
