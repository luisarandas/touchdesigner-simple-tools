

# luis arandas 18-07-2022
# setting up global mixer values

# volume1 ... volumex = channels of the mixer
# no work has been done on the db scale

op('audiofilein1').par.play = 1
op('audiofilein2').par.play = 1

# [fromrange1, fromrange2], [torange1, torange2]
op('volume1').par.torange1 = 0 # try 0.3
op('volume2').par.torange1 = 0 # try 0.3

# setup out volume
op('out').par.volume = 1
