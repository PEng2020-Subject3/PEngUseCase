#!/usr/bin/python
from .PerformanceScores import PerformanceScores
import json

'''Handles PerformanceScore Function'''
def handle(req):
    json_req = json.loads(req)
    persID = json_req["persID"]
    days = json_req["days"]
    method = json_req["function"]

    temp = PerformanceScores(method, persID, days)
    output = temp.main()

    return output
