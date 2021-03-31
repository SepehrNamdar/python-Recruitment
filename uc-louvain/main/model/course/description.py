from main.model.course.exceptions.courseCannotBeCreated import CourseCannotBeCreated

# Value Object
class Description:
    def __init__(self,contenu, acquis, methode_evaluation):
        # Validate Domain Object
        if not contenu or not acquis or not methode_evaluation:
            raise CourseCannotBeCreated
        self.contenu = contenu
        self.acquis = acquis
        self.methode_evaluation = methode_evaluation
        self.descriptions =  {"contenu" : contenu,
                             "acquis": acquis,
                              "methode_evaluation": methode_evaluation}

    # Map Domain Object to DTO
    def getSerializedDescriptions(self):
        return {"contenu" : self.contenu,
                "acquis": self.acquis,
                "methode_evaluation": self.methode_evaluation}

    # Equals & Hash Code by attributes
    # TODO