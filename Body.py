from typing import List

from Action import Action

class Body():
    def __init__(self):

        self.currentWellness = [0, 0, 0]

        self.wellnessGoal = [0, 0, 0]

        self.currentProgram : List[Action]

    def applyProgram(self, program: List[Action], delta : float) -> List[int]:

        wellnessBuffer = self.currentWellness.copy()

        for action in program:

            wellnessBuffer = action.contributeBody(wellnessBuffer, delta)

        return wellnessBuffer