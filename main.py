from Body import Body

from Action import Action

from Visualiser import Visualiser

testBody = Body()

testBody.wellnessGoal = [5, 0, 0]

pullAction = Action("pull")

pullAction.weightScalar = 1

testBody.currentProgram = [pullAction]

nextState = testBody.applyProgram(testBody.currentProgram, 0.5)

print(nextState)

v = Visualiser(testBody)

v.animate()

