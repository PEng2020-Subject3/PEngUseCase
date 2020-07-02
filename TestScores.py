from DriverScores import DriverScores
from IndivScores import IndivScores
import DriverScores

class TestScores:
    output = DriverScores.DriverScores("genDriverScore", 2, 2)
    temp = output.main()

    output2 = DriverScores.DriverScores("genDriverScoreWeek", 2, 2)
    temp2 = output2.main()


    print("Hier bims ich DriverScore: " + temp)
    print("Hier bims ich DriverScoreWeek: " + temp2)
