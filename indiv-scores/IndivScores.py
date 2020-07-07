#!/usr/bin/python
from configparser import ConfigParser
import psycopg2

'''This class calculates individual scores based on information received from a database that can be further processed.'''
class IndivScores(Object):
	def __init__(self, id, days, scoretype):
		self.id = id
		self.days = days
		self.scoretype = scoretype

	def main(self):
		self.initTables()
		if (scoretype == driverscore):
			return self.getDriverscoreData()
		elif (scoretype == performancescore):
			return self.getPerfscoreData()
		else:
			print("Undefined Data Requested.")
			exit()

	#from https://www.postgresqltutorial.com/postgresql-python/connect/
	def config(filename='database.ini', section='postgresql'):
	    # create a parser
	    parser = ConfigParser()
	    # read config file
	    parser.read(filename)

	    # get section, default to postgresql
	    db = {}
	    if parser.has_section(section):
	        params = parser.items(section)
	        for param in params:
	            db[param[0]] = param[1]
	    else:
	        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

	    return db

	#based on https://www.postgresqltutorial.com/postgresql-python/connect/
	def connect(query):
	    '''Connect to the PostgreSQL database server'''
	    conn = None
	    try:
	        # read connection parameters
	        params = IndivScores.config()

	        # connect to the PostgreSQL server
	        conn = psycopg2.connect(**params)

	        # create a cursor
	        cur = conn.cursor()

			# execute a statement
	        cur.execute(query)

	        # display the PostgreSQL database server version
	        db_version = cur.fetchone()

	        return db_version

		    # close the communication with the PostgreSQL
	        cur.close()
	    except (Exception, psycopg2.DatabaseError) as error:
	        print(error)
	    finally:
	        if conn is not None:
	            conn.close()

	'''Packs JSON with use case-specific data '''
	def getDriverscoreData(self):
		self.speedscore = IndivScores.getSpeedVal(self.id, self.days)
		self.turnscore = IndivScores.getTurnVal(self.id, self.days)
		self.brakescore = IndivScores.getBrakeVal(self.id, self.days)
		self.crashscore = IndivScores.getCrashVal(self.id, self.days)
		self.avgspeed = IndivScores.getAvgSpeed(self.id, self.days)

		return packJSON()

	def getPerfscoreData(self):
		self.logs = IndivScores.getn(self.id, self.days)
		self.speedscore = IndivScores.getSpeedVal(self.id, self.days)
		self.turnscore = IndivScores.getTurnVal(self.id, self.days)
		self.brakescore = IndivScores.getBrakeVal(self.id, self.days)
		self.crashscore = IndivScores.getCrashVal(self.id, self.days)
		self.avgspeed = IndivScores.getAvgTypeSpeed(self.id, self.days)
		self.engperf = IndivScores.getEnginePerf(self.id, self.days)

		return packJSON()

	def packJSON(self):
		if (scoretype == driverscore):
			res_raw = {
				'speedscore': self.speedscore,
				'turnscore': self.turnscore,
				'brakescore': self.brakescore,
				'crashscore': self.crashscore,
				'avgspeed': self.avgspeed
			}

			res = json.dumps(res_raw, indent=2)

			return res

		elif (scoretype == performancescore):
			res_raw = {
				'logs': self.logs,
				'speedscore': self.speedscore,
				'turnscore': self.turnscore,
				'brakescore': self.brakescore,
				'crashscore': self.crashscore,
				'avgspeed': self.avgspeed,
				'engperf': self.engperf
			}

			res = json.dumps(res_raw, indent=2)

			return res

		else:
			print("Undefined Data Requested.")
			exit()

	'''Get from date'''
	def getdate(days):
		'''
		TODO:

		calculate from date based on current_date and days
		'''

		return '2000-01-01'

	'''Create tables if they do not exist yet'''
	def initTables(self):
		query = str('CREATE TABLE IF NOT EXISTS usecase (persID int PRIMARY KEY,typeID varchar (50) NOT NULL,speed int,performance int,speedev boolean,brakeev boolean,turnev boolean,crashev boolean,date date NOT NULL)')
		IndivScores.connect(query)

	'''Get total amount of values, while values are received every XX seconds'''
	def getn(persID, days):
		date = getdate(self.days)
		query = str('SELECT COUNT(*) FROM usecase WHERE persID = ' + str(persID) + ' AND date >= ' + str(date))
		result = IndivScores.connect(query)

		return result

	'''Functions below calculate values between 0 and 1 – Use Cases 1 & 3'''
	def getSpeedVal(persID, days):
		n = getn(persID, date)
		date = getdate(days)

		query = str('SELECT COUNT(*) FROM usecase WHERE persID = ' + persID + ' AND speedev = 1 AND date >= ' + str(date))
		temp = IndivScores.connect(query)
		result = (temp / n)

		return result

	def getTurnVal(persID, days):
		n = getn(persID, date)
		date = getdate(days)

		query = str('SELECT COUNT(*) FROM usecase WHERE persID = ' + persID + ' AND turnev = 1 AND date >= ' + str(date))
		temp = IndivScores.connect(query)
		result = (temp / n)

		return result

	def getBrakeVal(persID, days):
		n = getn(persID, date)
		date = getdate(days)

		query = str('SELECT COUNT(*) FROM usecase WHERE persID = ' + persID + ' AND brakeev = 1 AND date >= ' + str(date))
		temp = IndivScores.connect(query)
		result = (temp / n)

		return result

	def getCrashVal(persID, days):
		n = getn(persID, date)
		date = getdate(days)

		query = str('SELECT COUNT(*) FROM usecase WHERE persID = ' + persID + ' AND crashev = 1 AND date >= ' + str(date))
		temp = IndivScores.connect(query)
		result = (temp / n)

		return result

	'''Functions below calulate positive values – Use Case 3'''
	def getAvgSpeed(persID, days):
		date = getdate(days)

		query = str('SELECT to_char(AVG(speed)) FROM usecase WHERE persID = ' + persID + ' AND date >= ' + str(date))
		result = IndivScores.connect(query)

		return result


	'''Functions below calulate positive values – Use Case 2'''
	def getAvgTypeSpeed(typeID, days):
		date = getdate(days)

		query = str('SELECT to_char(AVG(speed)) FROM usecase WHERE typeID = ' + typeID + ' AND date >= ' + str(date))
		result = IndivScores.connect(query)

		return result

	def getEnginePerf(typeID, days):
		date = getdate(days)

		query = str('SELECT to_char(AVG(performance)) FROM usecase WHERE typeID = ' + typeID + ' AND date >= ' + str(date))
		result = IndivScores.connect(query)

		return result
