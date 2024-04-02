

# luis arandas 03-07-2022

def onValueChange(channel, sampleIndex, val, prev):
    value = int(val)
    print('[-] this is toggled from container1', value)
    if value == 1:
        # When toggled on, reload and play the movie, and reset the level to normal
        op('/project1/container2/movie').par.reloadpulse.pulse()
        op('/project1/container2/movie').par.play = 1
        op('/project1/container2/level1').par.brightness1 = 1  # Ensure normal video display
    else:
        # When toggled off, stop the movie and adjust the level to make the video output black
        op('/project1/container2/movie').par.play = 0
        op('/project1/container2/level1').par.brightness1 = 0  # Make the video display black

    return
