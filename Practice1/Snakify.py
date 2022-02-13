class Exam:
    def __init__(self, courseId, courseTitle):
        self.courseId = courseId
        self.courseTitle = courseTitle

    def detailsPrint(self):
        print("Exam:", self.courseTitle)
        print("Course Id:", self.courseId)

class FinalExam(Exam):
    def __init__(self, courseId, courseTitle, Duration):
        super().__init__(courseId, courseTitle)
        self.Duration = Duration

    def detailsPrint(self):
        print("\nExam:", self.courseTitle)
        print("Course Id:", self.courseId)
        print("Exam Duration:", self.Duration)


Exam1 = Exam("CSE221", "OOP2")
Exam1.detailsPrint()

FinExam = FinalExam("CSE223", "OOP3", "2 Hours")
FinExam.detailsPrint()