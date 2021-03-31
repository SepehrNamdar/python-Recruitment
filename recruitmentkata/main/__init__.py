from main.common.dateUtils import DateUtils
from main.common.dto.candidateData import CandidateData
from main.common.dto.recruiterData import RecruiterData
from main.common.events import mailEvent
from main.common.events.event import Event
from main.recruitment.model.interview import Interview
from main.recruitment.model.recruiter import Recruiter

from main.recruitment.exposition.plannerRequest import PlannerRequest
from main.recruitment.use_case.interviewPlanner import InterviewPlanner

if __name__ == "__main__":
    request = PlannerRequest(str(DateUtils.today), 1)
    planner = InterviewPlanner()
    response = planner.scheduleInterview(request)
    if response.interview.status == "scheduled":
        event = Event()
        event += mailEvent.mailEvent
        event.notify(response.getRecruiter(), response.getInterview().getDate())
