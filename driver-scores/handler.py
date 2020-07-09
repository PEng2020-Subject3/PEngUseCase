#!/usr/bin/python
from .DriverScores import DriverScores
import json

'''Handles DriverScore Function'''
def handle(req):
    json_req = json.loads(req)
    persID = json_req["persID"]
    days = json_req["days"]
    method = json_req["function"]

    temp = DriverScores(method, persID, days)
    output = temp.main()

    return output

#Example Input: {"persID": 666,"days": 1,"function": "genDriverScore"}
