#!/usr/bin/python
from .PerformanceScores import PerformanceScores
import json

'''Handles PerformanceScore Function'''
def handle(req):
    json_req = json.loads(req)
    typeID = json_req["typeID"]
    method = json_req["function"]

    temp = PerformanceScores(method, typeID)
    output = temp.main()

    return output

# Example input:
# {"typeID": "prius", "function": "genPerformanceScore"}
