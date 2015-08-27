import os, subprocess, sys, string, platform
from pyomxplayer import OMXPlayer
from pprint import pprint

def refresh(playlist):
    'define sequence for geting started
    if playlist=="All"
        FindPlaylistNames()
    
def play(SelectedPlaylist, PlayNo):
    #Set up the OMX player code here
    PL = open(SelectedPlaylist, "rw+")
    video = PL.readline(PlayNo)
    omx = OMXPlayer(video)
    pprint(omx.__dict__)
    {'_position_thread': <Thread(Thread-5, started 1089234032)>,
    '_process': <pexpect.spawn object at 0x1a435d0>,
    'audio': {'bps': 16,
            'channels': 2,
            'decoder': 'mp3',
            'rate': 48000,
            'streams': 1},
    'chapters': 0,
    'current_audio_stream': 1,
    'current_volume': 0.0,
    'paused': True,
    'position': 0.0,
    'subtitles': 0,
    'subtitles_visible': False,
    'video': {'decoder': 'omx-mpeg4',
            'dimensions': (640, 272),
            'fps': 23.976025,
            'profile': 15,
            'streams': 1}}
    omx.toggle_pause()
    #omx.position
    #9.43
    omx.stop()    
    
def skip(Skip):
    #read open text file
    #add/subtract Skip o current line number being read

def playpause():
    #Still a toggle playpause in

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
    if platform.system == "Windows"
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
    elif platform.system == "Linux"
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
    refresh()
