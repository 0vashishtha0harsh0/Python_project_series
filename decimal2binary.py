while True:
    choice = int(input("Choose the option from the following : \n1. Decimal to Binary \n2. Binary To decimal \n3. Exit\nEnter : "))

    if(choice==1):
        Decimal_num = int(input("Enter the decimal number : "))
        Binary_output = ""

        while(Decimal_num>0):
            Remainder = Decimal_num%2
            r = str(Remainder)
            Binary_output = Binary_output + r
            Decimal_num = Decimal_num//2

        Final_result = Binary_output[::-1]
        print(Final_result)

    elif(choice ==2):
        Binary_num = input("Enter the Binary Value :")
        Rev = Binary_num[::-1]
        Decimal_output = 0
        for k in range(0,len(Binary_num)):
            d = Rev[k]
            In = (int(d)) * (pow(2,k))
            Decimal_output = Decimal_output + In
    
        print(Decimal_output)

    elif(choice == 3):
        break

    else:
        print("Invalid Choice !!!! Choose integer number between(1,2 and 3).......")
