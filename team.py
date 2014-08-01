class Team:
	def __init__(self, number, qs, firstSort, secondSort, thirdSort, fourthSort=0, fifthSort=0):
		self.number = number;
		self.qs = qs;
		self.firstSort = firstSort;
		self.secondSort = secondSort;
		self.thirdSort = thirdSort;
		self.fourthSort = fourthSort;
		self.fifthSort = fifthSort;

	def getNumber(self):
		return self.number;

	def getQS(self):
		return self.qs;

	def getFirstSort(self):
		return self.firstSort;

	def getSecondSort(self):
		return self.secondSort;

	def getThirdSort(self):
		return self.thirdSort;

	def getFourthSort(self):
		return self.fourthSort;

	def getFifthSort(self):
		return self.fifthSort

	def win(self):
		self.qs += 2;

	def __cmp__(self, other):
		if self.getQS() > other.getQS():
			return 1
		elif self.getQS() < other.getQS():
			return -1
		elif self.getFirstSort() > other.getFirstSort():
			return 1
		elif self.getFirstSort() < other.getFirstSort():
			return -1
		elif self.getThirdSort() > other.getThirdSort():
			return 1
		elif self.getThirdSort < other.getThirdSort():
			return -1
		elif self.getFourthSort() > other.getFourthSort():
			return 1
		elif self.getFourthSort() < other.getFourthSort():
			return -1
		elif self.getFifthSort > other.getFifthSort():
			return 1
		elif self.getFifthSort < other.getFifthSort():
			return -1
		elif self.getFifthSort == other.getFifthSort():
			return 0