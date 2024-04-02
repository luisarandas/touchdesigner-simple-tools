
# luis arandas 31-07-2022
# Simple primitive feedback and Movie File Out

# Resolutions

op('background').par.resolutionw = 1920 # setting up for rtx3070 small generation
op('background').par.resolutionh = 1080
op('circle').par.resolutionw = 1920
op('circle').par.resolutionh = 1080

# Circle to white and transparent background

op('circle').par.fillcolorr = 0 
op('circle').par.fillcolorg = 0
op('circle').par.fillcolorb = 0
op('circle').par.bgalpha = 0 

# Setup shape color
op('shape_color').par.colorr = 0.498
op('shape_color').par.colorr = 0.592
op('shape_color').par.colorb = 1

# Setup background color

op('background').par.colorr = 0
op('background').par.colorg = 1
op('background').par.colorb = 0.725

