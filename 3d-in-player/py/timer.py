

# luis arandas 29-07-2022
# timer for subtitles

# -------

# me is this DAT.
# timerop is the connected Timer CHOP.
# cycle is the cycle index.
# segment is the segment index.
# fraction is the time in fractional form.
#
# interrupt is True if the user initiated a premature
#	interrupt, False if a result of a normal timeout.
#
# onInitialize(): if return value > 0, it will be
#	called again after the returned number of frames.


# get the data loaded to the table in TouchDesigner
how_many_subtitles = op('data').numRows 
# only one column should be in the table
# text = op('data').text
column = 0
current_subtitle = 0

def onInitialize(timerop):
	# i think I can just reset here
	return 0

def onReady(timerop):
	return
	
def onStart(timerop):
	return
	
def onTimerPulse(timerop, segment):
	return

def whileTimerActive(timerop, segment, cycle, fraction):
	return

def onSegmentEnter(timerop, segment, interrupt):
	return
	
def onSegmentExit(timerop, segment, interrupt):
	return

def onCycleEndAlert(timerop, segment, cycle, alertSegment, alertDone, interrupt):
	return
	

def onCycle(timerop, segment, cycle):

    # execute every 2 seconds
    if (cycle % 2 == 0):    
        global column
        global current_subtitle

        subtitle_to_display = op('data')[current_subtitle, column]
        op('text2').par.text = subtitle_to_display

        if (current_subtitle <= (how_many_subtitles-2)): # need to check this indexing
            current_subtitle = current_subtitle + 1
        else:
            current_subtitle = 0
        
        print("count ", cycle)
    return

def onDone(timerop, segment, interrupt):
	return
