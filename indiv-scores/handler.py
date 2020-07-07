#!/usr/bin/python
from indiv-scores.IndivScores import IndivScores
import json

'''Handles DriverScore Function'''
def handle(req):
    json_req = json.loads(req)
    id = json_req["id"]
    days = json_req["days"]
    scoretyepe = json_req["scoretype"]

    temp = IndivScores.IndivScores(id, days, scoretype)
    output = temp.main()

    return output
