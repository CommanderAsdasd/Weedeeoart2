from datetime import datetime
import random

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def file_timestamp():

    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d%b%Y_%H%M%S")

    return timestampStr

def random_sequence(length, file_length):
    
    startPoint = file_length - length
    startPoint = random.uniform(0,startPoint)
    return (startPoint, startPoint+length)
    # translate()

def no_extension(filename: str) -> str:

    return filename.split(".")[-2]
    

