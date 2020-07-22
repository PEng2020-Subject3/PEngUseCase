#!/usr/bin/python
from .DriverScores import DriverScores
import json

def handle(req):
    """Handles DriverScore Function"""
    try:
        json_req = json.loads(req)
        sensor_ID = json_req["sensor_ID"]
        method = json_req["function"]
    except:
        return Exception(400, "BadRequest", "Example input:", '{"sensor_ID": "666", "function": "genDriverScore"}')

    temp = DriverScores(method, sensor_ID)
    output = temp.main()

    return output

# Example Input:
# {"sensor_ID": "666", "function": "genDriverScore"}
