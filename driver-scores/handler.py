#!/usr/bin/python
from .DriverScores import DriverScores
import json

'''Handles DriverScore Function'''
def handle(req):
    json_req = json.loads(req)
    method = json_req["method"]
    persID = json_req["persID"]
    days = json_req["days"]

    #output should be a JSON with persID, days and driverscore
    temp = DriverScores.DriverScores(method, persID, days)
    output = temp.main()

    return output
