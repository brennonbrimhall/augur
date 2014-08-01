class Node:
	def __init__(self, probability=0):
		self.probability = probability
		self.children = {}

	def updateProbability(self, deltaProbability):
		self.probability += deltaProbability

	def getProbability(self):
		return self.probability

	def addChild(self, key, probability=0):
		if not key in self.children:
			self.children[key] = Node(probability)

	def getChild(self, key):
		return self.children[key]

	def log(self, level=0):
		padding = ""
		for i in range(0, level):
			padding += "\t"
		sortedNodes = sorted(self.children.items(), key=lambda x: x[1].probability, reverse=True)
		for key, value in sortedNodes:
			print(padding+"Rank "+str((level+1))+": "+str(key)+" @ "+str(round(value.getProbability()*100, 2)))+"%"
			value.log(level+1)

class Root:
	def __init__(self):
		self.children = {}

	def addChild(self, key, probability=0):
		if not key in self.children:
			self.children[key] = Node(probability)

	def getChild(self, key):
		return self.children[key]

	def log(self):
		#Sort by probability
		sortedNodes = sorted(self.children.items(), key=lambda x: x[1].probability, reverse=True)
		for key, value in sortedNodes:
			print("Rank 1: "+str(key)+" @" +str(round(value.getProbability()*100, 2)))+"%"
			value.log(1)
