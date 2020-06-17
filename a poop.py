
#I know ryt now u would be like what is all this. Don't worry
Cosmic=dict()               #Creates an empty dictionary
i=1                              #Empty variable for loop
flag=0
n=int(input("Enter number of entries"))
while(i<=n):             
    username=input("Enter a Username")                #username
    dob=(input("Enter your DOB"))                    #dob
    pswrds=input("Enter your Password ")             #password
    b=(username,dob,pswrds)        #assigning to a variable
    Cosmic[username]=b
    i=i+1
ls=Cosmic.keys()
for i in ls:
    print("\n username-",username)
    z=Cosmic[i]
    print("username\t","dob\t","pswrds\t")   
for j in z:
    print(j,end="\t")
#########################################################################################

import mysql.connector
from mysql.connector import Error
try:
    conn=mysql.connector.connect(host="localhost",user="root",passwd="root",charset='utf8',database="school")
    mycursor=conn.cursor()
    log=("insert into cosmic (name,password,dob)  values(%s,%s,%s)")
    val=(username,dob,pswrds)
    mycursor.execute(log,val)
    conn.commit()
    print("Done")
except Exception as e:
    print(e)
