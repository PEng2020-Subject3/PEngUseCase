'''This class calculates individual scores based on information received from a database that can be further processed.'''

class IndivScores(object):
	def __init__(self):

		'''
		MAYBE ALWAYS RELATE TO CURRENT DATE?

		#reference point for score determination
		self.refdate =
		#values have to be younger than this date
		self.pastdate =
		'''

		print("Individual Scores: Initialized.")

	'''Get total amount of values, while values are received every 30 seconds'''
	def getn(persID, days):
		return 30

	'''Functions below calculate value between 0 and 1 – Use Cases 1 & 3'''
	def getSpeedVal(persID, days):
		return 0.5

	def getTurnVal(persID, days):
		return 0.5

	def getBrakeVal(persID, days):
		return 0.5

	def getCrashVal(persID, days):
		return 0.5

	'''Functions below calulate positive values – Use Case 3'''
	def getAvgSpeed(persID, days):
		return 50

	'''Functions below calulate positive values – Use Case 2'''
	def getAvgTypeSpeed(typeID, days):
		return 36

	def getEnginePerf(typeID, days):
		return 89
