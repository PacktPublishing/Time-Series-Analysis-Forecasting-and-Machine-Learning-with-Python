from student import Student
#import student

name=input("Enter your name: ")
roll=int(input("Enter your roll no: "))
gender=input("Enter your gender: ")
marks=float(input('Enter your marks: '))

print(Student.count)

s1=Student(name,roll,gender,marks)
print(Student.count)

s2=Student("abc",2,"M",85.5)
print(Student.count)

print("Grade of {0} is {1}".format(s1.name,s1.calculateGrade()))

print("Grade of {0} is {1}".format(s2.name,s2.calculateGrade()))
