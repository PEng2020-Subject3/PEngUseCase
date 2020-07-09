#!/usr/bin/python
from .DriverScores import DriverScores
import json

'''Handles DriverScore Function'''
def handle(req):
    json_req = json.loads(req)
    persID = json_req["persID"]
    method = json_req["function"]

    temp = DriverScores(method, persID)
    output = temp.main()

    return output

# Example Input: 
# {"persID": 666, "function": "genDriverScore"}
