import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    username = "Harsh Vashishtha",
    password = "Harsh@1234",
    database = "myquiz"
    )
mycursor = mydb.cursor()
new = "INSERT INTO record(Student, Email, Score)VALUES(%s,%s,%s)"
a = input("Enter your name : ")
b = input("Enter your Email : ")
score = 0
print("\nWelcome",a)
c = input("Use 's' to start the Quiz ")
if(c == 's'):
    print("\nGood luck",a)
    print("Your Quiz is started succefully")
    print("\n")
    z = input("1. Which state is known as DevBhoomi ?\na.UttarPradesh\nb.Assam\nc.Gujarat\nd.Uttrakhand\nAnswer : ")
    if(z=="d"):
        print("correct answer ")
        score = score + 5
    if((z=="a")or(z=="b")or(z=="c")):
        print("incorrect answer, correct answer is 'Uttrakhand' ")
d = input("Click on 'n' to proceed Next question : ")
if(d == "n"):
    y = input("\n2. Which state has highest population density ?\na.Uttarpradesh\nb.Rajasthan\nc.Bihar\nd.Arunachal pradesh\nAnswer : ")
    if(y=="c"):
        print("Correct answer ")
        score = score + 5
    if((y=="a")or(y=="b")or(y=="d")):
        print("incorrect answer, correct answer is 'Bihar'")
    
d0 = input("Click on 'n' to proceed Next question : ")
if(d0 == "n"):
    x = input("\n3.what is contituional amendment ?\na.Change in constitution\nb.Delete constitution\nc.Update constitution\nd.Rename Constitution\nAnswer : ")
    if(x=="a"):
        print("Correct answer ")
        score = score + 5
    if((x=="d")or(x=="b")or(x=="c")):
        print("incorrect answer, correct answer is 'change in constituition'")
 
d1 = input("click on 'n' to proceed Next question : ")
if(d1 == "n"):
    w = input("\n4.Who is known as the 'missile man of india' ?\na.S Jaishankar\nb.APJ Abdul Kalam\nc.Subash Chandra Bose\nd.Milkha Singh\nAnswer : ")
    if(w == "b"):
        print("correct answer")
        score = score + 5
    if((w=="d")or(w=="a")or(w=="c")):
        print("incorrect answer, correct answer is 'APJ Abdul Kalam' ")
d2 = input("Click on 'n' to proceed Next question : ")
if(d2 == "n"):
    v = input("\n5.Which country has the highest life expectancy ?\na.United states\nb.India\nc.Hong kong\nd.Russia\nAnswer : ")
    if(v == "c"):
        print("correct answer ")
        score = score + 5
    if((v=="d")or(v=="a")or(v=="b")):
        print("incorrect answer, correct answer is 'Hong Kong'")

d3= input("Click on 'n' to proceed Next question : ")
if(d3 == "n"):
    u = input("\n6.How many minute are in full week ?\na.10890\nb.10080\nc.9680\nd.10880\nAnswer : ")
    if(u == "b"):
        print("correct answer")
        score = score + 5
    if((u=="d")or(u=="a")or(u=="c")):
        print("incorrect answer, correct answer is '10080'")

d4 = input("Click on 'n' to proceed to Next question : ")
if(d4 == "n"):
    t = input("\n7.How many bones do we have in ear ?\na.5\nb.2\nc.3\nd.4\nAnswer : ")
    if(t == "c"):
        print("correct answer ")
        score = score + 5
    if((t=="d")or(t=="a")or(t=="b")):
        print("incorrect answer, correct answer is '3'")

d5 = input("Click on 'n' to proceed to Next question : ")
if(d5=="n"):
    s = input("\n8.Which country drink the most coffee per capita ?\na.Rome\nb.China\nc.Italy\nd.Netherland\nAnswer : ")
    if(s == "a"):
        print("correct answer")
        score = score + 5
    if((s=="d")or(s=="b")or(s=="c")):
        print("incorrect answer, correct answer is 'Rome'")

d6 = input("Click on 'n' to proceed to Next question : ")
if(d6=="n"):
    r = input("\n9.Which counrty invented ice-cream ?\na.Moscow\nb.China\nc.India\nd.Iran\nAnswer : ")
    if(r == "b"):
        print("correct answer")
        score = score + 5
    if((r=="d")or(r=="a")or(r=="c")):
        print("incorrect answer, correct answer is 'china'")


d7 = input("Click on 'n' to proceed to Next question : ")
if(d7=="n"):
    q = input("\n10.Which animal has the largest brain relative to body size ?\na.Elephant\nb.Mangoose\nc.Dolphin\nd.Cat\nAnswer : ")
    if(q == "c"):
        print("correct answer")
        score = score + 5
    if((q=="d")or(q=="b")or(q=="a")):
        print("incorrect answer, correct answer is 'Dolphin'")


d8 = input("Click on 'n' to proceed to Next question : ")
if(d8=="n"):
    p = input("\n11.Which animal has the longest tongue ?\na.Elephant\nb.Giraffe\nc.Whale\nd.Cow\nAnswer : ")
    if(p == "b"):
        print("correct answer")
        score = score + 5
    if((p=="d")or(p=="a")or(p=="c")):
        print("incorrect answer, correct answer is 'Giraffe'")

d9 = input("Click on 'n' to proceed to Next question : ")
if(d9=="n"):
    o = input("\n12.How many heart does an octopus have ?\na.1\nb.2\nc.3\nd.4\nAnswer : ")
    if(o == "c"):
        print("correct answer")
        score = score + 5
    if((o=="d")or(o=="b")or(o=="a")):
        print("incorrect answer, correct answer is '3'")



print("\n Quiz is completed Successfully")
print("You score",score," marks out of 60")

val =(a,b,score)
mycursor.execute(new,val)
mydb.commit()
print(mycursor.rowcount,"Your Quiz is submitted",a)
    
    





        
    
