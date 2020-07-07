#!/usr/bin/python
import json

'''Functions in this class create a json containing respective information'''
class DriverScores(object):
	def __init__(self, method, persID, days):
		self.method = method
		self.persID = persID
		self.days = days

	def main(self):
		if (self.method == "genDriverScore"):
			return self.genDriverScore()
		elif (self.method == "genDriverScoreWeek"):
			return self.genDriverScoreWeek()
		else:
			print("Unknown Method!")

	def getData(self, class):
		reqraw = {
			'id': self.persID,
			'days': self.days,
			'scoretype': driverscore
		}

		req = json.dumps(reqraw, indent=2)

		'''
		TODO:

		connect to db, send req and get res!!

		'''

		json_res = json.loads(res)

		self.speedscore = res["speedscore"]
		self.turnscore = res["turnscore"]
		self.brakescore = res["brakescore"]
		self.crashscore = res["crashscore"]
		self.avgspeed = res["avgspeed"]

	'''Dashboard Information – Use Case 1'''
	def genDriverScore(self):
		self.getData()
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
