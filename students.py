def _menu_():
    print("WELCOME TO SDC SYSTEM BY CHRIS. \n")
    print("MENU")
    print("1. ENTER RECORDS")
    print("2. DISPLAY RECORDS")
    print("3. DELETE RECORD")
    x=int(input(" "))
    if x==1:
        _capture_()
    elif x==2:
        _display_()
    elif x==3:
        _delete_()
    else:
        print("Wrong number, retry again. ")

def _capture_():
    print("Enter the student(s) records \n")
    name=input("NAME: ")
    age=int(input("AGE: "))
    course=input("COURSE: ")
    semester=input("SEMESTER: ")
    stdno=int(input("STUDENT NUMBER: "))
    university=input("UNIVERSITY: ")
    acyear=int(input("ACADEMIC YEAR: "))
    print("Thanks, the records were capture successfully.")

def _display_():
    print("Student(s) Records  From The System\n")
    print("NAME: ",name)
    print("AGE: ",age)
    print("COURSE: ",course)
    print("SEMESTER: ",semester)
    print("STUDENT NUMBER: ",stdno)
    print("UNIVERSITY: ",university)
    print("ACADEMIC YEAR: ",acyear)
    print("\n")
_menu_()

def _delete_():
    print("Enter the number to delete.")
    
_menu_()
