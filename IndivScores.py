#!/usr/bin/python
from configparser import ConfigParser
import psycopg2


'''This class calculates individual scores based on information received from a database that can be further processed.'''
class IndivScores(object):
	def __init__(self):

		'''
		TODO:

		determine goal date here for sql request
		'''

		print("Individual Scores: Initialized.")

	def main():
		IndivScores.config()
		
		
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

	def connect(query):
	    """ Connect to the PostgreSQL database server """
	    conn = None
	    try:
	        # read connection parameters
	        params = IndivScores.config()

	        # connect to the PostgreSQL server
	        #print('Connecting to the PostgreSQL database...')
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
	            #print('Database connection closed.')


	'''Get total amount of values, while values are received every 30 seconds'''
	def getn(persID):#, date):
		query = str('SELECT COUNT(*) FROM usecase WHERE persID = ' + str(persID)) #' AND date >= ' + str(date) 
		temp = IndivScores.connect(query)
		print(temp)
		return 30

	'''Functions below calculate value between 0 and 1 – Use Cases 1 & 3'''
	def getSpeedVal(persID, date):
		query = str('SELECT COUNT(*) FROM usecase WHERE persID =' + persID)
		temp = IndivScores.connect(query)
		print(temp)
		return 0.5

	def getTurnVal(persID, date):
		return 0.5

	def getBrakeVal(persID, date):
		return 0.5

	def getCrashVal(persID, date):
		return 0.5

	'''Functions below calulate positive values – Use Case 3'''
	def getAvgSpeed(persID, date):
		return 50

	'''Functions below calulate positive values – Use Case 2'''
	def getAvgTypeSpeed(typeID, date):
		return 36

	def getEnginePerf(typeID, date):
		return 89

if __name__ == '__main__':
	IndivScores.main()