from itertools import accumulate
from typing import List, Dict

from Action import Action

class Body():
    def __init__(self):

        self.currentWellness = [0, 0, 0]

        self.wellnessGoal = [0, 0, 0]

        self.currentProgram : List[Action]

        self.totalWeight = 24

    def applyProgram(self, program: List[Action], delta : float) -> List[int]:

        wellnessBuffer = self.currentWellness.copy()

        for action in program:

            wellnessBuffer = action.contributeBody(wellnessBuffer, delta)

        return wellnessBuffer

    def updateWellness(self, delta : float):

        self.currentWellness = self.applyProgram(self.currentProgram, delta)

    def getRelativeGoal(self):

        goalBuffer = self.wellnessGoal.copy()

        for i in range(len(goalBuffer)-1):
            goalBuffer[i] -= self.currentWellness[i]


        return goalBuffer

    def reweightProgram(self):

        relativeGoal = self.getRelativeGoal()

        alignmentBuffer : Dict[str, float] = {}

        accumulativeWeightBuffer : float = 0

        for action in self.currentProgram:

            alignmentBuffer[action.name] = max(0, action.getAlignment(relativeGoal))

            accumulativeWeightBuffer += alignmentBuffer[action.name]

        self.adjustPrograms(alignmentBuffer, self.totalWeight / accumulativeWeightBuffer)

    def adjustPrograms(self, alignmentBuffer : Dict[str, float], weightUnit : float):

        self.currentProgram = []

        for actionName, weight in alignmentBuffer.items():

            actionBuffer : Action = Action(actionName)

            actionBuffer.weightScalar = weight * weightUnit

            self.currentProgram.append(actionBuffer)

