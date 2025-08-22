#import os
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



mydb = mysql.connector.connect(
    host ="localhost",
    user = "Harsh Vashishtha",
    password = "Harsh@1234",
    database = "DataDoc"
)

mycursor = mydb.cursor()

sql = "INSERT into students(name,Physics, Chemistry, Maths) VALUES(%s,%s,%s,%s)"



Name = []
Physics= []
Chemistry =[]
Maths = []

while True :
    choice = int(input("Choose the following options:\n1.Data Entry\n2.View Data\n3. View Graphs\n4. Exit\nEnter : "))
    if (choice == 1):
        x = input("Enter your name : ")
        P = int(input("Enter the marks of Physics : "))
        C = int(input("Enter the marks of Chemistry : "))
        M = int(input("Enter the marks of Maths : "))


        Name.append(x)
        Physics.append(P)
        Chemistry.append(C)
        Maths.append(M)
        
        newName = Name[:10]
        newPhysics = Physics[:10]
        newChemistry = Chemistry[:10]
        newMaths = Maths[:10]

        val= (x,P,C,M)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "Record Inserted Successfully..")

        with open("Data.txt", "a") as saved:
            print("Name -> ", newName[:10], file=saved)
            print("Physics Marks -> ",newPhysics[:10], file=saved)
            print("Chemistry Marks ->",newChemistry[:10], file=saved)
            print("Maths Marks ->", newMaths[:10], file = saved)

        print("Data is stored successfully..... in file...")
           

    elif(choice == 2):
        mycursor.execute("SELECT * FROM students")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        

    elif(choice ==4):
        break

    elif(choice ==3):
         mycursor.execute("SELECT name, Physics, Chemistry, Maths FROM students")
         mydata = mycursor.fetchall()
       # print("invalid choice !!! please choose again")
         df = pd.DataFrame(mydata, columns=['name', 'Physics', 'Chemistry', 'Maths'])
       
       
         xpt = df['name']
         ypt = df['Physics']

         x1pt = df['name']
         y1pt = df['Chemistry']

         x2pt = df['name']
         y2pt = df['Maths']

         choose = int(input("Which subject of marks you want to displayyy as graphh...?\n1.Physics\n2.Chemistry\n3.Maths\nEnter : "))
         if(choose==1):
             plt.bar(xpt,ypt,color = "red", width= 0.4)
             plt.title("Student vs Phsics Marks")
             plt.show()

         elif(choose == 2):
             plt.bar(x1pt,y1pt,color = "green", width= 0.4)
             plt.title("Student vs Chemistry Marks")
             plt.show()

         elif(choose == 3):
             plt.bar(x2pt,y2pt,color = "blue", width= 0.4)
             plt.title("Student vs Maths Marks")
             plt.show()
         else:
             print("Invalid option!!!")
        




