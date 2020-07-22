#!/usr/bin/python
from .IndivScores import IndivScores
import json


def handle(req):
"""Handles DriverScore Function"""
    try:
        json_req = json.loads(req)
        sensor_ID = json_req["sensor_ID"]
        scoretype = json_req["scoretype"]
    except:
        print("Bad formatted input %s", req, file=sys.stderr)
        return Exception(400, 'Bad Request', 'Example Input:', '{"sensor_ID": "666","scoretype": "driverscore"}')

    temp = IndivScores(sensor_ID, scoretype)
    output = temp.main()

    return output

# Example Input:
# {"sensor_ID": "666","scoretype": "driverscore"}
