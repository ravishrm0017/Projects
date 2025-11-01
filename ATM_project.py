#    ATM 
a = 0
b = 0
person = ['Ravi','Amisha','Shelja']
mobile=[9354594339, 9873270017,8020000052]
current_balance = [10000,20000,300]
user = input("enter Your Name ....") 

print("\n----- Welcome To the ATM -----\n")
for i in person:
    if i==user:
        b = 1
for j in range(len(person)):
    if person[j] == user:
        a = j
if b ==1:
    print(f"{person[a]}\nMobile No: {mobile[a]}") # \nCurrent Balance: {current_balance[a]}")
    print("\n----Select Any One Option----\n")
    print("1. Account Statement")
    print("2. Withdraw Funds")
    print("3. Deposit Funds")
    print("4. Change PIN")
    print("5. Exit\n")

    option1 = int(input("Choose an option (1-5) : ..."))

    if option1==1:
     print("\n----- Account Statement -----\n")
     print(f"Current Balance: {current_balance[a]}\n")
     print("----Select Any One Option----\n")
     print("1. Account Statement")
     print("2. Withdraw Funds")
     print("3. Deposit Funds")
     print("4. Change PIN")
     print("5. Exit\n")

     option2 = int(input("Choose an option (1-5) : ..."))
     if option2 ==1:
        print(f"Current Balance: {current_balance[a]}\n")
     elif option2 == 2:   
        Withdraw_amount = int(input("\nEnter Amount To Withdraw....")) 
        if Withdraw_amount <= current_balance[a]:
         print(f"\n{Withdraw_amount} Withdrawn Successfully !")
         print("\nThank You \n Visit Again")
        else :
         print("Insufficient Balance") 
         print("Thank You! \nVisit Again")
        #  print("----Select Any One Option----\n")
        #  print("1. Account Statement")
        #  print("2. Withdraw Funds")
        #  print("3. Deposit Funds")
        #  print("4. Change PIN")
        #  print("5. Exit\n")
        #  option3 = int(input("Choose an option (1-5) : ..."))
     elif option2==3:   
        print("Deposit Funds Option is not Working rigt now.")   
     elif option2==4:
        print("Change PIN option is not Working Right now")
     else :
        print("Thank You!")  
        print("Visit Again") 
#     elif option1==2:
#      Withdraw_amount = int(input("\nEnter Amount To Withdraw....")) 
#      if Withdraw_amount <= current_balance[a]:
#         print(f"\n{Withdraw_amount} Withdrawn Successfully !")
#      else :
#         print("Insufficient Balance")   
# else:
#     print("You r not our account holder.....")

