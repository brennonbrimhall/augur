from datetime import datetime
from datetime import timedelta

class Timer:
	def __init__(self):
		self.startTime = datetime.now()
	
	#Time until complete, given nonzero percentage until completion
	def timeToCompletion(self, percent):
		dt = datetime.now() - self.startTime
		dividedSeconds = dt.total_seconds() / percent
		totalTime = timedelta(seconds=dividedSeconds)
		timeRemaining = totalTime - dt
		return timeRemaining
	
	#Time since started
	def started(self):
		return datetime.now() - self.startTime
