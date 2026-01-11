from Body import Body

from Action import Action

from Visualiser import Visualiser

from PhysioProfile import PhysioProfile

testBody = Body()

testBody.wellnessGoal = [5, 0, 0]

testBody.currentWellness = [0, 0, 0]

testBody.totalWeight = 2

testBody.currentProgram = [Action("pull"), Action("push")]

testBody.reweightProgram()

for i in testBody.currentProgram:

    print(i.name)

    print(i.weightScalar)


PhysioProfile.saveBody(testBody)

print(PhysioProfile.getUserFile().name)

print(testBody)

exit()

v = Visualiser(testBody)

v.animate()

