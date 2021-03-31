from main.recruitment.exposition.plannerResponse import PlannerResponse
#Application Service
#Ne voit que Candidat Repository
from main.recruitment.model.candidate import Candidate
from main.recruitment.model.interview import Interview
from main.recruitment.use_case.icandidateRepository import ICandidateRepository
from main.recruitment.use_case.irecruitersReferential import IRecruitersReferential


class InterviewPlanner:

    def __init__(self):
        self.interview = Interview()
        self.candidates = ICandidateRepository()
        self.recruiters = IRecruitersReferential()


    def scheduleInterview(self, request):
        candidate = self.candidates.findCandidateById(request.getCandidateId())
        recruiters = self.recruiters.findCurrentMonthRecruiters()
        pertinentRecruiters = []

        for recruiter in recruiters:
            if Candidate().canBeTested(candidate, recruiter):
                pertinentRecruiters.append(recruiter)

        self.interview.plan(request.getDate(), pertinentRecruiters)

        response = PlannerResponse(candidate)
        response.setDate(self.interview.getDate())
        response.setRecruiter(self.interview.getRecruiterName())
        return response