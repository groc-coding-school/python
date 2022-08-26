def menu():
    print("WELCOME TO SDC SYSTEM BY CHRIS. \n")
    print("MENU")
    print("1. ENTER RECORDS")
    print("2. DISPLAY RECORDS")
    print("3. DELETE RECORD")
    x=int(input(" "))
    if x==1:
        capture()
    elif x==2:
        display()
    elif x==3:
        delete()
    else:
        print("Wrong number, retry again. ")

def capture():
    print("Enter the student(s) records \n")
    name=input("NAME: ")
    age=int(input("AGE: "))
    course=input("COURSE: ")
    semester=input("SEMESTER: ")
    stdno=int(input("STUDENT NUMBER: "))
    university=input("UNIVERSITY: ")
    acyear=int(input("ACADEMIC YEAR: "))
    print("Thanks, the records were capture successfully.")
    menu()

def display():
    print("Student(s) Records  From The System\n")
    print("NAME: ",name)
    print("AGE: ",age)
    print("COURSE: ",course)
    print("SEMESTER: ",semester)
    print("STUDENT NUMBER: ",stdno)
    print("UNIVERSITY: ",university)
    print("ACADEMIC YEAR: ",acyear)
    print("\n")
    menu()

def delete():
    print("Enter the number to delete.")

menu()
