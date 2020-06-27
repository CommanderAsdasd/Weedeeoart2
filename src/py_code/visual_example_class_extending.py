#!/usr/bin/env pipenv-shebang

# Import everything needed to edit video clips
from moviepy.editor import *
import ipdb
import random
import datetime
from classes_hijack import *
# from scipy import ndimage
# from scipy import misc
# f = misc.face()
# misc.imsave('face.png', f) # uses the Image module (PIL)

# import matplotlib.pyplot as plt
# plt.imshow(f)
# plt.show()



clip = VideoFileClip(sys.argv[1]).random_sequence(2).random_sequence(1)

# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0.8)

# Generate a text clip. You can customize the font, color, etc.
# breakpoint()
# txt_clip = TextClip("My Holidays 2013",fontsize=70,color='white').list('font')

# Say that you want it to appear 10s at the center of the screen
# txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip on the first video clip
images = [0,0]
i = 0


def invert_green_blue(get_frame, t):
    image = get_frame(t)
    global i
    gap = 1
    if i > gap:
        try:
            im_out = ((random.choice(images)[:,:,(0,1,2)] // t * t) - image[:,:,(0,1,2)]  // t * t)
        except Exception:
            im_out = images[i-gap] - image[:,:,(0,1,2)]
    else:
        i += 1
        # im_out = random.randint(0,255) - image[:,:,(0,1,2)]
        im_out = image[:,:,(0,1,2)]
    images.append(im_out)
    # im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)
    # im_out = image[255,200:250,:].min()
    # ipdb.set_trace()
    return im_out

# def scroll(get_frame, t):
#     """
#     This function returns a 'region' of the current frame.
#     The position of this region depends on the time.
#     """
#     frame = get_frame(t)
#     global i
#     gap = 1
#     if i > gap:
#         try:
#             frame_region = (random.choice(images)[:,:,(0,1,2)] // 32 * 32) - frame[:,:,(0,1,2)][int(t):int(t)+360,:]  // 32 * 32
#         except Exception:
#             frame_region = frame[int(t):int(t)+360,:]
#     else:
#         frame_region = frame[int(t):int(t)+360,:]
#     return frame_region

def scroll(get_frame, t):
    """
    This function returns a 'region' of the current frame.
    The position of this region depends on the time.
    """
    frame = get_frame(t)
    frame_region = frame[int(t):int(t)+360,:]
    return frame_region

modifiedClip = clip.fl( invert_green_blue )
# modifiedClip = clip.fl( scroll )
# modifiedClip = clip.fl( scroll )

video = CompositeVideoClip([modifiedClip])

# Write the result to a file (many options available !)
video.write_videofile(f"../../output/myHolidays_edited{datetime.datetime.now().timestamp()}.mp4")