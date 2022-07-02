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

	length_val = op('length_of_audio')['sample_length0'] # gets the length of the channel
	
	if (val >= (length_val-0.2)):
		print("audio file finished!")
		op('audio_finish').panel.state = 1 # turn other button on to continue logic if needed
	return
	