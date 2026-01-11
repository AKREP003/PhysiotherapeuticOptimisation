from typing import List, Dict

from Action import Action

from datetime import date

class Body():
    def __init__(self, name : str = "default"):

        self.name : str = name

        self.currentWellness : List[float] = [0, 0, 0]

        self.wellnessGoal : List[float] = [0, 0, 0]

        self.currentProgram : List[Action]

        self.totalWeight : float = 24

        self.startDate: date = date.today()

    def applyProgram(self, program: List[Action], delta : float) -> List[int]:

        wellnessBuffer = self.currentWellness.copy()

        for action in program:

            wellnessBuffer = action.contributeBody(wellnessBuffer, delta)

        return wellnessBuffer

    def updateWellness(self, delta : float):

        self.currentWellness = self.applyProgram(self.currentProgram, delta)

    def getRelativeGoal(self) -> List[float]:

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

        self.currentProgram : List[Action] = []

        for actionName, weight in alignmentBuffer.items():

            actionBuffer : Action = Action(actionName)

            actionBuffer.weightScalar = weight * weightUnit

            self.currentProgram.append(actionBuffer)
