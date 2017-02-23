#import python skills
# cat file.txt | python script.py |
import fileinput
import sys

endPointDatalist = []
requestDatalist = []

for line in sys.stdin:
    # split line on space starting the 3rd line
    if line.count(" ") ==  1:
        endPointDatalist.append(line)
    if line.count(" ") == 2:
        requestDatalist.append(line)
        
print endPointDatalist
print requestDatalist


requestObjectList = []

for request in requestDatalist:
    reqObj = Request(request[0], request[1], request[2])
    requestObjectList.append(reqObj)
# loop over de lijst en stop elk onderdeeltje in een object
        
print requestObjectList


class Request(object):
	"""
	Represents a request
	"""
    def __init__(self, amount, video, endpoint):
        self.video_id = video
        self.endpoint = endpoint
        self.amount = amount
        self.urgency = None
