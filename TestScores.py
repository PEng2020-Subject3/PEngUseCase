from DriverScores import DriverScores
from IndivScores import IndivScores
from PerformanceScores import PerformanceScores
import DriverScores

class TestScores:
    output = DriverScores.DriverScores("genDriverScore", 2, 2)
    temp = output.main()

    output2 = DriverScores.DriverScores("genDriverScoreWeek", 2, 2)
    temp2 = output2.main()

    output3 = PerformanceScores("genPerformanceScore", 2, 2)
    temp3 = output3.main()


    print("DriverScore: " + temp)
    print("DriverScoreWeek: " + temp2)
    print("PerformanceScores: " + temp3)
