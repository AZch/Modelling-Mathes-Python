import numpy

class Game():
    def __init__(self, homeGoals, homeShots, homeRange, awayGoals, awayShots, awayRange, maxNumRand = 10000):
        self.__homeGoals = homeGoals
        self.__homeShots = homeShots
        self.__homeRange = homeRange

        self.__awayGoals = awayGoals
        self.__awayShots = awayShots
        self.__awayRange = awayRange
        self.__randomNum = lambda: int(round(numpy.random.uniform(0, maxNumRand), 1))
        self.__rangeForScore = lambda difScore, rangeData: 0 if len(rangeData) != 5 else \
                                                        rangeData[0] if difScore > 1 else  \
                                                        rangeData[1] if difScore == 1 else \
                                                        rangeData[2] if difScore == 0 else \
                                                        rangeData[3] if difScore == -1 else \
                                                        rangeData[4] if difScore < -1 else 0

    def __call__(self, *args):
        currentFirstScore = 0
        currentSecondScore = 0
        for i in range(0, 90):
            currentRange = currentFirstScore - currentSecondScore
            for valId in range(len(self.__homeShots)):
                currentFirstScore += self.__addGoalsMinutes(self.__homeShots[valId],
                                                            self.__homeGoals[valId],
                                                            currentRange,
                                                            self.__homeRange)
                currentSecondScore += self.__addGoalsMinutes(self.__awayShots[valId],
                                                            self.__awayGoals[valId],
                                                            currentRange * -1,
                                                            self.__awayRange)

        return currentFirstScore, currentSecondScore


    def __addGoalsMinutes(self, shots, goals, currentRange, dataRange):
        if self.__randomNum() * self.__rangeForScore(currentRange, dataRange) <= shots:
            if self.__randomNum() <= goals:
                return 1
        return 0

