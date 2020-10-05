from Program import *
import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="root",charset='utf8',database="school")
mycursor=conn.cursor()

def whoami(choice):
    if choice==1:
        print("\n[+] Hello master\n")
    if choice==2:
        print("Good luck with the slaves")
    if choice==3:
        print("Ah ma man whattup yo?")

def login():
    '''so create a table account
    then use this
    '''

    username = input("Enter your Username:-")
    password = input("Enter your password:-")
    mycursor.execute(f"select username from accounts where username = '{username}'")  # this is for checking if the username exists in the table
    mycursor.fetchall()
    if mycursor.rowcount > 0:
        mycursor.execute(f"select password from accounts where username = '{username}'")  # this gets the the pwd from the table for that username
        table_password = mycursor.fetchall()
        conn.commit()
        print(table_password[0][0])
        if password == table_password[0][0]:
            return username # lead this somewhere
        else:
            return False
    else:
        return False



            # Admin
def admin_AddUser():
    print('-------------------')
    username= input("Enter username: ")
    a=input("enter the type of user: ")
    print("1.Admin")
    print("2.Teacher")
    print("3.parent")
    if a == 1:
        type = "admin"
    if a == 2:
        type = "teacher"
    if a == 3:
        type = "student"
    dob= input("Enter date of birth (yyyy/mm/dd): ")
    pass1= input("Enter password: ")
    pass2 = input("Confirm your password: ")
    if pass1 != pass2:
        while pass1 != pass2:
            print('\nPasswords does not match')
            pass1= input("Enter password: ")
            pass2 = input("Confirm your password: ")
    try:
        log = ("insert into accounts (username,type,dob,password)  values(%s,%s,%s,%s)")
        val=(username,type,dob, pass2)
        mycursor.execute(log,val)
        conn.commit()
        print("\n The process has been over")
    except Exception as e:
        print(e)
    else:
        print('------Done!-------\n')


def Admin_RemoveSelf(username):
    print('-----------------')
    d=input("Do you want to continue(y/n): ")
    if d=='n':
        admin(username)
    if d=='y':        
        a=('delete from accounts where username="{}"'.format(username))
        mycursor.execute(a)
        conn.commit()
        login()
    print('-----------------')

def admin_AddAdmin():
    print('-----------------')
    username= input("Enter username: ")
    dob= input("Enter date of birth (yyyy/mm/dd): ")
    pass1= input("Enter password: ")
    pass2 = input("Confirm your password: ")
    if pass1 != pass2:
        while pass1 != pass2:
            print('\nPasswords does not match')
            pass1= input("Enter password: ")
            pass2 = input("Confirm your password: ")
    try:
        log = ("insert into accounts (username,type,dob,password)  values(%s,%s,%s,%s)")
        val=(username,"Admin",dob, pass2)
        mycursor.execute(log,val)
        conn.commit()
        print("\n The process has been over")
    except Exception as e:
        print(e)
    else:
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

