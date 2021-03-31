from main.recruitment.use_case.recruitersReferential import RecruitersReferential


class IRecruitersReferential:
    def findCurrentMonthRecruiters(self):
        return RecruitersReferential().findCurrentMonthRecruiters()