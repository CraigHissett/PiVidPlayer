>>> from pyomxplayer import OMXPlayer
>>> from pprint import pprint
>>> omx = OMXPlayer('/tmp/video.mp4')
>>> pprint(omx.__dict__)
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
>>> omx.toggle_pause()
>>> omx.position
9.43
>>> omx.stop()

#read notes for ideas on how to change
