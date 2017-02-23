# imports

# class request
# class cashe


class Video(object):
	"""
	Represents a video
	""" 
	def __init__(self, number, size):
		self.id = number
		self.size = size

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
	def __init__(self, amount, video, endpoint):
		self.video_id = video
		self.amount = amount

		# must be an endpoint object, so we can acces the latency to base
		self.endpoint = endpoint
		
		# calculate urgency of request
		self.urgency = self.endpoint.latency_to_base * self.amount

class Endpoint(object):
	"""
	Represents an endpoint
	"""
	def __init__(self, latency, connections):
		self.latency_to_base = latency
		self.connections = {}

