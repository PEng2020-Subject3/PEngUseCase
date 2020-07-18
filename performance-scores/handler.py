#!/usr/bin/env python3
from .PerformanceScores import PerformanceScores
import json


def handle(req):
    """Handles PerformanceScore Function"""
    try:
        json_req = json.loads(req)
        typeID = json_req["typeID"]
        method = json_req["function"]
    except:
        return Exception(400, "BadRequest", "Example input:", '{"typeID": "prius", "function": "genPerformanceScore"}')

    temp = PerformanceScores(method, typeID)
    output = temp.main()

    return output

# Example input:
# {"typeID": "prius", "function": "genPerformanceScore"}
