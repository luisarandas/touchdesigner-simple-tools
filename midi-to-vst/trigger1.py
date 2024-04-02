

# luis arandas 03-07-2022

notes_send = []

def onOffToOn(channel, sampleIndex, val, prev):
    print("note on")
    op('vst').sendNoteOn(1, 80, 127)
    return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
    #op('vst').sendNoteOff(1, 60, 0)
    print("note off")
    op('vst').sendNoteOff(1, 80, 0)
    return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
	