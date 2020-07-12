#!/usr/bin/python
from urllib.request import urlopen
import json
import os

'''Functions in this class create a json containing respective information'''
class PerformanceScores(object):
	def __init__(self, method, typeID):
		self.method = method
		self.typeID = typeID

	def main(self):
		if (self.method == "genPerformanceScore"):
			return self.genPerformanceScore()
		else:
			print("Unknown Method!")

	def getData(self):
		req_raw = {
			'id': self.typeID,
			'scoretype': 'performancescore'
		}

		req = json.dumps(req_raw, indent=2)

		binary_req = req.encode('utf-8')

		try:
			policy = str(os.environ['openfaas.policy.name'])
			url = str("http://gateway.openfaas:8080/function/indiv-performancescores?policy=" + str(policy))
		except:
			url = str("http://gateway.openfaas:8080/function/indiv-performancescores")

		rv = urlopen(url, data=binary_req)
		temp = rv.read().decode('utf-8')
		res = json.loads(temp)
		rv.close()

		self.logs = res["logs"]
		self.speedscore = res["speedscore"]
		self.turnscore = res["turnscore"]
		self.brakescore = res["brakescore"]
		self.crashscore = res["crashscore"]
		self.avgspeed = res["avgspeed"]
		self.engperf = res["engperf"]

	def genPerformanceScore(self):
		self.getData()

		uc_2raw = {
			'general': {
				'typeID': self.typeID,
				'logs': self.logs
			},
			'scores': {
				'performancescore': self.engperf,
				'speedscore': self.speedscore,
				'turnscore': self.turnscore,
				'brakescore': self.brakescore,
				'crashscore': self.crashscore,
				'avgspeed': self.avgspeed
			}
		}

		uc_2 = json.dumps(uc_2raw, indent=2)

		return uc_2
