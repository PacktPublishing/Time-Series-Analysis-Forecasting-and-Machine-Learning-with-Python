#Write a menu driven program to do the following:
#1. Enter student
#2. Search by roll no
#3. Display Male members
#4. Exit

from student import Student

students={}

def create_new_student():
    name=input("Enter your name: ")
    roll=int(input("Enter your roll: "))
    gender=input("Enter your gender: ")
    marks=float(input("Enter your marks: "))

    s=Student(name,gender,roll,marks)
    students[roll]=s

def search_by_roll_no(roll):
    if roll in students:
        return students[roll]

def get_males():
    return [s[1] for s in student.items() if s[1].gender=="M"]

def display(student_list):
    for s in student_list:
        s.displayDetails()

while True:
    print("1: Enter the student data")
    print("2: Search by roll no")
    print("3: Display males")
    print("4: Exit")

    c=int(input("Choice: "))

    if c==1:
        create_new_student()
    elif c==2:
        search_roll=int(input('Enter the roll no to be searched '))
        s=search_by_roll_no(search_roll)
        s.displayDetails()
    elif c==3:
        males=get_males()
        display(males)
    else:
        break
