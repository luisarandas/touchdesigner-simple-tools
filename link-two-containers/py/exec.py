

# luis arandas 03-07-2022

def onValueChange(channel, sampleIndex, val, prev):
	value = int(val)
	print('[-] this is toggled from container1', value)
	if value == 1:
		op('/project1/container2/movie').par.reload = 1
		op('/project1/container2/movie').par.play = 1
	else:
		op('/project1/container2/movie').par.reload = 0
		op('/project1/container2/movie').par.play = 0
	return
