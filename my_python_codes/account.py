# This my bank account creation

#First set initial balance
#Set the options
   #option 1. Check balance
   #option 2. Deposit money
   #option 3. Withdraw money
   #option 4. Exit


#current balance
balance = 0
loan_limit = 3000
pin = 2005
while True:

    print("Select an option")
    print("1. Check balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Send Money")
    print("5. Loan")
    print("6. Exit")

    option = input("Enter your option: ")

    if option == "1":
        pin = int(input("Enter your pin: "))
        
        if pin != 2005:
           print("You have entered the wrong pin. Please Try again!")
        else:
           print(f"Your current balance is {balance}")
           
    elif option == "2":
        deposit_amount = int(input("Enter amount you want to deposit: "))
        pin = int(input("Enter your pin: "))
        
        if pin != 2005:
           print("You have entered the wrong pin. Please Try again!")
        elif deposit_amount <= 0:
            print("Can't deposit a negative amount")
        else:
         balance += deposit_amount
         print(f"You have deposited {deposit_amount}. New balance is {balance}")

    elif option == "3":
        withdraw_amount = int(input("Enter amount you want to withdraw: "))
        pin = int(input("Enter your pin: "))
        
        if pin != 2005:
           print("You have entered the wrong pin. Please Try again!")
        elif withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"You have successfully withdrawn {withdraw_amount}. New balance {balance}")
        else:
            print("You have Insufficient funds! ")

    elif option == "4":
        phone_number = (input("Enter phone number: "))

        send_money = int(input("Enter amount to send: "))

        pin = int(input("Enter your pin: "))
        
        if len (phone_number) != 10:
            print("Wrong number. Please Enter the correct number!")
        
        elif balance < send_money :
            print("Insufficient funds to complete transaction: ")
        
        elif pin != 1947:
           print("You have entered the wrong pin. Please Try again!")

        else:
            balance -= send_money
            print(f"You have sent {send_money} to {phone_number}. New balance is {balance}")

            
         
    elif option =="5":
        while True:
         
    
            print("Select an option")
            print("1. Check loan limit")   
            print("2. Borrow loan")   
            print("3. Repay loan")  
            print("4. Check debt")
            print("5. Exit") 

            option = input("Enter your option: ")

            if option == "1":
                print(f"Your loan limit is {loan_limit}: ")
            
            elif option == "2":
                Borrowed_amount =int (input("Enter the amount you want to borrow: "))

                if loan_limit < 0:
                    print("You have exceeded your borrowing limit")

                elif Borrowed_amount > loan_limit:
                    print("That amount is above your loan limit")

                elif Borrowed_amount <= 3000:
                 balance += Borrowed_amount
                 loan_limit -= Borrowed_amount
                 print(f"You have successfully received a loan of {Borrowed_amount}")

                else:
                 print("You can't receive a loan. Please contact the Customer Care")

            elif option == "3":
                Repaid_amount = int(input("Enter amount you want to repay: "))

                if loan_limit == 3000:
                    print("You have no debt to clear")
                    
                elif balance == 0 or Repaid_amount > balance:
                    print("You have insufficient funds in your account")

                elif Repaid_amount > Borrowed_amount:
                    print("You cant more than you borrowed")
                
                elif balance != 0:
                 balance -= Repaid_amount
                 loan_limit += Repaid_amount

                 if loan_limit  != 3000:
                  print(f"You have repaid {Repaid_amount}. Your loan balance is {Borrowed_amount - Repaid_amount}. Your Account balance is {balance}")

                 else:
                    print ("You have successfully cleared your debt!")
            
                else:
                    print("Try again later!!")

            elif option == "4":

                if loan_limit == 3000:
                 print("You have no debt!")

                else:
                 print(f"Your debt is {Borrowed_amount}")



            elif option == "5":
                print("Thank you and welcome again")
                break
            else:
                print("Invalid Input")
            


    elif option == "6":
        print("Thank you")
        break

    else:
        print("Invalid Input")