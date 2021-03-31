from main.model.course.exceptions.courseCannotBeCreated import CourseCannotBeCreated

# Value Object
class Volume:

    def __init__(self, magistraux, pratique):
        if not magistraux or not pratique or magistraux + pratique <= 0 :
            raise CourseCannotBeCreated
        self.magistraux = magistraux
        self.pratique = pratique
        self.volumes  = {"magistraux" : magistraux,
                      "pratique" : pratique}

    # Mapper
    def getSerializedVolumes(self):
        return {"magistraux" : self.magistraux,
                "pratique" : self.pratique}

    # TODO : Equals & Hash code

