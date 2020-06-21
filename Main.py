def whoami(choice):
    if choice==1:
        print("\n[+] Hello master\n")
    if choice==2:
        print("Good luck with the slaves")
    if choice==3:
        print("Ah ma man whattup yo?")

def login():
    username=(input("Enter username: "))
    password=(input("Enter password: "))
    return username

# Admin
def admin_AddUser():
    print('-------------------')
    username= input("Enter username: ")
    dob= input("Enter date of birth (yyyy/mm/dd): ")
    pass1= input("Enter password: ")
    pass2 = input("Confirm your password: ")
    if pass1 != pass2:
        while pass1 != pass2:
            print('\nPasswords does not match')
            pass1= input("Enter password: ")
            pass2 = input("Confirm your password: ")
    print('------Done!-------\n')

def Admin_RemoveSelf():
    print('-----------------')
    print('-----------------')

def admin_AddAdmin():
    print('-----------------')
    print('-----------------')

def admin_RemoveUser():
    print('-----------------')
    print('-----------------')


# Teacher
def teacher_RegisterMarks():
    print('-----------------')
    print('-----------------')

def teacher_ReviewAssignment():
    print('-----------------')
    print('-----------------')

def teacher_ReviewAttendance():
    print('-----------------')
    print('-----------------')

def teacher_AddSuggestion():
    print('-----------------')
    print('-----------------')


# student
def student_ViewMarks():
    print('-----------------')
    print('-----------------')

def student_SubmitAssignment():
    print('-----------------')
    print('-----------------')

def student_ReviewAttendance():
    print('-----------------')
    print('-----------------')

# parent
def parent_Academicperformance():
    print('-----------------')
    print('-----------------')

def parent_Attendance():
    print('-----------------')
    print('-----------------')

def parent_SendSuggestion():
    print('-----------------')
    print('To?')
    choice = int(input('[1] Teacher\n[2] Admin\n[+] '))

    if choice == 1:
        print()
    elif choice == 2:
        print()

    print('-----------------')
