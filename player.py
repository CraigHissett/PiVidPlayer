#Class for OMX player

class Player:
    def __init__(self, playlist_file, autoplay=True):
        with open(playlist_file) as f:
            self.playlist = [line.strip() for line in f]
        self.cur_pos = 0
        self._omx = None

    @property
     def current_file(self):
         return self.playlist[self.cur_pos]

     def play(self):
         if self._omx is None:
             self._omx = OMXPlayer(self.current_file)
         elif self._omx.paused:
             self._omx.toggle_pause()

    def stop(self):
        if self._omx is not None:
            self._omx.stop()
            self._omx = None

    def next(self):
        self.stop()
        # We don't want to seek past the end of the playlist.
        # Alternatively, you could add an 'else' clause that resets
        # self.cur_pos = 0 to wrap the playlist around
        if self.cur_pos < len(self.playlist)-1:
            self.cur_pos += 1
            self.play()

    def prev(self):
         # Don't go back before the beginning of the playlist
         # You could also implement something like in `next()` and loop
         # to the end of the playlist. That would be self.cur_pos = len(self.playlist)-1
         self.cur_pos = max(0, self.cur_pos - 1)
