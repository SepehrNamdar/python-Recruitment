class RecruiterData():

    def __init__(self, id, firstName, lastName, xp, skills):
        self.availabilities = []
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.xp = xp
        self.skills = skills


    def getAvailabilitie(self):
        return self.availabilities

    def setAvailabilities(self, availabilities):
        self.availabilities = availabilities

    def getName(self):
        return self.firstName + " " + self.lastName