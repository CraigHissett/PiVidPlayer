# PiVidPlayer
Raspberry Pi-based, Python-powered video player

Code Spec: To monitor 9 Arcade buttons to control playing and skipping videos and playlist selection.

To Address:

1) Video Playing

  TogglePlay - Play/Pause video
  
  StopVid - Go back to beginning and pause video
  
  PrevVid - Select previous video from playlist
  
  NextVid - Select next video from playlist
  
  Playlist(x) - Clear current playlist, load selected, cue first video (if video was playing when pressed then play video1; if it was paused then do not play
  
  
2) Creating Playlists

  Playlists.py now compiles all playlists (based on search criteria in a text file called 'PlaylistDefs.txt').
  It searches all drives for files containing the playlist name (ie Peppa Pig) and dumps their location to a playlist file (Peppa Pig.txt for instance).
  To Do - Convert to a class, pass playlist contents to player.py when done.
  
3) ButtonPresses

  Monitor Buttons, debouncing, measuring whether pressed/held, combination presses
  
  Run related function for that sequence
  
  List sequences here, and the press and hold functions:
  
    Button1 (Playlist 1)            Load Playlist1, Vid1 - Load Playlist 1, Random
    
    Button2 (Playlist 2)            Load Playlist2, Vid2 - Load Playlist 2, Random
    
    Button3 (Playlist 3)            Load Playlist3, Vid3 - Load Playlist 3, Random
    
    Button4 (Playlist 4)            Load Playlist4, Vid4 - Load Playlist 4, Random
    
    Button5 (Playlist 5)            Load Playlist5, Vid5 - Load Playlist 5, Random
    
    Button6 (Playlist 6)            Load Playlist6, Vid6 - Load Playlist 6, Random
    
    Button7 (Previous Button)       PrevVid - Rwd
    
    Button8 (Play/Pause Button)     TogglePlay - StopVid
    
    Button9 (Next Button)           NextVid - FFwd
    
                                    UpdatePlaylists
                                    
                                    
4) GUI

  WelcomeScreen - display a splash screen while loading playlists
  
  PlaylistMenu - to consider. Possibly load small icons to represent playlists rather than har coding.
  
  Settings - Menu for configuring timers and other parental features
  
  ModeSelect - Mode1 will be the video player. Look to expand use of the project with more modes.
  
