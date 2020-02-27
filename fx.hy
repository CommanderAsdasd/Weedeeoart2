#!/usr/bin/env hy

(import [numpy [*]])
(import [moviepy [*]])

my_clip = VideoFileClip("some_file.mp4")
my_clip.set_start(t=5) # does nothing, changes are lost
my_new_clip = my_clip.set_start(t=5) # good !