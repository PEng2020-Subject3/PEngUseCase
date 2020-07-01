import IndivScores as indiv
import json

'''Functions in this class create a json containing respective information'''
class DriverScores:
	def __init__(self, persID, days):
		self.speedscore = indiv.getSpeedVal()
		self.turnscore = indiv.getTurnVal()
		self.brakescore = indiv.getBrakeVal()
		self.crashscore = indiv.getCrashVal()
		self.avgspeed = indiv.getAvgSpeed()

		#indiv ID
		self.persID = persID
		#range of days that values shall be calculated for
		self.days = days


		print("Driver Scores: Initialized.")

	'''Calulate driver score – Use Case 1'''
	def getDriverScore(self):
		self.driverscore = (0.2 * self.speedscore) + (0.2 * self.turnscore) + (0.2 * self.brakescore) + (0.4 * self.crashscore)

		print(self.driverscore)
		
		#write driver score into json 

	'''Calculate driver score for one week – Use Cases 1 & 2'''
	def getDriverScoreWeek(self):
		self.days = 7
		self.driverscore = calcDriverScore()

		#write driverscore and avgspeed into json

	