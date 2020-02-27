from moviepy.editor import *
import weedeeo
import sys
import time
import os

def invert_green_blue(image):
    return image[:,:,[0,2,1]]


my_clip = VideoFileClip(sys.argv[1])
my_clip_name = os.path.basename(sys.argv[1]).splitext()[0]
# my_clip.set_start(t=5) # does nothing, changes are lost
my_new_clip = my_clip.set_start(t=5) # good !
# breakpoint()
modifiedClip = my_clip.set_start(t=5).set_end(t=6).fl_image( invert_green_blue )
modifiedClip.write_videofile("{}_{}.mp4".format(my_clip_name, time.strftime("%I%M%S")))