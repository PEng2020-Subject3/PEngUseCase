#!/usr/bin/python
from __future__ import division
from configparser import ConfigParser
import psycopg2
import json

'''This class calculates individual scores based on information received from a database that can be further processed.'''
class IndivScores(object):
	def __init__(self, id, days, scoretype):
		self.id = id
		self.days = days
		self.scoretype = scoretype

	def main(self):
		self.initTables()

		if (self.scoretype == "driverscore"):
			return self.getDriverscoreData()
		elif (self.scoretype == "performancescore"):
			return self.getPerfscoreData()
		else:
			print("Undefined Data Requested.")
			exit()

	#based on https://www.postgresqltutorial.com/postgresql-python/connect/
	def config(filename='database.ini', section='postgresql'):
	    # create a parser
	    parser = ConfigParser()
	    # read config file
	    parser.read(filename)

	    # get section, default to postgresql
	    db = {
			"host": "usecase-postgres-db-postgresql",
			"database": "postgres",
			"user": "postgres",
			"password": "3BDAJjFHOA"
		}

	    return db

	#based on https://www.postgresqltutorial.com/postgresql-python/connect/
	def connect(query, mode):
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
	        db_version = None

	        if (mode == "display"):
	            # display the PostgreSQL database server version
	            db_version = cur.fetchone()
	        else:
	            conn.commit()

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

		return self.packJSON()

	def getPerfscoreData(self):
		self.logs = IndivScores.getn(self.id, self.days)
		self.speedscore = IndivScores.getSpeedVal(self.id, self.days)
		self.turnscore = IndivScores.getTurnVal(self.id, self.days)
		self.brakescore = IndivScores.getBrakeVal(self.id, self.days)
		self.crashscore = IndivScores.getCrashVal(self.id, self.days)
		self.avgspeed = IndivScores.getAvgTypeSpeed(self.id, self.days)
		self.engperf = IndivScores.getEnginePerf(self.id, self.days)

		return self.packJSON()

	def packJSON(self):
		if (self.scoretype == "driverscore"):
			res_raw = {
				'speedscore': self.speedscore,
				'turnscore': self.turnscore,
				'brakescore': self.brakescore,
				'crashscore': self.crashscore,
				'avgspeed': self.avgspeed
			}

			res = json.dumps(res_raw, indent=2)

			return res

		elif (self.scoretype == "performancescore"):
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
		query = str("CREATE TABLE IF NOT EXISTS usecase (persID int PRIMARY KEY,typeID varchar (50) NOT NULL,speed int,performance int,speedev boolean,brakeev boolean,turnev boolean,crashev boolean,targetdate date NOT NULL);")
		IndivScores.connect(query, "create")

		# FOR TESTING
		# stuff = str("INSERT INTO usecase VALUES (652, 'smart', 34, 60, true, false, true, false, '1997-12-27');")
		# IndivScores.connect(stuff, "insert")
		#
		# query = str('SELECT * FROM usecase WHERE persID = 654;')
		# temp = IndivScores.connect(query, "display")
		# print("jetzt kommt's")
		# print(temp)

	'''Get total amount of values, while values are received every XX seconds'''
	def getn(persID, days):
		date = IndivScores.getdate(days)
		query = str('SELECT COUNT(*) FROM usecase WHERE persID = ' + str(persID) + ';')#' AND targetdate >= ' + str(date) + ';')
		result = IndivScores.connect(query, "display")

		return result

	'''Functions below calculate values between 0 and 1 – Use Cases 1 & 3'''
	def getSpeedVal(persID, days):
		n = IndivScores.getn(persID, days)
		date = IndivScores.getdate(days)

		query = str('SELECT COUNT(*) FROM usecase WHERE persID = ' + str(persID) + ' AND speedev = TRUE')# AND targetdate >= ' + str(date))
		temp = IndivScores.connect(query, "display")

		if (n[0] != 0):
			result = (temp[0] / n[0])
		else:
			print("No Matching DB Entries!")
			exit()

		return result

	def getTurnVal(persID, days):
		n = IndivScores.getn(persID, days)
		date = IndivScores.getdate(days)

		query = str('SELECT COUNT(*) FROM usecase WHERE persID = ' + str(persID) + ' AND turnev = TRUE')# AND targetdate >= ' + str(date))
		temp = IndivScores.connect(query, "display")

		if (n[0] != 0):
			result = (temp[0] / n[0])
		else:
			print("No Matching DB Entries!")
			exit()

		return result

	def getBrakeVal(persID, days):
		n = IndivScores.getn(persID, days)
		date = IndivScores.getdate(days)

		query = str('SELECT COUNT(*) FROM usecase WHERE persID = ' + str(persID) + ' AND brakeev = TRUE')# AND targetdate >= ' + str(date))
		temp = IndivScores.connect(query, "display")

		if (n[0] != 0):
			result = (temp[0] / n[0])
		else:
			print("No Matching DB Entries!")
			exit()

		return result

	def getCrashVal(persID, days):
		n = IndivScores.getn(persID, days)
		date = IndivScores.getdate(days)

		query = str('SELECT COUNT(*) FROM usecase WHERE persID = ' + str(persID) + ' AND crashev = TRUE')# AND targetdate >= ' + str(date))
		temp = IndivScores.connect(query, "display")

		if (n[0] != 0):
			result = (temp[0] / n[0])
		else:
			print("No Matching DB Entries!")
			exit()

		return result

	'''Functions below calulate positive values – Use Case 3'''
	def getAvgSpeed(persID, days):
		date = IndivScores.getdate(days)

		query = str('SELECT AVG(speed) FROM usecase WHERE persID = ' + str(persID))# + ' AND targetdate >= ' + str(date))
		result = IndivScores.connect(query, "display")

		return result


	'''Functions below calulate positive values – Use Case 2'''
	def getAvgTypeSpeed(typeID, days):
		date = IndivScores.getdate(days)

		query = str('SELECT to_char(AVG(speed)) FROM usecase WHERE typeID = ' + str(typeID))# + ' AND targetdate >= ' + str(date))
		result = IndivScores.connect(query, "display")

		return result

	def getEnginePerf(typeID, days):
		date = IndivScores.getdate(days)

		query = str('SELECT to_char(AVG(performance)) FROM usecase WHERE typeID = ' + str(typeID))# + ' AND targetdate >= ' + str(date))
		result = IndivScores.connect(query, "display")

		return result
