#!/usr/bin/python
from IndivScores import IndivScores as indiv
import json

'''Functions in this class create a json containing respective information'''
class DriverScores(object):
	def __init__(self, method, persID, days):
		self.method = method
		self.persID = persID
		self.days = days

		self.speedscore = indiv.getSpeedVal(persID, days)
		self.turnscore = indiv.getTurnVal(persID, days)
		self.brakescore = indiv.getBrakeVal(persID, days)
		self.crashscore = indiv.getCrashVal(persID, days)
		self.avgspeed = indiv.getAvgSpeed(persID, days)

	def main(self):
		if (self.method == "genDriverScore"):
			return self.genDriverScore()
		elif (self.method == "genDriverScoreWeek"):
			return self.genDriverScoreWeek()
		else:
			print("Unknown Method!")

	'''Dashboard Information – Use Case 1'''
	def genDriverScore(self):
		score = self.getDriverScore()

		uc_1raw = {
			'id': self.persID,
			'days': self.days,
			'driverscore': score
		}

		uc_1 = json.dumps(uc_1raw, indent=2)

		return uc_1

	'''Calulate driver score for certain time period'''
	def getDriverScore(self):
		driverscore = ((float(0.2) * float(self.speedscore)) + (float(0.2) * float(self.turnscore)) + (float(0.2) * float(self.brakescore)) + (float(0.4) * float(self.crashscore)))

		return driverscore

	'''Dashboard Information – Use Cases 1 & 3'''
	def genDriverScoreWeek(self):
		#time aggreation over one week (can be adjusted of course)
		self.days = 7
		driverscore = self.getDriverScore()

		uc_13raw = {
			'id': self.persID,
			'driverscore': driverscore,
			'avgspeed': self.avgspeed
		}

		uc_13 = json.dumps(uc_13raw, indent=2)
		return uc_13

	'''Would be nice to have a crash alert, but does not make really sense as long as database not dynamically created'''
	#def getAlert(self):
	#	self.days = 1
