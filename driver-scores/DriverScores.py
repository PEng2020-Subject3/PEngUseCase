#!/usr/bin/python
from urllib.request import urlopen
import json
import os

class DriverScores(object):
"""Functions in this class create a json containing respective information"""
	def __init__(self, method, sensor_ID):
		self.method = method
		self.sensor_ID = sensor_ID

	def main(self):
		if (self.method == "genDriverScore"):
			return self.genDriverScore()
		elif (self.method == "genDriverScoreFleet"):
			return self.genDriverScoreFleet()
		else:
			print("Unknown Method!")

	def getData(self):
	"""Pack and send request to indiv-scores....py and receive response with requested data"""
		req_raw = {
			'sensor_ID': self.sensor_ID,
			'scoretype': "driverscore"
		}

		req = json.dumps(req_raw, indent=2)

		binary_req = req.encode('utf-8')

		try:
			policy = str(os.environ['openfaas.policy.name'])
			url = str("http://gateway.openfaas:8080/function/indiv-driverscores?policy=" + str(policy))
		except:
			url = str("http://gateway.openfaas:8080/function/indiv-driverscores")

		rv = urlopen(url, data=binary_req)
		temp = rv.read().decode('utf-8')
		res = json.loads(temp)
		rv.close()

		self.speedscore = res["speedscore"]
		self.turnscore = res["turnscore"]
		self.brakescore = res["brakescore"]
		self.crashscore = res["crashscore"]
		self.avgspeed = res["avgspeed"]

	def genDriverScore(self):
	"""Output Data – Use Case 1"""
		self.getData()
		score = self.getDriverScore()

		uc_1raw = {
			'sensor_ID': self.sensor_ID,
			'driverscore': score
		}

		uc_1 = json.dumps(uc_1raw, indent=2)

		return uc_1

	def getDriverScore(self):
	"""Calulate driver score – Use Cases 1 & 3"""
		driverscore = ((float(0.2) * float(self.speedscore)) + (float(0.2) * float(self.turnscore)) + (float(0.2) * float(self.brakescore)) + (float(0.4) * float(self.crashscore)))

		return driverscore

	def genDriverScoreFleet(self):
	"""Output Information – Use Case 3"""
		#car type aggregation -- fleet manager can call data for his fleet id/typeID
		self.getData()
		driverscore = self.getDriverScore()

		uc_13raw = {
			'sensor_ID': self.sensor_ID,
			'driverscore': driverscore,
			'avgspeed': self.avgspeed
		}
		uc_13 = json.dumps(uc_13raw, indent=2)

		return uc_13
