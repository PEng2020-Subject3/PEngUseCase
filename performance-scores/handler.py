#!/usr/bin/env python3
from .PerformanceScores import PerformanceScores
import json
import sys


def handle(req):
    """Handles PerformanceScore Function"""
    try:
        json_req = json.loads(req)
        sensor_ID = json_req["sensor_ID"]
        method = json_req["function"]
    except:
        return Exception(400, "BadRequest", "Example input:", '{"sensor_ID": "prius", "function": "genPerformanceScore"}')

    temp = PerformanceScores(method, sensor_ID)
    output = temp.main()

    return output

# Example input:
# {"sensor_ID": "prius", "function": "genPerformanceScore"}
