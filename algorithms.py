from heapq import *

def greedy(requests, caches, videos):

	# variable for worst latency score (all videos in base data centre)
	worstScore = 0

	# put requests in priorityqueue
	urgencyQueue = []

	for request in requests:
		heappush(urgencyQueue,((request.urgency*-1),request))
		worstScore += request.urgency

	# pop requests and place them in caches
	for request in urgencyQueue:
		request = heappop(urgencyQueue)[1]

		# starting best value
		best = request.urgency
		cacheID = None

		# choose best cache
		for connection in request.endpoint.connections:
			cost = connection['latency'] * request.amount
			if cost < best:
				cacheID = connection['id']
				if (caches[cacheID].currentCapacity + videos[request.video_id] <= caches[cacheID].capacity)
					best = cost

		# send video of this request to best cache
		if cacheID != None:
			caches[cacheID].videos.append(request.video_id)
			# score improvement
			worstScore -= (request.urgency - best)

	# this is actually the best score now
	print worstScore



