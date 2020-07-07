#!/usr/bin/python
from .PerformanceScores import PerformanceScores
import json

'''Handles PerformanceScore Function'''
def handle(req):
    json_req = json.loads(req)
    method = json_req["method"]
    persID = json_req["persID"]
    days = json_req["days"]

    #output should be a JSON with typeID, days and performancescore
    temp = PerformanceScores.PerformanceScores(method, persID, days)
    output = temp.main()

    return output
