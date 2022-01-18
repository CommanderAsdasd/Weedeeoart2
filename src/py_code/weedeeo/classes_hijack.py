from moviepy.editor import *
import random
# import mido

class VideoFileClip(VideoFileClip):

    # def __init__(self,)

    def random_sequence(self, length, count=1, stutter=False):
        """stutter repeates only one fragment"""
        # self.sequence=[]
        file_length = self.end
        
        # file_length = self.end
        # print(f"clip duration {self.duration} clip end is {self.end}")
        def randclip():
            startPoint = file_length - length
            startPoint = random.uniform(0,startPoint)
            return self.subclip(startPoint, startPoint+length)
        
        if stutter:
            clip = randclip() 
            sequence = [clip for i in range(count)]

        sequence = [randclip() for i in range(count)]
        # breakpoint()
        # self.sequence.append()
        return concatenate_videoclips(*[sequence])
        # return self

    # def render_sequence(self):

