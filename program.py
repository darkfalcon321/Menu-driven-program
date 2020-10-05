from mysql.connector import Error
from Functions import *

def main():

    print("Please login")
    username = login()
    if username:
        print("Login Successful")
        account(username)
    else:
        print("invalid login")
def account(username):

    account=int(input("who are you? \n[1]Admin \n[2]teacher \n[3]Student \n[4]Parent \n[+]"))
    if account==1:
        admin(username)
    if account==2:
        teacher()
    if account==3:
        student()
    if account==4:
        parent()

# Admin
def admin(username):
    print('\n[!] You are admin')
    quit = False
    while not quit:
        print('What would you like to do?')
        choice = int(input('[1] Remove this account\n[2] Add_admin\n[3] Add_user\n[4] Remove_user\n[5] exit\n[+] '))

        if choice == 1:
            Admin_RemoveSelf(username)
        elif choice == 2:
            admin_AddAdmin()
        elif choice == 3:
            admin_AddUser()
        elif choice == 4:
            admin_RemoveUser()
        elif choice == 5:
            quit = True
        else:
            print('Please enter a valid option')


#Teacher
def teacher():
    quit = False
    while not quit:
        print('\nWhat would you like to do?')
        choice = int(input('[1] Register_Marks\n[2] Review_Assignment\n[3] Review_Attendance\n[4] Add_Suggestion\n[5] exit\n[+]'))

        if choice == 1:
            teacher_RegisterMarks()
        elif choice == 2:
            teacher_ReviewAssignment()
        elif choice == 3:
            teacher_ReviewAttendance()
        elif choice == 4:
            teacher_AddSuggestion()
        elif choice == 5:
            quit = True
        else:
            print('Please enter a valid option')

# Student
def student():
    quit = False
    while not quit:
        print('\nWhat would you like to do?')
        choice = int(input('[1] View_Marks\n[2] Submit_Assignment\n[3] Review_Attendance\n[4] exit\n[+]'))

        if choice == 1:
            student_ViewMarks()
        elif choice == 2:
            student_SubmitAssignment()
        elif choice == 3:
            student_ReviewAttendance()
        elif choice == 4:
            quit = True
        else:
            print('Please enter a valid option')

# Parent
def parent():
    quit = False
    while not quit:
        print('\nWhat would you like to do?')
        choice = int(input('[1] Academic_performance\n[2] Attendance\n[3] Send_Suggestion\n[4] exit\n[+]'))


        if choice == 1:
            parent_Academicperformance()
        elif choice == 2:
            parent_Attendance()
        elif choice == 3:
            parent_SendSuggestion()
        elif choice == 4:
            quit = True
        else:
            print('Please enter a valid option')


        # conn=mysql.connector.connect(host="localhost",user="root",passwd="root",charset='utf8',database="school")
        # try:
        #     mycursor=conn.cursor()
        #     log=("insert into login_page (username,dob,password)  values(%s,%s,%s)")
        #     val=("username","dob","passwords")
        #     mycursor.execute(log,val)
        #     conn.commit()
        #     print("\n The process has been over")
        # except Exception as e:
        #     print(e)

if __name__ == '__main__':
    main()
