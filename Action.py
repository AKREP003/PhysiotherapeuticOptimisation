from typing import List

#Action Data Base

ACTION_DB = {

    "pull" : [1, 0, 0],

    "push" : [-1, 0, 0]

}

class Action:
    def __init__(self, name):

        self.name = name

        self.weightScalar = 0

        self.actionVector = ACTION_DB[self.name]

    #Momentary action-specific transformation

    def contributeBody(self, wellness : List[float] , delta : float) -> List[int]:

        wellnessBuffer = wellness.copy()

        for i in range(len(wellnessBuffer)):

            wellnessBuffer[i] += self.actionVector[i] * delta * self.weightScalar

        return wellnessBuffer

