#!/usr/bin/python
from .IndivScores import IndivScores
import json

'''Handles indiv-performancescores Function'''
def handle(req):
    json_req = json.loads(req)
    id = json_req["id"]
    scoretype = json_req["scoretype"]

    temp = IndivScores(id, scoretype)
    output = temp.main()

    return output

# Example Input:
# {"id": "prius","scoretype": "performancescores"}
