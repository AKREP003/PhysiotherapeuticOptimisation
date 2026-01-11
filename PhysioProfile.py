from sys import path as executionFile



from os import  path

from Body import Body

import pickle

class PhysioProfile:

    def getProfilePath(name : str):

        return path.join(executionFile[0], f"{name}.data")


    def saveBody(body : Body):

        profilePath = PhysioProfile.getProfilePath(body.name)

        pickle.dump(body, open(profilePath, "wb+"))

    def getUserFile(name : str = "default") -> Body:

        profilePath = PhysioProfile.getProfilePath(name)

        if not path.exists(profilePath):
            super().initUserData(name)

        return pickle.load(open(profilePath, "rb"))

    def initUserData(name : str):

        bodyBuffer = Body(name)

        super().saveBody(bodyBuffer)



