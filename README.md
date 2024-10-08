## TouchDesigner simple algorithms and tools

A set of simple TouchDesigner projects with solutions for audiovisual work, tested on Windows 11 and RTX 3090/3070.


1)  **audio-mixer-fades**
    Trigger independent audio track fade in/out on button click, able to range, and master on/off (from 0-1).

2)  **audio-play-callback**
    Custom callback on sample length of an Audio Play CHOP to allow logic when audio files stop playing (trigger a panel when audio finishes).

3) **dir-mapper-2d-slider**
    Creates a GLSL grid map from the number of files within an input directory, 2D Slider file navigator.

4) **dir-watcher**
    Populate a Table DAT with arbitrary directory (files with sizes and last-modified, also hidden).

5) **extensions**
    Template for abstractions (e.g.) -> op('xyz').myFunction() wrapped within a Container object with GUI visibility.

6) **feedback-shape-saver**
    Simple primitive shape color feedback with Movie File Out TOP export (composite on transparent background).

7) **get-running-apps**
    Populate Table DAT with running processes, PID, session name and memory usage (like task manager, hides CMD).

8) **glsl1-barrel** 
    BarrelDistortion.frag shader on input video file, affects 4 corners.

9) **glsl2-pingpong** 
    Ping-Pong Delay shader, feedback 0-1 (using .vs file).

10) **info-getter**
    A Text DAT execution on video file finish, creates a callback from video info channel.

11) **link-two-containers**
    A simple Select CHOP operator showing widget on container A triggered on container B (same logic as "send" and "receive" in MaxMSP).

12) **midi-to-vst**
    Simple boolean logic to send onNoteOn() and onNoteOff() to arbitrary VST3s.

13) **open-apps**
    Launch .exe applications found in provided paths, e.g. "C:\\Program Files (x86)", threaded search from string input.

14) **resolume-xml-parser**
    Parse a Resolume XML file with mapping values into a Table DAT (composition example with 2 layers).

15) **subprocess**
    Execute a request from a file on the same folder deriving paths (hides CMD using opened TD session).

16) **tcp-io**
    Simple server to illustrate TCP io between TouchDesigner session DAT and CMD (start tcp_server.py first).

17) **timer-subtitles-3d**
    Reads randomly generated sentences from a Table DAT, works on timer and displays with geometry to texture.

18) **web-server-internal**
    Internal Web Server DAT with external communication such as `tcp-io` folder.


```
(only using standard libs for now)
$ python -m venv venv
$ .\venv\Scripts\activate
```


Related implementations:
1. https://github.com/luisarandas/touchdesigner-apc40mk2-midi
2. https://github.com/luisarandas/touchdesigner-ig20-iegeekcam

