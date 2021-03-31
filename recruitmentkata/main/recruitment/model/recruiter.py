from main.recruitment.model.noRecruitersAvailable import NoRecruitersAvailable

class Recruiter:
	def findAvailable(self, recruiters, requestedDate):
		if not recruiters:
			raise NoRecruitersAvailable()
		else:
			availableRecruiters = []
			for recruiter in recruiters:
				if requestedDate in recruiter.availabilities:
					availableRecruiters.append(recruiter)
			return availableRecruiters



			
