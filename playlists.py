import os, subprocess, sys

FoundFolder = "J:\Films\Peppa Pig"

#for root, dirs, files in os.walk(r'FoundFolder'):
#    for file in files:
#        if file.endswith('.mp4'):


def ListDrives():
    print(os.listdir(FoundFolder))
    
def CompilePlaylist(PlaylistTitle):
    #Create a text file, step through folder and copy files into text file
    PlaylistText = open(PlaylistTitle + '.txt', "w")
    print(PlaylistTitle)
    #for root, dirs, files in os.walk(".", topdown=True):
    for root, dirs, files in os.walk(FoundFolder, topdown=True):
        for name in files:
            print(os.path.join(root, name))
            PlaylistText.write(os.path.join(root, name) + '\n')
        for name in dirs:
            print(os.path.join(root, name))
            PlaylistText.write(os.path.join(root, name) + '\n')
    PlaylistText.close()

#def LoadPlaylist(PlaylistTitle):
    #For the Selected Playlist loop through the text file and create a list
    #LoadedPlaylist = open(PlaylistTitle + '.txt', 'r')
    #print LoadedPlaylist.read()
    
def Main():
    ListDrives()
    CompilePlaylist('Peppa')

Main()
