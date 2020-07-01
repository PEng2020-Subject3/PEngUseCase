'''This class calculates individual scores based on information received from a database that can be further processed.'''

class IndivScores:
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
	def getn(self):
		self.n = 30

	'''Functions below calculate value between 0 and 1 – Use Cases 1 & 2 & 3'''
	def getSpeedVal(self):
		return 0,5

	def getTurnVal(self):
		return 0,5

	def getBrakeVal(self):
		return 0,5

	def getCrashVal(self):
		return 0,5

	'''Functions below calulate positive values – Use Cases 2 & 3'''
	def getAvgSpeed(self):	
		return 50
		#maybe define time range for working hours to determine this value more precisely