class CandidateData():
#ajout xp et skills
    def __init__(self, id, firstName, lastName, xp, skills):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.xp = xp
        self.skills = skills

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getSkills(self):
        return self.skills

    def getYearsXp(self):
        return self.xp



