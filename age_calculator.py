from datetime import datetime
from calendar import isleap


name_input = input("Enter your Name : ")
dob_input = input("Enter your DOB ( YYYY-MM-DD) : ")

dob = datetime.strptime(dob_input, "%Y-%m-%d")

try:
    dob = datetime.strptime(dob_input, "%Y-%m-%d")

except ValueError:
    print("The format of input Date of Birth is wrong ")

today = datetime.today()
if(today.year>dob.year):
    age = today.year - dob.year - ((today.month, today.day)<(dob.month, dob.day))
    day = (today - dob).days
    print(name_input ," is ", age, "years old")
    permit = input("Include end date in calculation(yes or no)")
    if(permit == "yes"):
        day = day +1
        print("Total number of day are :",day)
    else:
        print("Total number of day are :",day)    

else:
    print("people from future are not allowed to calculate age !!")


