# Entity
class Teacher:
    def __init__(self, profilId, faculty):
        self.profilId = profilId
        self.faculty = faculty

    # Domain behaviour
    def canCreateCourse(self, idCourse):
        if self.faculty == idCourse[0]:
            return True
        return False

    # TODO : Equals & Hash Code