## touchdesigner simple algorithms and tools

A set of simple TouchDesigner projects with solutions for audiovisual work, tested on Windows 11 and RTX 3090/3070.


1)  **audio-mixer-fades**
    Trigger independent audio track fade in/out on button click, able to range, and master on/off (from 0-1).
2)  **audio-play-callback**
    Custom callback on sample length of an Audio Play CHOP to allow logic when audio files stop playing (trigger a panel when audio finishes).
3) **dir-watcher**
    Populate a Table DAT with arbitrary directory (files with sizes and last-modified, also hidden).
4) **extensions**
    Template for abstractions (e.g.) -> op('xyz').myFunction() wrapped within a Container object with GUI visibility.
5) **feedback-shape-saver**
    Simple primitive shape color feedback with Movie File Out TOP export (composite on transparent background).
6) **get-running-apps**
    Populate Table DAT with running processes, PID, session name and memory usage (like task manager, hides CMD).
5) **info-getter**
    A Text DAT execution on video file finish, creates a callback from video info channel.
6) **link-two-containers**
    A simple Select CHOP operator showing widget on container A triggered on container B (same logic as "send" and "receive" in MaxMSP).
7) **midi-to-vst**
    Simple boolean logic to send onNoteOn() and onNoteOff() to arbitrary VST3s.
8) **subprocess**
    Execute a request from a file on the same folder deriving paths (hides CMD using opened TD session).
9) **tcp-io**
    Simple server to illustrate TCP io between TouchDesigner session DAT and CMD (start tcp_server.py first).
10) **timer-subtitles-3d**
    Reads randomly generated sentences from a Table DAT, works on timer and displays with geometry to texture.
11) **web-server-internal**
    Internal Web Server DAT with external communication such as `tcp-io` folder.

```
(only using standard libs for now)
$ python -m venv venv
$ .\venv\Scripts\activate
```

