from moviepy.editor import *
import math

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
    # breakpoint()
    new_audio = clip.audio.fx(vfx.speedx, speed)
    new_clip = new_clip.set_audio(new_audio)
    return new_clip

def invert_green_blue(clip):
    # return clip
    return clip.fl_image(lambda image: image[:,:,[0,1,2]])

def mirror(clip):
    print("activated")
    return vfx.time_mirror(clip)

def tf_test(clip):
    image[:,:,[0,2,1]]
    
    return clip.fl_image(lambda image: image[:,:,[0,2,1]])


passed_function = lambda count, clip, function="tf_test" : function(clip)

sas_maker = lambda count, clip : mirror(invert_green_blue(clip)) if count % 2 == 0 \
                                else (mirror(clip) if count % 3 == 0 else clip)


speed_reversing = lambda count, clip : speedx_sync(clip, 0.9) \
                        if count % 2 == 0 else \
                        (clip.fl(scroll).fx(vfx.time_mirror) \
                        if count % 3 == 0 \
                        else speedx_sync( clip, 2))

stutter = lambda length, clip: clip.subclip()

templates["speed_reversing"] = speed_reversing
templates["sas_maker"] = sas_maker