# import python skills
# cat file.txt | python script.py |

class Cache(object):
    """
    Represents a cache that can be filled with videos
    """
    def __init__(self, number, capacity):
        self.id = number
        self.capacity = capacity
        self.videos = []


class Request(object):
    """
    Represents a request
    """
    def __init__(self, amount, video, endpoint, tobeanounced):
        self.video_id = video
        self.amount = amount
        self.endpoint = endpoint
        self.urgency = tobeanounced


class Endpoint(object):
    """
    Represents an endpoint
    """
    def __init__(self, latency, connections):
        self.latency_to_base = latency
        self.connections = []


import sys
lijst = []
for line in sys.stdin:
    # split line on space starting the 3rd line
    lijst.append(line.split())

videos = lijst[1]
counter = 0

endpoints = []
ekte_endpoints = {}
index = 0
for lijst_item in lijst:
    if len(lijst_item) == 2:
        endpoints.append(lijst_item)

print endpoints

i = 0
countjes = 0
cach = {}
while i < range(len(endpoints) - 1):
    try:
        ekte_endpoints[countjes] = {}
        ekte_endpoints[countjes][endpoints[i][0]] = []
        print endpoints[i][0], endpoints[i][1]
        for j in range(int(endpoints[i][1])):
            ekte_endpoints[countjes][endpoints[i][0]] \
                .append(endpoints[i + j + 1][1])
            print ekte_endpoints, i, j, countjes
        print i, int(endpoints[i][1]), "regel 63"
        i = i + int(endpoints[i][1]) + 1
        countjes += 1
    except IndexError:
        break

print ekte_endpoints


# print lijst[2][1]
# for item in range(int(lijst[2][1]) - 1):
#     endpoints[lijst[2][0]] = lijst[2 + item + 1]
#     print lijst[2 + item + 1]

# print endpoints
