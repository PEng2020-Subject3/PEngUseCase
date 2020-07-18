#!/usr/bin/env python3
from __future__ import division
from configparser import ConfigParser
import psycopg2
import json
import os
import sys


class IndivScores(object):
    """
    This class calculates individual scores based on information received from a database that can be further
    processed.
    """

    def __init__(self, id, scoretype):
        self.id = id
        self.scoretype = scoretype

    def main(self):
        self.initTables()

        if (self.scoretype == "performancescore"):
            return self.getPerfscoreData()
        else:
            print("Undefined Data Requested.", file=sys.stderr)
            exit()

    # based on https://www.postgresqltutorial.com/postgresql-python/connect/
    def config(filename='database.ini', section='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)
        db_host = str(os.environ['db_host'])
        db_name = str(os.environ['db_name'])
        db_user = str(os.environ['db_user'])
        db_password = str(os.environ['db_password'])

        # get section, default to postgresql
        db = {
            "host": db_host,
            "database": db_name,
            "user": db_user,
            "password": db_password
        }

        return db

    # based on https://www.postgresqltutorial.com/postgresql-python/connect/
    def connect(query, mode):
        """Connect to the PostgreSQL database server"""
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

            if mode == "display":
                # display the PostgreSQL database server version
                db_version = cur.fetchone()
            else:
                conn.commit()

            return db_version

        except (Exception, psycopg2.DatabaseError) as error:
            print(error, file=sys.stderr)
        finally:
            if conn is not None:
                conn.close()

    def getPerfscoreData(self):
        """Packs JSON with use case-specific data """
        self.logs = self.getn()
        self.speedscore = self.getSpeedVal()
        self.turnscore = self.getTurnVal()
        self.brakescore = self.getBrakeVal()
        self.crashscore = self.getCrashVal()
        self.avgspeed = self.getAvgSpeed()
        self.engperf = self.getEnginePerf()

        return self.packJSON()

    def packJSON(self):
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
        print(res, file=sys.stderr)
        return res

    def initTables(self):
        """Create tables if they do not exist yet"""
        query = str("CREATE TABLE IF NOT EXISTS usecase (persID int PRIMARY KEY,typeID varchar (50) NOT NULL,speed int,performance int,speedev boolean,brakeev boolean,turnev boolean,crashev boolean,targetdate date NOT NULL);")
        IndivScores.connect(query, "create")

    def getn(self):
        """Get total amount of values, while values are received every XX seconds"""
        query = str("SELECT COUNT(*) FROM usecase WHERE typeID = '" + str(self.id) + "';")
        result = IndivScores.connect(query, "display")

        return result[0]

    def getSpeedVal(self):
        """Functions below calculate values between 0 and 1 – Use Cases 1 & 3"""
        n = self.getn()

        query = str("SELECT COUNT(*) FROM usecase WHERE typeID = '" + str(self.id) + "'AND speedev = TRUE;")
        temp = IndivScores.connect(query, "display")

        if (n != 0):
            result = (temp[0] / n)
        else:
            print("No Matching DB Entries!", file=sys.stderr)
            exit()

        return result

    def getTurnVal(self):
        n = self.getn()

        query = str("SELECT COUNT(*) FROM usecase WHERE typeID = '" + str(self.id) + "'AND turnev = TRUE;")
        temp = IndivScores.connect(query, "display", file=sys.stderr)

        if (n != 0):
            result = (temp[0] / n)
        else:
            print("No Matching DB Entries!", file=sys.stderr)
            exit()

        return result

    def getBrakeVal(self):
        n = self.getn()

        query = str("SELECT COUNT(*) FROM usecase WHERE typeID = '" + str(self.id) + "'AND brakeev = TRUE;")
        temp = IndivScores.connect(query, "display")

        if (n != 0):
            result = (temp[0] / n)
        else:
            print("No Matching DB Entries!", file=sys.stderr)
            exit()

        return result

    def getCrashVal(self):
        n = self.getn()

        query = str("SELECT COUNT(*) FROM usecase WHERE typeID = '" + str(self.id) + "'AND crashev = TRUE;")
        temp = IndivScores.connect(query, "display")

        if (n != 0):
            result = (temp[0] / n)
        else:
            print("No Matching DB Entries!", file=sys.stderr)
            exit()

        return result

    def getAvgSpeed(self):

        query = str("SELECT AVG(speed) FROM usecase WHERE typeID = '" + str(self.id) + "';")
        temp = IndivScores.connect(query, "display")
        result = int(temp[0])

        return result

    def getEnginePerf(self):
        """Function below calculate positive values – Use Case 3"""
        query = str("SELECT AVG(performance) FROM usecase WHERE typeID = '" + str(self.id) + "';")
        temp = IndivScores.connect(query, "display")
        result = int(temp[0])

        return result
