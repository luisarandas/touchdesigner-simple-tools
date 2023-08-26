

# luis arandas 26-08-2023
# timer for display, constant

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

# -------

import random

def generate_random_sentences():
    # Lists of subjects, verbs, and objects
    subjects = ["The cat", "A dog", "My friend", "The teacher", "A bird"]
    verbs = ["jumped", "sang", "ran", "slept", "danced"]
    objects = ["on the bed", "in the park", "with joy", "loudly", "gracefully"]

    sentences = []

    # Generate 15 random sentences
    for _ in range(15):
        subject = random.choice(subjects)
        verb = random.choice(verbs)
        obj = random.choice(objects)
        sentence = f"{subject} {verb} {obj}."
        sentences.append(sentence)

    return sentences


def populate_DAT_table():
    sentences = generate_random_sentences()
    table = op('text_data')
    
    # Clear the table and populate with new sentences
    table.clear()
    for sentence in sentences:
        table.appendRow([sentence])
    print("supposedly populated")


current_subtitle = 0

def onInitialize(timerop):
    global current_subtitle
    current_subtitle = 0
    populate_DAT_table()
    return

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
    # execute ecevery 2 seconds
    if cycle % 2 == 0:
        global current_subtitle
        
        # Getting the number of subtitles and the subtitle data
        how_many_subtitles = op('text_data').numRows
        subtitle_to_display = op('text_data')[current_subtitle, 0]  # Since column is always 0
        op('subtitles').par.text = subtitle_to_display
	
        # Cycle through subtitles
        current_subtitle = (current_subtitle + 1) % how_many_subtitles
        print("count ", cycle)
	
    return

def onDone(timerop, segment, interrupt):
	return
