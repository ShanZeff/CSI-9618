# Task 27.08 Containment

class Course:
    def __init__(self, t, m):   # sets up a new course
        self.__CourseTitle = t                  # DECLARE CourseTitle       : STRING
        self.__MaxStudents = m                  # DECLARE MaxStudents       : INTEGER
        self.__NumberOfLessons = 0              # DECLARE NumberOfLessons   : INTEGER
        self.__CourseLesson = []                # DECLARE CourseLesson[1:50] OF Lesson
        self.__CourseAssessment = Assessment    # DECLARE CourseAssessment  : Assessment

    def AddLesson(self, t, d, r):
        self.__NumberOfLessons = self.__NumberOfLessons + 1
        self.__CourseLesson.append(Lesson(t, d, r))

    def AddAssessment(self, t, m):
        CourseAssessment = Assessment(t, m)

    def OutputCourseDetails(self):
        print(self.__CourseTitle, end=' ')
        print("Maximum number of students: ", self.__MaxStudents)
        for i in range(self.__NumberOfLessons):
            print(self.__CourseLesson[i].OutputLessonDetails())


class Lesson:
    def __init__(self, t, d, r):
        self.__LessonTitle = t      # DECLARE LessonTitle       : STRING
        self.__DurationMinutes = d  # DECLARE DurationMinutes   : INTEGER
        self.__RequiresLab = r      # DECLARE RequiresLab       : BOOLEAN

    def OutputLessonDetails(self):
        print(self.__LessonTitle, self.__DurationMinutes)


class Assessment:
    def __init__(self, t, m):
        self.__AssessmentTitle = t  # DECLARE AssessmentTitle   : STRING
        self.__MaxMarks = m         # DECLARE MaxMarks          : INTEGER

    def OutputAssessmentDetails(self):
        print(self.__AssessmentTitle, " Marks: ", self.__MaxMarks)


def main():
    MyCourse = Course("Computing", 10)          # sets up a new course
    MyCourse.AddAssessment("Programming", 100)  # adds an assignment

    # add 3 lessons
    MyCourse.AddLesson("Problem Solving", 60, False)
    MyCourse.AddLesson("Programming", 120, True)
    MyCourse.AddLesson("Theory", 60, False)

    # check it all works
    MyCourse.OutputCourseDetails()


main()
