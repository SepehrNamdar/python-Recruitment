class Candidate:
#Ne devrait pas être visible par les autres objets

    def canBeTested(self, candidate, recruiter):
        for skill in candidate.skills:
            if not skill in recruiter.skills or candidate.xp > recruiter.xp:
                return False
            return True