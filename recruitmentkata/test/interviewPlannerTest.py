import unittest
from main import DateUtils
from main.recruitment.exposition.plannerRequest import PlannerRequest
from main.recruitment.use_case.interviewPlanner import InterviewPlanner


class InterviewPlannerTest(unittest.TestCase):

    def test_should_plan_an_interview(self):
        request = PlannerRequest(str(DateUtils.today), 1)
        planner = InterviewPlanner()
        response = planner.scheduleInterview(request)
        self.assertEqual(response.interview.status, 'scheduled')

if __name__ == '__main__':
    unittest.main()