class Match:
	def __init__(self, red1, red2, red3, blue1, blue2, blue3, redWinProbability):
		self.red1 = red1
		self.red2 = red2
		self.red3 = red3
		self.blue1 = blue1
		self.blue2 = blue2
		self.blue3 = blue3
		self.redWinProbability = redWinProbability

	def getRed1(self):
		return self.red1

	def getRed2(self):
		return self.red2

	def getRed3(self):
		return self.red3

	def getBlue1(self):
		return self.blue1

	def getBlue2(self):
		return self.blue2

	def getBlue3(self):
		return self.blue3

	def getRedWinProbability(self):
		return self.redWinProbability

	def getBlueWinProbability(self):
		return 1-self.redWinProbability