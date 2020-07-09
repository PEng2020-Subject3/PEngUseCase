#!/usr/bin/python
from urllib.request import urlopen
import json

'''Functions in this class create a json containing respective information'''
class DriverScores(object):
	def __init__(self, method, persID):
		self.method = method
		self.persID = persID

	def main(self):
		if (self.method == "genDriverScore"):
			return self.genDriverScore()
		elif (self.method == "genDriverScoreWeek"):
			return self.genDriverScoreWeek()
		else:
			print("Unknown Method!")

	def getData(self):
		req_raw = {
			'id': self.persID,
			'scoretype': "driverscore"
		}

		req = json.dumps(req_raw, indent=2)

		binary_req = req.encode('utf-8')

		url = 'http://a489ca8c99162488eb7526720cc82431-290010750.us-east-1.elb.amazonaws.com:8080/function/indiv-driverscores'
		rv = urlopen(url, data=binary_req)
		temp = rv.read().decode('utf-8')
		res = json.loads(temp)
		rv.close()

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
		#car type aggregation -- fleet manager can call data for his fleet id/typeID
		self.getData()
		driverscore = self.getDriverScore()

		uc_13raw = {
			'id': self.persID,
			'driverscore': driverscore,
			'avgspeed': self.avgspeed
		}
		uc_13 = json.dumps(uc_13raw, indent=2)

		return uc_13
