import random
import string

total = string.ascii_letters
total1 = string.digits 
total2 = string.punctuation

def Simple_pass():
    
    length = 16
    password = "".join(random.sample((total+total1+total2),length))
    print("Your Password is : ",password)

def Aadhar_format():
   length = 4
   pass1 = "".join(random.sample(total,length))
   pass2 = "".join(random.sample(total1,length))
   print("Your Password is : ",pass1+pass2)

def Social_account():

    len1 =5
    len2 =1
    len3 = 4
    pass1 = "".join(random.sample(total,len1))
    pass2 = "".join(random.sample(total2,len2))
    pass3 = "".join(random.sample(total1,len3))
    print("Your Password is : ",pass1+pass2+pass3)

def Design_your_own():
    
        a = int(input("Enter the length of password : "))
        b = int(input("Enter the number of letters : "))
        c = int(input("Enter the number of special Characters : "))
        d = int(input("Enter the number of Numbers : "))
        
        if(a!=(b+c+d)):
           print("Your total length of elements is matching with the remaining elements")
        else:
            pass1 = "".join(random.sample(total,b))
            pass2 = "".join(random.sample(total2,c))
            pass3 = "".join(random.sample(total1,d))
            x = int(input("Choose the desired format:\n1.(ABCXX@**123..)\n2.(ABCXX123...@**)\n3.(123...@**ABCXX)"))
            if(x==1):
                print("Your Password is : ",pass1+pass2+pass3)
            elif(x==2):
                print("Your Password is : ",pass1+pass3+pass2)
            elif(x==3):
                print("Your Password is : ",pass3+pass2+pass1)
            else:
                print("Invalid choice!!! no desired format available....")

while True:
    choice = int(input("Enter your choice to generate ha password :\n1.Simple password\n2.Aadhar fromat\n3.Social Media Account format\n4.Customize Your Own\n5.Exit\nEnter : "))
    if(choice==1):
        Simple_pass()
    elif(choice==2):
        Aadhar_format()
    elif(choice==3):
        Social_account()
    elif(choice==4):
        Design_your_own()
    elif(choice==5):
        break
    else:
        print("Invalid Choice!!!!!")
        
        
        
        
                
                
                
        

    
    
    
   
