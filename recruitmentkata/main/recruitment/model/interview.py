from main.recruitment.model.noRecruitersAvailable import NoRecruitersAvailable
from main.recruitment.model.recruiter import Recruiter


class Interview :

	status = "unscheduled"
	recruiterName = ""
	date = None

	def plan(self, requestedDate, recruiters):
		recruiter = Recruiter()
		availaleRecruiters = recruiter.findAvailable(recruiters, requestedDate)

		if not availaleRecruiters:
			raise NoRecruitersAvailable()

		firstAvailableRecruiter = availaleRecruiters[0]
		self.recruiterName = firstAvailableRecruiter.getName()
		self.status = "scheduled"
		self.date = requestedDate
		return self

	def getStatus(self):
		return self.status

	def getDate(self):
		return self.date

	def getCandidateName(self):
		return None

	def getRecruiterName(self):
		return self.recruiterName




