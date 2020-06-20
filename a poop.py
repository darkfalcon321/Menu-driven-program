
print("1.Admin\n2.teacher\n3.student")
choice=int(input("who tf are u?"))
if choice==1:
    print("Hello master")
if choice==2:
    print("good luck with the slaves")
if choice==3:
    print("ah ma man whattup yo?")
print("1,signup \n2,login")
choice=eval(input("choose em"))
if choice==1:
    def signup():
        username= input("Enter username: ")
        dob= input("Enter date of birth: ")
        pass1= input("Enter password: ")
        pass2 = input("Confirm your password: ")
        if pass1 != pass2:
            while pass1 != pass2:
                print('Passwords does not match')
                pass1= input("Enter password: ")
                pass2 = input("Confirm your password: ")
        else:
            print('continue')
if choice==2:
    username=(input("Enter username :"))
    password=(input("Enter password :"))
import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="root",charset='utf8',database="school")
try:
    mycursor=conn.cursor()
    log=("insert into login_page (username,dob,password)  values(%s,%s,%s)")
    val=("username","dob","passwords")
    mycursor.execute(log,val)
    conn.commit()
    print("\n The process has been over")
except Exception as e:
    print(e)
