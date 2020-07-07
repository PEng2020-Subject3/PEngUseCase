#!/usr/bin/python
from driver-scores.DriverScores import DriverScores
import json

'''Handles DriverScore Function'''
def handle(req):
    json_req = json.loads(req)
    method = json_req["method"]
    persID = json_req["persID"]
    days = json_req["url"]

    temp = DriverScores.DriverScores(method, persID, days)
    output = temp.main()

    return output
