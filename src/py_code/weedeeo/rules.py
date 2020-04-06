from moviepy.editor import *
import pdb, sys
# import effects

def video_from_function(generating_function):
    video = [ generating_function(count, clip)
            for count, clip in enumerate(clip)]