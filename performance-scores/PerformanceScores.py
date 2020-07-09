#!/usr/bin/python
from urllib.request import urlopen
import json

'''Functions in this class create a json containing respective information'''
class PerformanceScores(object):
	def __init__(self, method, typeID, days):
		self.method = method
		self.typeID = typeID
		self.days = days

	def main(self):
		if (self.method == "genPerformanceScore"):
			return self.genPerformanceScore()
		else:
			print("Unknown Method!")

	def getData(self):
		req_raw = {
			'id': self.typeID,
			'days': self.days,
			'scoretype': 'performancescore'
		}

		req = json.dumps(req_raw, indent=2)

		binary_req = req.encode('utf-8')

		url = 'http://a489ca8c99162488eb7526720cc82431-290010750.us-east-1.elb.amazonaws.com:8080/function/indiv-performancescores'
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
				'days': self.days,
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
