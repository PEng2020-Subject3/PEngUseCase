#!/usr/bin/env python3
from .PerformanceScores import PerformanceScores
import json
import sys


def handle(req):
    """Handles PerformanceScore Function"""
    try:
        json_req = json.loads(req)
        typeID = json_req["typeID"]
        method = json_req["function"]
    except:
        return Exception(400, "BadRequest", "Example input:", '{"typeID": "prius", "function": "genPerformanceScore"}')

    print("handle request", file=sys.stderr)
    temp = PerformanceScores(method, typeID)
    output = temp.main()

    return output

# Example input:
# {"typeID": "prius", "function": "genPerformanceScore"}
