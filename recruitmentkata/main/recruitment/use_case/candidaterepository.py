from main import CandidateData


class CandidateRepository:

    tom = CandidateData(1, "Tom", "Hardy", 2, ["Java", "Python"])
    jessica = CandidateData(2, "Jessica", "Alba", 4, ["VBA", "Java"])
    greg = CandidateData(3, "Greg", "Miakassissa", 3, ["Python"])
    candidates = [tom, jessica,greg]

    def getCandidates(self):
        return self.candidates

    def findCandidateById(self, id):
        for candidate in self.candidates:
            if candidate.id == id:
                return candidate
