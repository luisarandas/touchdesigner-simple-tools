

# luis arandas 31-07-2022
# automate making simple shapes navigating in a color background and export

# run this script to start the variables
op('background').par.resolutionw = 512 # setting up for rtx3070 small generation
op('background').par.resolutionh = 288
op('circle').par.resolutionw = 512
op('circle').par.resolutionh = 288
op('rectangle').par.resolutionw = 512
op('rectangle').par.resolutionh = 288
op('rectangle').par.sizex = 0.3
op('rectangle').par.sizey = 0.2
op('rectangle').par.sizeunit = 2

op('background').par.colorr = 0 # just setup the background color
op('background').par.colorg = 0.5
op('background').par.colorb = 0.4

op('circle').par.fillcolorr = 0 # just setup the shape color
op('circle').par.fillcolorr = 0
op('circle').par.fillcolorr = 0
op('circle').par.bgalpha = 0 