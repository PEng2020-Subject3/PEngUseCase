#!/usr/bin/env python3
from __future__ import division
from configparser import ConfigParser
import psycopg2
import json
import os
import sys


class IndivScores(object):
    """
    This class calculates individual scores based on information received from a
    database that can be further processed.
    """

    def __init__(self, sensor_ID, scoretype):
        self.sensor_ID = sensor_ID
        self.scoretype = scoretype

    def main(self):
        self.initTables()

        if (self.scoretype == "performancescore"):
            return self.getPerfscoreData()
        elif (self.scoretype == "driverscore"):
            return self.getDriverscoreData()
        else:
            print("Undefined Data Requested.", file=sys.stderr)
            exit()

    def config(self):
        """Configure Database Access using Environment variables"""
        # based on https://www.postgresqltutorial.com/postgresql-python/connect/

        # get configuration from env or use default
        db_host = str(os.getenv('db_host', 'usecase-postgres-db-postgresql'))
        db_name = str(os.getenv('db_name', 'postgres'))
        db_user = str(os.getenv('db_user', 'postgres'))
        db_password = str(os.getenv('db_password', '3BDAJjFHOA'))

        db = {
            "host": db_host,
            "database": db_name,
            "user": db_user,
            "password": db_password
        }

        return db


    def connect(self, query, mode):
        """Connect to the PostgreSQL database server"""
        # based on https://www.postgresqltutorial.com/postgresql-python/connect/

        conn = None
        try:
            # read connection parameters and connect to db
            params = self.config()
            conn = psycopg2.connect(**params)

            # create a cursor and execute a statement
            cur = conn.cursor()
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


    def getDriverscoreData(self):

        self.speedscore = self.getSpeedVal()
        self.turnscore = self.getTurnVal()
        self.brakescore = self.getBrakeVal()
        self.crashscore = self.getCrashVal()
        self.avgspeed = self.getAvgSpeed()

        return self.packdriveJSON()

    def getPerfscoreData(self):

        self.logs = self.getn()
        self.speedscore = self.getSpeedVal()
        self.turnscore = self.getTurnVal()
        self.brakescore = self.getBrakeVal()
        self.crashscore = self.getCrashVal()
        self.avgspeed = self.getAvgSpeed()
        self.engperf = self.getEnginePerf()

        return self.packperfJSON()

    def packdriveJSON(self):
        """Packs JSON with use case-specific data """

        res_raw = {
            'speedscore': self.speedscore,
            'turnscore': self.turnscore,
            'brakescore': self.brakescore,
            'crashscore': self.crashscore,
            'avgspeed': self.avgspeed
        }

        res = json.dumps(res_raw, indent=2)

        return res

    def packperfJSON(self):
        """Packs JSON with use case-specific data """

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

        query = str("CREATE TABLE IF NOT EXISTS usecase (sensor_ID varchar (50) PRIMARY KEY,speed int,performance int,speedev boolean,brakeev boolean,turnev boolean,crashev boolean,targetdate date NOT NULL);")
        self.connect(query, "create")
        query = "INSERT INTO usecase (sensor_ID, speed, performance, speedev, brakeev, turnev, crashev, targetdate) VALUES ('prius', 33, 99, true, false, true, false, '1997-02-27') ON CONFLICT DO NOTHING;"
        self.connect(query, "insert")

    def getn(self):
        """Get total amount of values, while values are received every XX seconds"""

        query = str("SELECT COUNT(*) FROM usecase WHERE sensor_ID = '" + str(self.sensor_ID) + "';")
        result = self.connect(query, "display")

        return result[0]

    """
    Functions below calculate values between 0 and 1
    """
    def getSpeedVal(self):
        n = self.getn()

        query = str("SELECT COUNT(*) FROM usecase WHERE sensor_ID = '" + str(self.sensor_ID) + "'AND speedev = TRUE;")
        temp = self.connect(query, "display")

        if (n != 0):
            result = (temp[0] / n)
        else:
            print("No Matching DB Entries!", file=sys.stderr)
            exit()

        return result

    def getTurnVal(self):
        n = self.getn()

        query = str("SELECT COUNT(*) FROM usecase WHERE sensor_ID = '" + str(self.sensor_ID) + "'AND turnev = TRUE;")
        temp = self.connect(query, "display")

        if (n != 0):
            result = (temp[0] / n)
        else:
            print("No Matching DB Entries!", file=sys.stderr)
            exit()

        return result

    def getBrakeVal(self):
        n = self.getn()

        query = str("SELECT COUNT(*) FROM usecase WHERE sensor_ID = '" + str(self.sensor_ID) + "'AND brakeev = TRUE;")
        temp = self.connect(query, "display")

        if (n != 0):
            result = (temp[0] / n)
        else:
            print("No Matching DB Entries!", file=sys.stderr)
            exit()

        return result

    def getCrashVal(self):
        n = self.getn()

        query = str("SELECT COUNT(*) FROM usecase WHERE sensor_ID = '" + str(self.sensor_ID) + "'AND crashev = TRUE;")
        temp = self.connect(query, "display")

        if (n != 0):
            result = (temp[0] / n)
        else:
            print("No Matching DB Entries!", file=sys.stderr)
            exit()

        return result

    def getAvgSpeed(self):

        query = str("SELECT AVG(speed) FROM usecase WHERE sensor_ID = '" + str(self.sensor_ID) + "';")
        temp = self.connect(query, "display")
        result = int(temp[0])

        return result

    """
    Function below calculates positive values – Use Case 2
    """
    def getEnginePerf(self):

        query = str("SELECT AVG(performance) FROM usecase WHERE sensor_ID = '" + str(self.sensor_ID) + "';")
        temp = self.connect(query, "display")
        result = int(temp[0])

        return result
