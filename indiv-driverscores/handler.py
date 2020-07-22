#!/usr/bin/python
from .IndivScores import IndivScores
import json

'''Handles DriverScore Function'''
def handle(req):
    json_req = json.loads(req)
    sensor_ID = json_req["sensor_ID"]
    scoretype = json_req["scoretype"]

    temp = IndivScores(sensor_ID, scoretype)
    output = temp.main()

    return output

# Example Input:
# {"sensor_ID": 666,"scoretype": "driverscore"}
