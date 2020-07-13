#!/usr/bin/python
from urllib.request import urlopen
from .IndivScores import IndivScores
import json
import os

'''Functions in this class create a json containing respective information'''
class DriverScores(object):
	def __init__(self, method, persID):
		self.method = method
		self.persID = persID

	def main(self):
		if (self.method == "genDriverScore"):
			return self.genDriverScore()
		elif (self.method == "genDriverScoreFleet"):
			return self.genDriverScoreFleet()
		else:
			print("Unknown Method!")

	def getData(self):
		req_raw = {
			'id': self.persID,
			'scoretype': "driverscore"
		}

		req = json.dumps(req_raw, indent=2)

		res = DriverScores.handle(req)
		json_res = json.loads(res)

		self.speedscore = json_res["speedscore"]
		self.turnscore = json_res["turnscore"]
		self.brakescore = json_res["brakescore"]
		self.crashscore = json_res["crashscore"]
		self.avgspeed = json_res["avgspeed"]

	def handle(req):
	    json_req = json.loads(req)
	    id = json_req["id"]
	    scoretype = json_req["scoretype"]

	    temp = IndivScores(id, scoretype)
	    output = temp.main()

	    return output


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
	def genDriverScoreFleet(self):
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
