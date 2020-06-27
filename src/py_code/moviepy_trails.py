#!/usr/bin/env pipenv-shebang

from moviepy.editor import *
import datetime
from weedeeo.classes_hijack import *
import weedeeo.helpers
import moviepy.video.fx.all
import random

def visual_trail(frame):
    # print(get_frame(t), t)
    frame.resize(int(frame.shape[0]*0.99),int(frame.shape[1]*0.99))
    return frame 

# def scroll(get_frage

resize_exp = [lambda t : 1/(t+1),lambda t : random.randint(t)+1]
clip = VideoFileClip(sys.argv[1]).random_sequence(0.3, 5, stutter=True).fl_image(visual_trail)
# images = [0,0]
# i = 0

# modifiedClip = clip.fli_image()
# modifiedClip = clip.fl_image(
video = CompositeVideoClip([clip])
video.write_videofile(f"../../output/{sys.argv[0]}_{weedeeo.helpers.file_timestamp()}.mp4")