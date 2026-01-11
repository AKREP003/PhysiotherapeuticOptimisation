from time import sleep

from turtle import *

from Body import Body

class Visualiser:

    def __init__(self, body : Body, dimensions : tuple = (0, 1), scale : float = 20, pivot : tuple = (0, 0), delta : float = 1):

        self.body = body

        self.dimensions = dimensions

        self.scale = scale

        self.pivot = pivot

        self.delta = delta

        self.initPos = (
            self.body.currentWellness[dimensions[0]] * self.scale,
            self.body.currentWellness[dimensions[1]] * self.scale
        )

        self.currentPos = self.initPos

        self.goalPos = (
            self.body.wellnessGoal[dimensions[0]] * self.scale,
            self.body.wellnessGoal[dimensions[1]] * self.scale
        )

    def gotoCurrent(self):

        self.currentPos = (
            self.body.currentWellness[self.dimensions[0]] * self.scale,
            self.body.currentWellness[self.dimensions[1]] * self.scale
        )

        goto(self.pivot[0] + self.currentPos[0], self.pivot[1] + self.currentPos[1])



    def animInit(self):

        penup()

        goto(self.pivot[0] + self.initPos[0], self.pivot[1] + self.initPos[1] - 20)

        pendown()

        circle(20, steps=20)

        penup()

        goto(self.pivot[0] + self.goalPos[0], self.pivot[1] + self.goalPos[1] - 20)

        pendown()

        circle(20, steps=20)

        penup()

        goto(self.pivot[0] + self.initPos[0], self.pivot[1] + self.initPos[1])

        pendown()

    def exerciseStep(self):

        self.body.updateWellness(self.delta)

        self.gotoCurrent()



    def animate(self):

        self.animInit()

        while (True):

            self.body.reweightProgram()

            self.exerciseStep()



        mainloop()
