class StudentInfo:

    def __init__(self, student_rollno, student_name):
        self.student_rollno = student_rollno
        self.student_name = student_name


class StudentMarks:

    def __init__(self, student_rollno, student_marks_one,
                 student_marks_two, student_marks_three):
        self.student_rollno = student_rollno
        self.student_marks_one = student_marks_one
        self.student_marks_two = student_marks_two
        self.student_marks_three = student_marks_three


class Main:

    @staticmethod
    def getGrade(marks1, marks2, marks3):

        if marks1 > 100 or marks2 > 100 or marks3 > 100:
            return None, "Invalid Marks"

        avg = (marks1 + marks2 + marks3) / 3

        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 40:
            grade = "D"
        else:
            grade = "Fail"

        return avg, grade

    def __init__(self):

        students = int(input("Number of students: "))

        for i in range(students):

            print(f"\nStudent {i + 1}")

            roll_no = input("Roll number: ")
            name = input("Name: ")

            marks1 = int(input("Marks 1: "))
            marks2 = int(input("Marks 2: "))
            marks3 = int(input("Marks 3: "))

            stdInfo = StudentInfo(roll_no, name)

            stdMarks = StudentMarks(
                roll_no,
                marks1,
                marks2,
                marks3
            )

            average, grade = Main.getGrade(
                stdMarks.student_marks_one,
                stdMarks.student_marks_two,
                stdMarks.student_marks_three
            )

            print(f"\nRoll Number: {stdInfo.student_rollno}")
            print(f"Name: {stdInfo.student_name}")
            print(f"Average: {average}")
            print(f"Grade: {grade}")


Main()
