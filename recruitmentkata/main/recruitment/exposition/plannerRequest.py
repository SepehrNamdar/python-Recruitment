class PlannerRequest():

    def __init__(self, date, candidateId):
        self.date = date
        self. candidateId = candidateId

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getCandidateId(self):
        return self.candidateId

    def setCandidateId(self, candidateId):
        self.candidateId = candidateId
