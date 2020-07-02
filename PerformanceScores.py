import IndivScores as indiv
import json

class Performance Scores(object):
	def __init__(self, pubID, days):
		self.speedscore = indiv.getSpeedVal()
		self.turnscore = indiv.getTurnVal()
		self.brakescore = indiv.getBrakeVal()
		self.crashscore = indiv.getCrashVal()

		#indiv ID
		self.pubID = pubID
		#range of days that values shall be calculated for
		self.days = days


		print("Driver Scores: Initialized.")
	'''Create json with performance data so that engineer knows how cars are used'''
	def getRequirements(self):
