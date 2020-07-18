#!/usr/bin/env python3
from .IndivScores import IndivScores
import json
import sys


def handle(req):
    """Handles indiv-performancescores Function"""
    try:
        json_req = json.loads(req)
        id = json_req["id"]
        scoretype = json_req["scoretype"]
    except:
        print("Bad formatted input %s", req, file=sys.stderr)
        return Exception(400, 'Bad Request', 'Example Input:', '{"id": "prius","scoretype": "performancescore"}')

    temp = IndivScores(id, scoretype)
    output = temp.main()

    return output

# Example Input:
# {"id": "prius","scoretype": "performancescore"}
