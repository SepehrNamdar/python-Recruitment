from main import DateUtils
from main.common.dto.recruiterData import RecruiterData


class RecruitersReferential:

    sylvain = RecruiterData(1, "Sylvain", "Mpungu", 1, ["Java", "Python"])
    sylvain.setAvailabilities(str(DateUtils.today))

    ghiles = RecruiterData(2, "Ghiles", "ELRECRUTADOR", 11, ["Java", "Python"])
    ghiles.setAvailabilities(str(DateUtils.today))


    def findCurrentMonthRecruiters(self):
        recruiters = [self.sylvain, self.ghiles]
        return recruiters