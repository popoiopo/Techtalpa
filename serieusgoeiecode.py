#import python skills
# cat file.txt | python script.py |
import fileinput
import sys


class Request(object):
    def __init__(self, video, endpoint, amount):
        self.videoId = video
        self.endpoints = endpoint
        self.amount = amount
        self.urgency = None

class Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.videos = []
        self.currentCapacity = calculateCacheCapacity(videos)

def calculateCacheCapacity():
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
    if line.count(" ") > 4:
        generaldata = line.split()
    if line.count(" ") == 4:
        videoArray = line.split()
    if line.count(" ") ==  1:
        endPointDatalist.append(line.split())
    if line.count(" ") == 2:
        requestDatalist.append(line.split())

def generateEndpoints():

    endpoints = endPointDatalist
    ekte_endpoints = {}
    i = 0
    countjes = 0
    while i < range(len(endpoints) - 1):
        try:
            cach = {}
            ekte_endpoints[countjes] = {}
            ekte_endpoints[countjes][endpoints[i][0]] = []
            for j in range(int(endpoints[i][1])):
                print endpoints[i + j + 1][0], endpoints[i + j + 1][1]
                cach[endpoints[i + j + 1][0]] = endpoints[i + j + 1][1]
            ekte_endpoints[countjes][endpoints[i][0]] \
                .append(cach)
            i = i + int(endpoints[i][1]) + 1 
            countjes += 1
        except IndexError:
            break
        
    return ekte_endpoints
    

actualEndPointList = generateEndpoints()
print actualEndPointList
    
# get request objects
def generateRequests():
    requestObjectList = []

    for request in requestDatalist:
        print request[1]
        indexkey = request[1]
        reqObj = Request(request[0], actualEndPointList[indexkey], request[2])
        requestObjectList.append(reqObj)
    print requestObjectList
    return requestObjectList

# generate cache objects
def generateCaches():
    cacheList = []
    for cache in range(0, 9):
        cacheObj = Cache(100)
        cacheList.append(cacheObj)
    return cacheList

generateRequests()