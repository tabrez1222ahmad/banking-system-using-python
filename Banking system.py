
 #I LOVE YOU JANNU BABY INFINTY TIMES338
'''import time
import math
print("Hello I am Python!...")
x = int(input("Enter a num: "))
c = math.log(x)
print(c)
import mysql as sq
class School:
    print("*******************************JNV GANDERBAL****************************************")
    def class6(Class):
        print("Enter your section:")
        c = eval(input())
        name = str(input("Enetr yourn name:"))
        print("Your id: ")
        id = int(input())
        if (id in [600,601,602,603,670]):
            if (id == 600):
                print("Welcome {} Your todays lectures are {}".format(name,lectr))
            else:
                print('go now')
        return Class



    def class7(Class):
        print("Enter your section:")
        c = eval(input())
        name = str(input("Enetr yourn name:"))
        print("Your id: ")
        id = int(input())
        if (id in [700,701,702,703,770]):
            if (id == 770):
                print("Welcome {} Your todays lectures are {}".format(name,lectr))
            else:
                print('go now')
        return Class



    def class8(Class):
        print("Enter your section:")
        c = eval(input())
        name = str(input("Enetr yourn name:"))
        print("Your id: ")
        id = int(input())
        if (id in [800,801,802,803,870]):
            if (id == 801):
                print("Welcome {} Your todays lectures are {}".format(name,lectr))
            else:
                print('go now')
        return Class
    def Iteger():
        pass


Class = eval(input("Enter Your class:"))
lectr = ['English','Urdu','Science','Math','Social Science','Computer Science']
if(Class == 6):
    School.class6(Class)
elif(Class == 7):
    School.class7(Class)
else:
    School.class8(Class)




import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="****",
  password="*****"
)

mycur = mydb.cursor()
#mycur.execute("create database New")
mycur.execute("use New") 
#mycur.execute("create table Sell(Sno int, ID int primary key, Name varchar(50), Adress varchar(100),Pin int)")
mycur.execute("insert into Sell values(7, 925, 'Niyama','Pahalgam', 191211 )")

mydb.commit()

print(mycur.rowcount, "record inserted.")
mycur.execute("select * from Sell")
data = mycur.fetchall()
#for row in data:
    #print(row[],'\n')
for i in range(len(data)):
    print(end='\n')
print(data)
    


import mysql.connector as seq

mydp = seq.connect(
    host = "localhost",
    user = "*****",
    password = "*****"
)
cursor = mydp.cursor()
cursor.execute("create database Hostel")
cursor.execute("use Hostel")
cursor.execute("create table Registry(Sno int, Name varchar(50), Adress varchar(100), AdmissionNo varchar(10) primary key)")
cursor.execute("insert into registry values(1, 'Ilyas Ali Balti', 'Kolan,Ganderbal,J&K', '2021cs099')")
mydp.commit()
print(cursor.rowcount,"record inserted.")





from calendar import c
from secrets import choice
import time
import mysql.connector as con

db = con.connect(
    host = 'localhost',
    user = 'root',
    password = 'Tiger'
)

while True:
    cur = db.cursor()
    option = input("Have you created a database already?(y/n)")
    if option == 'n' or option == 'N':
        cur.execute('create database screw')
        cur.execute('use screw')
        cur.execute("create table held( sno int, Name varchar, class varchar, Uniroll int primary key, Adress varchar, course varchar,Year varchar,hoteller varchar)")
        inputs = int(input("How many enteries are you gonna make?"))
        for i in range(inputs):
            sno = input("Enter the sno: ")
            name = input("Enter the name: ")
            clas = input("Enter the class: ")
            roll = input("Enter rollno: ")
            adress = input("Enter the adress: ")
            course = input("Enter the course: ")
            year = input("Enter the year: ")
            hosteller = input("Whether hosteller or not? ")
            cur.execute('insert into held values({},{},{},{},{},{},{},{}.format(sno,name,clas,roll,adress,course,year,hosteller)')
            db.commit()


    elif option == 'y' or option == 'Y':
        choice2 = (input("Have created a table already?(y/n)"))
        if choice2 == 'n' or choice2 == 'N':
            cur.execute('use screw')
            cur.execute("create table held(sno int, Name varchar(60), class varchar(10), Uniroll int primary key, Adress varchar(50), course varchar(10),Year varchar(10),hoteller varchar(10))")
            inputs = int(input("How many enteries are you gonna make?"))
            for i in range(inputs):
                sno = str(input("Enter the sno: "))
                name = str(input("Enter the name: "))
                clas = str(input("Enter the class: "))
                roll = str(input("Enter rollno: "))
                adress = str(input("Enter the adress: "))
                course = str(input("Enter the course: "))
                year = str(input("Enter the year: "))
                cur.execute('insert into held values({},{},{},{},{},{},{},{}.format(sno,name,clas,roll,adress,course,year,hosteller))')
                db.commit()

        elif choice2 == 'y' or choice2 == 'Y':
            cur.execute('use screw')
            inputs = int(input("How many enteries are you gonna make?"))
            for i in range(inputs):
                sno = str(input("Enter the sno: "))
                name = str(input("Enter the name: "))
                clas = str(input("Enter the class: "))
                roll = str(input("Enter rollno: "))
                adress = str(input("Enter the adress: "))
                course = str(input("Enter the course: "))
                year = str(input("Enter the year: "))
                hosteller = input("Whether hosteller or not? ")
                cur.execute("insert into held values( '1' ,'ilya','csb', '210' ,'kullan','btech','second','yess')")
                db.commit()
    choice3 = input("Do you want to see the data filled? (y/n)")
    if choice3 == 'y' or choice3 == 'Y':
        cur.execute('use screw')
        cur.execute('select * from held')
        data = cur.fetchall()
        for i in range(len(data)):
            print(end='\n')
        print(data)
    else:
        print("all done!")

'''

import time
import mysql.connector as con

mydb = con.connect(
    host = 'localhost',
    user = 'root',
    password = 'Tiger'
)


cur = mydb.cursor()
cur.execute("use myfirstproject")


def signup(Name,userid,pass_word,dob):
    try:
        cur.execute("INSERT INTO users(Name,userid,password,dob) VALUES(%s,%s,%s,%s)",(Name,userid,pass_word,dob))
        mydb.commit()
        print(cur.rowcount, "record inserted.")
        return 
    except con.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if mydb.is_connected():
            #cur.close()
            #mydb.close()
            print("your acount has been created!")

def signin(user,pasword):
    try:
        cur.execute("user myfirstproject")
        data = cur.execute("select * from users WHERE userid = %s and password = %s",(user,pasword))
        cur.fetchone()
        print(data)
        return
    except:
        print("done too")

    finally:
        print("done")

print("Do you have an account or you want to create one")
print("1: if you want to create an account\n2: if you have already created one")
inp = int(input())


if inp == 1:
    print("\nEnter Your Name:\n ")
    name = input()
    print("\nEnter a unique username:\n ")
    userid = input()
    print("\nEnter a strong password:\n ")
    pass_word = input()
    print("\nEnter your dob:\n ")
    dob = input()

    signup(name,userid,pass_word,dob)



elif inp == 2:
    user = input("\nEnter your userid:\n")
    pasword = input("\nEnter your password:\n")
    signin(user,pasword) 
    