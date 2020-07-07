#!/usr/bin/python
import IndivScores
import json

class test:

    req_raw = {
        'id': 1,
        'days': 1,
        'scoretype': "driverscore"
    }

    req = json.dumps(req_raw, indent=2)

    json_req = json.loads(req)
    id = json_req["id"]
    days = json_req["days"]
    scoretype = json_req["scoretype"]

    temp = IndivScores.IndivScores(id, days, scoretype)
    output = temp.main()

    print(output)
