#!/usr/bin/env python3
from urllib.request import urlopen
from socket import timeout
import json
import os
import sys


class PerformanceScores(object):
    """
    Functions in this class create a json containing respective information
    """

    def __init__(self, method, sensor_ID):
        self.method = method
        self.sensor_ID = sensor_ID

    def main(self):
        if self.method == "genPerformanceScore":
            return self.genPerformanceScore()
        else:
            print("Unknown Method!")

    def getData(self):
        """Pack and send request to indiv-scores....py and receive response with requested data"""
        req_raw = {
            'sensor_ID': self.sensor_ID,
            'scoretype': 'performancescore'
        }

        req = json.dumps(req_raw, indent=2)

        binary_req = req.encode('utf-8')

        try:
            policy = str(os.environ['openfaas.policy.name'])
            print('invoking indiv-performancescores with policy: %s', policy, file=sys.stderr)
            url = str("http://gateway.openfaas:8080/function/indiv-performancescores?policy=" + str(policy))
        except:
            url = str("http://gateway.openfaas:8080/function/indiv-performancescores")

        print('invoking indiv-performancescores', file=sys.stderr)
        try:
            # if it does not respond in time, the function might be just deployed
            rv = urlopen(url, data=binary_req, timeout=10)
        except timeout:
            # try again - the function should respond now
            rv = urlopen(url, data=binary_req)
        temp = rv.read().decode('utf-8')
        res = json.loads(temp)
        rv.close()

        self.logs = res["logs"]
        self.speedscore = res["speedscore"]
        self.turnscore = res["turnscore"]
        self.brakescore = res["brakescore"]
        self.crashscore = res["crashscore"]
        self.avgspeed = res["avgspeed"]
        self.engperf = res["engperf"]

    def genPerformanceScore(self):
        """Output Data – Use Case 3"""
        self.getData()

        uc_2raw = {
            'general': {
                'sensor_ID': self.sensor_ID,
                'logs': self.logs
            },
            'scores': {
                'performancescore': self.engperf,
                'speedscore': self.speedscore,
                'turnscore': self.turnscore,
                'brakescore': self.brakescore,
                'crashscore': self.crashscore,
                'avgspeed': self.avgspeed
            }
        }

        uc_2 = json.dumps(uc_2raw, indent=2)

        return uc_2
