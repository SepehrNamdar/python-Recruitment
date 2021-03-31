#Lecture du Hashmap --- Facade
from main.recruitment.use_case.candidaterepository import CandidateRepository


class ICandidateRepository:

    def findCandidateById(self, uuid):
        return CandidateRepository().findCandidateById(uuid)

    def getCandidates(self):
        return CandidateRepository().getCandidates()

