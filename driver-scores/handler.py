#!/usr/bin/python
from .DriverScores import DriverScores
from .IndivScores import IndivScores
import json

'''Handles DriverScore Function'''
def handle(req):
    json_req = json.loads(req)
    persID = json_req["persID"]
    method = json_req["function"]

    temp = DriverScores(method, persID)
    output = temp.main()

    json_req = json.loads(output)
    id = json_req["id"]
    scoretype = json_req["scoretype"]

    temp = IndivScores(id, scoretype)
    output = temp.main()

    return output

# Example Input:
# {"persID": 666, "function": "genDriverScore"}
