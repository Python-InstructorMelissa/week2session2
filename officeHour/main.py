"""
to pass grade average over 75
failing is under 75 average
get average of students grades
"""


class Teacher:
    def __init__(self, firstName, lastName, className):
        self.firstName = firstName
        self.lastName = lastName
        self.className = className
        self.students = []
        self.passingStudents = []
        self.failingStudents = []

    def printInfo(self):
        print(f"{self.firstName}, teaches {self.className}")
        return self

    def addStudents(self, student):
        self.students.append(student)
        # print("student list: ", self.students)
        return self
    
    def printClass(self):
        myClass = []
        for s in self.students:
            myClass.append([s.studentFirst, s.studentLast])
        print(f"{self.firstName}'s {self.className} class, has the following students: \n {myClass}")
        return self

    def checkPassing(self, grade, student):
        grade = student.finalGrade
        s = student.studentFirst
        if grade > 75:
            self.passingStudents.append(s)
            print(f"{s} passed the class")
        else:
            self.failingStudents.append(s)
            print(f"{s} did not pass")
        return self

    def printFinal(self):
        print(f"The following students Failed {self.firstName}'s {self.className} class: \n{self.failingStudents} \n\n\nThe following students Pass {self.firstName}'s {self.className} class: \n{self.passingStudents}")
        return self

class Student:
    def __init__(self, studentFirst, studentLast):
        self.studentFirst = studentFirst
        self.studentLast = studentLast
        self.grades = []
        self.finalGrade = None

    def printStudentInfo(self):
        print(f"{self.studentFirst} {self.studentLast}")
        return self
    
    def addGrades(self, grade):
        self.grades.append(grade)
        return self

    def gradeAve(self):
        sum = 0
        length = len(self.grades)
        for g in self.grades:
            sum += g
        avg = sum / length
        print(f" {self.studentFirst} has a final average of {avg}")
        self.finalGrade = avg
        return self


melissa = Teacher("Melissa", "Longenberger", "Python")
mel = Teacher("Mel", "Brooks", "Teachers Assistant")
eion = Student("Eion", "PenGryphon")
sabrina = Student("Sabrina", "Henrice")
jane = Student("Jane", "Doe")
john = Student("John", "Smith")
bob = Teacher("Bob", "Ross", "Happy Little Trees")

melissa.printInfo()
mel.printInfo()
bob.printInfo()
eion.printStudentInfo()
sabrina.printStudentInfo()
jane.printStudentInfo()
john.printStudentInfo()

melissa.addStudents(eion).addStudents(sabrina).printClass()
mel.addStudents(jane).addStudents(sabrina).printClass()
bob.addStudents(jane).addStudents(john).printClass()


eion.addGrades(90).addGrades(80).addGrades(85).addGrades(75).addGrades(50)
sabrina.addGrades(80).addGrades(90).addGrades(85).addGrades(75).addGrades(95)
jane.addGrades(95).addGrades(50).addGrades(85).addGrades(75).addGrades(45)
john.addGrades(45).addGrades(90).addGrades(85).addGrades(75).addGrades(95)
eionGrade = eion.gradeAve()
sabrinaGrade = sabrina.gradeAve()
janeGrade = jane.gradeAve()
johnGrade = john.gradeAve()

melissa.checkPassing(eionGrade, eion).checkPassing(sabrinaGrade, sabrina).printFinal()
mel.checkPassing(janeGrade, jane).checkPassing(sabrinaGrade, sabrina).printFinal()
bob.checkPassing(janeGrade, jane).checkPassing(johnGrade, john).printFinal()