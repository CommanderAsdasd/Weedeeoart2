from datetime import datetime
import sys
import random

uni = lambda low, up, count=1: random.uniform(low, up) if count == 1 else [random.uniform(low, up) for i in range(count)]
choice = lambda x, count=1: random.choice(x) if count == 1 else [random.choice(x) for i in range(count)]

def input_data(file=sys.argv[1]):
    
    print(file)

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
        
    return filename.split("/")[-1].split(".")[-1]

    

