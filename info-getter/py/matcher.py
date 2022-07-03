# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):

    video_length = op('video_info')['length'] # gets the length of the video
    current_true_index = op('video_info')['true_index'] # where it is

    if (int(current_true_index) == int(video_length) - 1): # match 100 to 99
        print("video done")
        op('target').run() # run Text component as a result

    return