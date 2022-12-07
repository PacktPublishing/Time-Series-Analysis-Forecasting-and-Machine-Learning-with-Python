class Student:
    count=0
    def __init__(self,name,gender,roll=-1,marks=0):
        self.name=name
        self.roll=roll
        self.gender=gender
        self.marks=marks
        Student.count+=1

    def __del__(self):
        Student.count-=1

    def calculateGrade(self):
        if self.marks>=70 and self.marks<=100:
            return 'A'
        elif self.marks>=60 and self.marks<70:
            return 'B'
        elif self.marks>=40 and self.marks<60:
            return 'C'
        elif self.marks>=0 and self.marks<40:
            return 'F'
        else:
            return "Invalid marks"

    def getCount(self):
        return Student.count
