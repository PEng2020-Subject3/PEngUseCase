from IndivScores import IndivScores as indiv
import json

'''Functions in this class create a json containing respective information'''
class PerformanceScores(object):
	def __init__(self, method, typeID, days):
		self.method = method
		self.typeID = typeID
		self.days = days

		self.logs = indiv.getn(typeID, days)
		self.speedscore = indiv.getSpeedVal(typeID, days)
		self.turnscore = indiv.getTurnVal(typeID, days)
		self.brakescore = indiv.getBrakeVal(typeID, days)
		self.crashscore = indiv.getCrashVal(typeID, days)
		self.avgspeed = indiv.getAvgSpeed(typeID, days)

	def main(self):
		if (self.method == "genPerformanceScore"):
			return self.genPerformanceScore()
		else:
			print("Unknown Method!")

	def genPerformanceScore(self):
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
