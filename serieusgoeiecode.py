#import python skills
# cat file.txt | python script.py |
import fileinput
import sys


class Request(object):
    def __init__(self, amount, video, endpoint):
        self.videoId = video
        self.endpoints = endpoint
        self.amount = amount
        self.urgency = None

class Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.videos = []
        self.currentCapacity = return calculateCacheCapacity(videos)

def calculateCacheCapacity:
    size = 0
    for i in videoArray:
        size = size + videoArray[i]
    return size
                
# Split endpoint data and request data
generaldata = None
videoArray = None         
endPointDatalist = []
requestDatalist = []

for line in sys.stdin:
    # split line on space starting the 3rd line
    if line.count(" ") > 4
        generaldata = line.split()
    if line.count(" ") == 4:
        videoArray = line.split()
    if line.count(" ") ==  1:
        endPointDatalist.append(line)
    if line.count(" ") == 2:
        requestDatalist.append(line)
        
print endPointDatalist
print requestDatalist


# get request objects
def generateRequests:
    requestObjectList = []

    for request in requestDatalist:
        reqObj = Request(request[0], request[1], request[2])
        requestObjectList.append(reqObj)
    # loop over de lijst en stop elk onderdeeltje in een object
            
    return requestObjectList

# generate cache objects
def generateCaches:
    cacheList = []
    for cache in range(0, 9)
        cacheObj = Cache(100)
        cacheList.append(cacheObj)
    return cacheList
