#!/usr/bin/env python3
from .IndivScores import IndivScores
import json
import sys


def handle(req):
    """Handles indiv-performancescores Function"""
    try:
        json_req = json.loads(req)
        sensor_ID = json_req["sensor_ID"]
        scoretype = json_req["scoretype"]
    except:
        print("Bad formatted input %s", req, file=sys.stderr)
        return Exception(400, 'Bad Request', 'Example Input:', '{"sensor_ID": "prius","scoretype": "performancescore"}')

    temp = IndivScores(sensor_ID, scoretype)
    output = temp.main()

    return output

# Example Input:
# {"sensor_ID": "prius","scoretype": "performancescore"}
