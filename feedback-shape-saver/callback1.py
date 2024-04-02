def onOffToOn(channel, sampleIndex, val, prev):
	op('moviefileout1').par.file = "random_shape.mp4"
	op('moviefileout1').par.record = 1
	return

def onOnToOff(channel, sampleIndex, val, prev):
	op('moviefileout1').par.record = 0
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
	