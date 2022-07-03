

# luis arandas 02-07-2022

def onValueChange(channel, sampleIndex, val, prev):

    video_length = op('video_info')['length'] # gets the length of the video
    current_true_index = op('video_info')['true_index'] # where it is

    if (int(current_true_index) == int(video_length) - 1): # match 100 to 99
        print("video done")
        op('target').run() # run Text component as a result

    return