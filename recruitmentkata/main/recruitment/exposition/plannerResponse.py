class PlannerResponse:
    def __init__(self, candidate):
        self.recruiter = None
        self.candidate = candidate
        self.date = None

    def getRecruiter(self):
        return self.recruiter

    def setRecruiter(self, recruiter):
        self.recruiter = recruiter

    def getCandidate(self):
        return self.candidate

    def setCandidate(self, candidate):
        self.candidate = candidate

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date