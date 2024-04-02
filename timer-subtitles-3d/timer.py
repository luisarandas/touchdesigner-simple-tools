# luis arandas 26-08-2023
# timer for display, constant

import random

class RandomSentenceGenerator:
    def __init__(self):
        self.subjects = ["The cat", "A dog", "My friend", "The teacher", "A bird"]
        self.verbs = ["jumped", "sang", "ran", "slept", "danced"]
        self.objects = ["on the bed", "in the park", "with joy", "loudly", "gracefully"]
        self.names = ["Alex", "Jordan", "Sam", "Pat", "Taylor"]
        self.places = ["the museum", "the park", "the restaurant", "the beach", "the library"]

    def generate_sentences(self, count=15):
        sentences = []
        for _ in range(count):
            subject = random.choice(self.subjects)
            verb = random.choice(self.verbs)
            obj = random.choice(self.objects)
            sentence = f"{subject} {verb} {obj}."
            sentences.append(sentence)
        return sentences

    def generate_random_names(self, count=5):
        return [random.choice(self.names) for _ in range(count)]

    def generate_random_places(self, count=5):
        return [random.choice(self.places) for _ in range(count)]

    def generate_random_story(self):
        name = random.choice(self.names)
        place = random.choice(self.places)
        action = random.choice(self.verbs)
        reason = random.choice(self.objects)
        story = f"One day, {name} went to {place} to {action} {reason}. It was an unforgettable adventure."
        return story
    

# To populate the Table DAT with text data

def populate_DAT_table(use_stories=False):
    generator = RandomSentenceGenerator()
    if use_stories:
        content = [generator.generate_random_story() for _ in range(5)]  # Generate 5 random stories
        print_message = "Table populated with random stories."
    else:
        content = generator.generate_sentences()  # Generate random sentences
        print_message = "Table populated with random sentences."
    table = op('text_data')
    table.clear()
    for item in content:
        table.appendRow([item])
    print(print_message)


current_subtitle = 0

def onInitialize(timerop):
    global current_subtitle
    current_subtitle = 0
    populate_DAT_table(use_stories=True)
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
    # execute every 2 seconds
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

