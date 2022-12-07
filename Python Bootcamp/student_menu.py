#Write a menu driven program to do the following:
#1. Enter student
#2. Display total students
#3. Display Males
#4. Display Females
#5. Exit


from student import Student

students=[]

def create_new_student():
    name=input("Enter your name: ")
    roll=int(input("Enter your roll: "))
    gender=input("Enter your gender: ")
    marks=float(input("Enter your marks: "))

    s=Student(name,gender,roll,marks)
    students.append(s)

def get_count():
    return len(students)

def get_males():
    for student in students:
        if student.gender=="M":
            student.displayDetails()


def get_females():
    for student in students:
        if student.gender=="F":
            student.displayDetails()

while True:
    print("1: Enter student details")
    print("2: Display total students")
    print("3: Display males")
    print("4: Display females")
    print("5: Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        create_new_student()
    elif choice==2:
        print("The total number of students currently is",get_count())
    elif choice==3:
        get_males()
    elif choice==4:
        get_females()
    else:
        break
