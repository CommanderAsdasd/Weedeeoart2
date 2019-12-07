#!/usr/bin/env python3

from moviepy.editor import *
import pdb, sys
from weedeeo.helpers import *
from weedeeo.comprehensions import *


input_file = sys.argv[1]
clip = VideoFileClip(input_file)
# .subclip(0,50)


# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0.8)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')

# Say that you want it to appear 10s at the center of the screen
# txt_clip = txt_clip.set_pos('center').set_duration(10)

clip_count = 30
cutting_function = lambda counter, clip: clip.subclip(*random_sequence(1 * math.sin(random.uniform(counter-1,counter))*2, clip.duration))
clip = [ cutting_function(counter, clip) for counter, clip in enumerate([clip] * clip_count) ]

# To lambda there passed counter and clip, and called in list comprehension
# TODO: base more function on this random sequences
generating_function = comprehensions_set["speed_reversing"]
video = [ generating_function(count, clip)
            for count, clip in enumerate(clip)]
# pdb.set_trace()
video = concatenate_videoclips(video)
# video = CompositeVideoClip(clip)


# Write the result to a file (many options available !)
video.write_videofile("{}-{}.mp4".format(no_extension(input_file), file_timestamp()))