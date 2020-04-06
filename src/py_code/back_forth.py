#!/usr/bin/env python3

from moviepy.editor import *
import pdb, sys
from weedeeo.helpers import *
import math
from weedeeo.effects import *
from weedeeo.rules import *
import moviepy.video.VideoClip


clips = []
max_size = [0,0]
for video_path in sys.argv[1:]:
    # clip = 
    # if max_size[0] < clip.w:
    #     max_size[0] = clip.w
    # if max_size[1] < clip.h:
    #     max_size[1] = clip.h
    # import ipdb; ipdb.set_trace()
    # clips.append(clip.resize(max_size[0],max_size[1]))
    clips.append(VideoFileClip(video_path))

uni = lambda low, up: random.uniform(low, up)
choice = lambda x: random.choice(x)

clip_count = 10
cutting_function = lambda counter, clip: clip.subclip(*random_sequence(choice([uni(0,2),uni(3,5),uni(0.01, 0.1)]), clip.duration))
clips_cut = [cutting_function(counter, clip) for counter, clip in enumerate(clips * clip_count) ]

class part():
    
    def __init__(cut_rule, clip_count=1):
        pass
        

# To generating_function - lambda
# TODO: base more function on this random sequences
generating_function = templates["sas_maker"]
# clips = list(map(sas_maker, enumerate(clips)))
clips_cut_fx = [ generating_function(counter, clip) for counter, clip in enumerate(clips_cut) ]
video = concatenate_videoclips(clips_cut_fx, method="compose")
video.write_videofile("./output/{}-{}.mp4".format(no_extension(sys.argv[1])+no_extension(sys.argv[2]), file_timestamp()))