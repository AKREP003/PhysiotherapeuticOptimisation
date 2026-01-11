from sys import path as executionFile



from os import  path

from Body import Body

import pickle

class PhysioProfile:

    def getProfilePath(name : str) -> str:

        return path.join(executionFile[0], f"{name}.data")


    def saveBody(body : Body):

        profilePath = PhysioProfile.getProfilePath(body.name)

        pickle.dump(body, open(profilePath, "wb+"))

    def getUserFile(name : str = "default") -> Body:

        profilePath = PhysioProfile.getProfilePath(name)

        if not path.exists(profilePath):
            PhysioProfile.initUserData(name)

        return pickle.load(open(profilePath, "rb"))

    def initUserData(name : str):

        bodyBuffer = Body(name)

        PhysioProfile.saveBody(bodyBuffer)

    def ifExists(name : str = "default") -> bool:
        profilePath = PhysioProfile.getProfilePath(name)

        return path.exists(profilePath)

