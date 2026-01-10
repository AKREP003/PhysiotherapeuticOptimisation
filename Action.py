from typing import List, Dict

#Action Data Base

ACTION_DB : Dict[str, List[float]] = {

    "pull" : [1, 0, 0],

    "push" : [-1, 0, 0]

}

class Action:
    def __init__(self, name):

        self.name = name

        self.weightScalar = 0

        self.actionVector = ACTION_DB[self.name]

    #Momentary action-specific transformation

    def contributeBody(self, wellness : List[float] , delta : float) -> List[float]:

        wellnessBuffer = wellness.copy()

        for i in range(len(wellnessBuffer)):

            wellnessBuffer[i] += self.actionVector[i] * delta * self.weightScalar

        return wellnessBuffer

    #dot product scaled by weight

    def getAlignment(self, goal : List[float]):

        buffer : float = 0

        for i in range(len(goal)):
            buffer += self.actionVector[i] * goal[i]

        return buffer
