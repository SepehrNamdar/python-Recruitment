from main.common.events import mailEvent
from main.common.events.event import Event
from main.model.course.course import Course

# Application Service
class CreateCourse:

    def __init__(self, request, courses, teachers):
        self.request = request
        self.course = None
        self.courseData = None
        self.courses = courses
        self.teachers = teachers

    def create(self):
        # GIVEN
        teacherData = self.teachers.findTeacherById(self.request.profilId)

        # WHEN
        self.course = Course(self.request, teacherData)
        self.course = self.course.createCourse()

        # THEN
        self.courseData = self.course.getCourseData()
        self.courses.addCourse(self.courseData)
        if self.course.status == "created":
            event = Event()
            event += mailEvent.mailEvent
            event.notify(self.course.teacher.profilId, self.course.courseId, self.course.teacher.faculty)