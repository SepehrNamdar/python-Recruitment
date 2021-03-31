from main.common.dto.courseData import CourseData
from main.model.course.exceptions.teacherCannotCreateCourse import TeacherCannotCreateCourse
from main.model.course.idGenerator import IdGenerator


#Aggregate Root
# Entity
class Course:

    def __init__(self, request, teacherData):
        self.courseId = None
        self.teacher = teacherData.getTeacher()
        self.descriptions = request.descriptions
        self.volumes = request.volumes
        self.status = "uncreated"
        self.faculty = teacherData.getFaculty()

    # Equals on id
    def equals(self, course):
        return self.courseId == course.courseId

    def createCourse(self):
        self.courseId = IdGenerator().create_unique_id(self.teacher.faculty)
        if not self.teacher.canCreateCourse(self.courseId):
            raise TeacherCannotCreateCourse()
        self.status = "created"
        return self

    # Mapper : Map Domain object to DTO
    def getCourseData(self):
        return CourseData(self.courseId, self.teacher, self.descriptions, self.volumes)
