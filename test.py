#!/usr/bin/python
import IndivScores
import json

class test:
    '''Handles DriverScore Function'''
    def main(req):
        json_req = json.loads(req)
        id = json_req["id"]
        days = json_req["days"]
        scoretype = json_req["scoretype"]

        temp = IndivScores.IndivScores(id, days, scoretype)
        output = temp.main()

        return output

if __name__ == '__main__':
    res_raw = {
        'id': 1,
        'days': 1,
        'scoretype': driverscore
    }

    res = json.dumps(res_raw, indent=2)

    main(res)
