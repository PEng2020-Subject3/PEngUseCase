#!/usr/bin/python
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

	def getData(self, class):
		reqraw = {
			'id': self.typeID,
			'days': self.days,
			'scoretype': performancescore
		}

		req = json.dumps(reqraw, indent=2)

		'''
		TODO:

		connect to IndivScores, send req and get res!!

		'''

		json_res = json.loads(res)

		self.logs = res["logs"]
		self.speedscore = res["speedscore"]
		self.turnscore = res["turnscore"]
		self.brakescore = res["brakescore"]
		self.crashscore = res["crashscore"]
		self.avgspeed = res["avgspeed"]

	def genPerformanceScore(self):
		self.getData()
		perf = self.getPerformanceScore()

		uc_2raw = {
			'general': {
				'typeID': self.typeID,
				'days': self.days,
				'logs': self.logs
			},
			'scores': {
				'performancescore': perf,
				'speedscore': self.speedscore,
				'turnscore': self.turnscore,
				'brakescore': self.brakescore,
				'crashscore': self.crashscore,
				'avgspeed': self.avgspeed
			}
		}

		uc_2 = json.dumps(uc_2raw, indent=2)

		return uc_2

	def getPerformanceScore(self):
		return 100