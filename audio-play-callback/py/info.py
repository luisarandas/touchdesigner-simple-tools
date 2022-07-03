

# luis arandas 02-07-2022

def onValueChange(channel, sampleIndex, val, prev):

	length_val = op('length_of_audio')['sample_length0'] # gets the length of the channel
	
	if (val >= (length_val-0.2)):
		print("audio file finished!")
		op('audio_finish').panel.state = 1 # turn other button on to continue logic if needed
	return
	