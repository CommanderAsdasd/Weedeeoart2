
# Import everything needed to edit video clips
 # -*- coding: utf-8 -*-

from moviepy.editor import *
import moviepy.video.fx.all as mpfx
import sys, random, time
import ipdb
import glob
import os

def invert_green_blue(image):
    # ipdb.set_trace()
    return image[:,:,:]
# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clipOut = []



# for times in range(10):
# with open() 
path_mp4 = glob.glob('{}*mp4'.format(sys.argv[1]))
# path_avi = 'sys.argv[1]{}'.format(glob.glob('*avi'))

# for path in paths

for clip in path_mp4[::10]:
    wed_len = random.uniform(0.4,1)
    clip = VideoFileClip(os.path.realpath(clip))
    start = random.uniform(0,int(clip.duration))
    end = start + wed_len
    while end > clip.duration:
        end = clip.duration - (start + wed_len)
    try:
        clip = clip.subclip(start,end)
    except OSError as OSe:
        print(OSe) 
    clipOut.append(clip)

for i in range(6):
    clipOut.append(random.choice(clipOut).fl_image(invert_green_blue))
    clipOut.append(mpfx.time_mirror(random.choice(clipOut)))
    random.shuffle(clipOut)



# modifiedClip = my_clip.fl_image( invert_green_blue )

# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0.8)

# Generate a text clip. You can customize the font, color, etc.
# txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white')

# Say that you want it to appear 10s at the center of the screen
# txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([concatenate_videoclips(clipOut)])

# Write the result to a file (many options available !)
date = time.strftime("%I%M%S")
video.write_videofile("output/weedeeo_output{}.mp4".format(date))