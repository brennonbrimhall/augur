import tree
import match
import team
import copy
import sys
import timer
import datetime

class Event:
	def __init__(self, maxRank):
		self.matches = []
		self.teams = []
		self.root = tree.Root()
		self.maxRank = maxRank

	def addMatch(self, red1, red2, red3, blue1, blue2, blue3, redWinProbability=.5):
		self.matches.append(match.Match(red1, red2, red3, blue1, blue2, blue3, redWinProbability))

	def addTeam(self, number, qs, firstSort, secondSort, thirdSort, fourthSort=0, fifthSort=0):
		self.teams.append(team.Team(number, qs, firstSort, secondSort, thirdSort, fourthSort, fifthSort))

	def findTeam(self, teams, teamNumber):
		for team in teams:
			if team.getNumber() == teamNumber:
				return team
		return None

	def calculatePossibility(self, possibilityNumber):
		#Write out message to stderr; this won't get redirected to file.
		percent = float(possibilityNumber+1)/(2**len(self.matches))
		sys.stderr.write("\r["+"{0:.2f}".format((percent)*100)+"%] "+str(self.timer.started())+" elapsed, "+str(self.timer.timeToCompletion(percent))+" remaining")
		sys.stderr.flush()
		
		#Actually calculate the possibility
		currentNumber = possibilityNumber
		teams = copy.deepcopy(self.teams)
		probability = 1
		for i in range(0, len(self.matches)):
			outcomeNumber = currentNumber % 2
			if outcomeNumber == 0:
				#Red Wins
				probability = probability * self.matches[i].getRedWinProbability()
				self.findTeam(teams, self.matches[i].getRed1()).win()
				self.findTeam(teams, self.matches[i].getRed2()).win()
				self.findTeam(teams, self.matches[i].getRed3()).win()
			elif outcomeNumber == 1:
				#Blue Wins
				probability = probability * self.matches[i].getBlueWinProbability()
				self.findTeam(teams, self.matches[i].getBlue1()).win()
				self.findTeam(teams, self.matches[i].getBlue2()).win()
				self.findTeam(teams, self.matches[i].getBlue3()).win()
			currentNumber = currentNumber / 2
		teams.sort(reverse=True)
		self.updateSummary(teams, probability)

	def updateSummary(self, teams, probability):
		currentNode = self.root
		for i in range(0, self.maxRank):
			currentNode.addChild(teams[i].getNumber(), 0)
			currentNode = currentNode.getChild(teams[i].getNumber())
			currentNode.updateProbability(probability)

	def calculate(self):
		self.timer = timer.Timer()
		for i in range(0, (2**len(self.matches))):
			self.calculatePossibility(i)
		self.root.log()
		sys.stderr.write("\a")
		sys.stderr.flush()
