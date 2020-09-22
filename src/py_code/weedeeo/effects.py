from moviepy.editor import *
from weedeeo.helpers import *
import math
import random
from moviepy.video.tools.segmenting import findObjects
from moviepy.video.fx.all import *

templates = {}

def scroll(get_frame, t):
    """
    This function returns a 'region' of the current frame.
    The position of this region depends on the time.
    """
    frame = get_frame(t)
    frame_region = frame[int(t):int(t)*int(t),:]
    return frame_region

def speedx_sync(clip, speed):

    new_clip = clip.fx(vfx.speedx, speed)
    # ratio = clip.audio.duration / clip.duration
    new_audio = clip.audio.fx(vfx.speedx, speed)
    new_clip = new_clip.set_audio(new_audio)
    return new_clip

def color_channel_shuffle(clip, order):
    return clip.fl_image(lambda image: image[:,:,order])

def mirror(clip):
    return vfx.time_mirror(clip)

def tf_test(clip):
    image[:,:,[0,2,1]]
    
    return clip.fl_image(lambda image: image[:,:,[0,2,1]])

def draw_circles(clip):
    import numpy as np
    import scipy.misc as misc
    from scipy import ndimage

    def draw_circle(frame):
        f = misc.face(gray=True)
        sx, sy = f.shape
        X, Y = np.ogrid[0:sx, 0:sy]


        r = np.hypot(X - sx/2, Y - sy/2)
        rbin = (20* r/r.max()).astype(np.int)
        radial_mean = ndimage.mean(f, labels=rbin, index=np.arange(1, rbin.max() +1))
        print(radial_mean.reshape(frame.shape))
        return radial_mean

    return clip.fl_image(draw_circle)

def panoram(clips):
    clips_out = clips
    for i, clip in enumerate(clips):
        # print(clips)
        clip = clip.resize(1/2)
        clips_out.append(CompositeVideoClip([clip,clip,clip,clip]))
    return clips_out

def resize_func(t):
    # if t < 4:
    #     return 1 + 0.2*t  # Zoom-in.
    # elif 4 <= t <= 6:
    #     return 1 + 0.2*4  # Stay.
    # else: # 6 < t
    #     return 1 + 0.2*(duration-t)  # Zoom-out.
    return 


passed_function = lambda count, clip, function="tf_test" : function(clip)

sas_maker = lambda count, clip : mirror(clip) if count % choice([2,1,3]) == 0 else \
                                (color_channel_shuffle(clip, choice([[0,1,2],[0,2,1]]))) if count % choice([2,1,3]) == 0 else \
                                (clip if count % choice([2,1,3]) == 0 else speedx_sync(clip,choice([2,1,3])))


speed_reversing = lambda count, clip : speedx_sync(clip, 0.9) \
                        if count % 2 == 0 else \
                        (clip.fl(scroll).fx(vfx.reverse) \
                        if count % 3 == 0 \
                        else speedx_sync( clip, 2))

vanilla = lambda count, clip : clip.fx(vfx.time_mirror) \
                        if count % 4 == 0 \
                        else (concatenate_videoclips([mirror_x(speedx_sync(clip, random.uniform(0.8,1.4))) if i % 2 == 0 and clip.duration < 1 else clip for i in range(random.randint(1,10))]) \
                            if count % 3 == 0 and clip.duration < 1 \
                            else concatenate_videoclips([mirror_y(clip) if i % 2 == 0 else clip for i in range(random.randint(1,5))]))


zoom = lambda count, clip: clip

stutter = lambda length, clip: clip

templates["speed_reversing"] = speed_reversing
templates["sas_maker"] = sas_maker
templates["vanilla"] = vanilla
templates["zoom"] = zoom