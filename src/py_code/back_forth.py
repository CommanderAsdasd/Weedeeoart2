#!/usr/bin/env pipenv-shebang


from moviepy.editor import *
import pdb, sys
from weedeeo.helpers import *
import math
from weedeeo.effects import *
from weedeeo.rules import *
from weedeeo import scanner
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

def take_random_clips(video_file_list, count=5):

    video_files_out = []
    for i in range(count):
        video_files_out.append(random.choice(video_file_list))
    return video_files_out


path_list = []
# for video in scanner.scan_path(path):
    # print(video)
    # path_list.append(video)
# videos_list = take_random_clips(path_list)


clip_count = 20


def compose_timeline(*args):
    output_clips = [None]
    for i, clip  in enumerate(args):
        print(i)
        try:
            output_clips[i] = clip
        except Exception:
            pass
    return concatenate_videoclips(output_clips)

# clips_cut = [concatenate_videoclips([cutting_function(counter, clip), cutting_function_2(counter, clip)]) for counter, clip in enumerate(clips * clip_count) ]
# clips = [clip.subclip(*random_sequence(20, clip.duration/2)) for clip in clips]
clips_cut = [cutting_function_2(counter, clip) for counter, clip in enumerate(clips * clip_count) ]
random.shuffle(clips_cut)

class part():
    
    def __init__(cut_rule, clip_count=1):
        pass
        

# To generating_function - lambda
# TODO: base more function on this random sequences
effects = templates["vanilla"]
# clips = list(map(sas_maker, enumerate(clips)))
clips_cut_fx = [effects(counter, clip) for counter, clip in enumerate(clips_cut) ]
# clips_cut_fx = panoram(clips_cut_fx)
random.shuffle(clips_cut_fx)
video = concatenate_videoclips(clips_cut_fx, method="compose")
name = "_".join([no_extension(sys.argv[i]) for i, video_path in enumerate(sys.argv)])
video.write_videofile(f"output/{name}-{file_timestamp()}.mp4")