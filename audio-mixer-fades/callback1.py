def onOffToOn(channel, sampleIndex, val, prev):
	op('mixer').par.gain = 1
	return

def onValueChange(channel, sampleIndex, val, prev):
	return