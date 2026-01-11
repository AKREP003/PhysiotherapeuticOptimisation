from typing import List, Dict

#Action Data Base

ACTION_DB : Dict[str, List[float]] = {

    "pull" : [1, 0, 0],

    "push" : [-1, 0, 0]

}

ACTION_DESC : Dict[str, str] = {

    "pull" : "Pull Action",

    "push" : "Push Action"

}

class Action:
    def __init__(self, name):

        self.name = name

        self.weightScalar : float = 0

        self.actionVector : List[float] = ACTION_DB[self.name]

        self.desc : str = ACTION_DESC[self.name]

    #Momentary action-specific transformation

    def contributeBody(self, wellness : List[float] , delta : float) -> List[float]:

        wellnessBuffer = wellness.copy()

        for i in range(len(wellnessBuffer)):

            wellnessBuffer[i] += self.actionVector[i] * delta * self.weightScalar

        return wellnessBuffer

    #dot product scaled by weight

    def getAlignment(self, goal : List[float]) -> List[float]:

        buffer : float = 0

        for i in range(len(goal)):
            buffer += self.actionVector[i] * goal[i]

        return buffer
