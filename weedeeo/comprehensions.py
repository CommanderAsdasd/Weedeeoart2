from moviepy.editor import *
import math

comprehensions_set = {}

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


speed_reversing = lambda count, clip : speedx_sync(clip, 0.9) \
                        if count % 2 == 0 else \
                        (clip.fl(scroll).fx(vfx.time_mirror) \
                        if count % 3 == 0 \
                        else speedx_sync( clip, 2))

stutter = lambda length, clip: clip.subclip()

comprehensions_set["speed_reversing"] = speed_reversing