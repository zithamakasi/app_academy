balance = 7000
request = float(input("How much do you want to withdraw?: R"))


if request <= 0:
    print("Invalid amount. You must withdraw more than R0.")  
    
elif request <= balance:
    min = balance - request
    print(f"Withdrawal successful! Remaining balance: R{min}")      
    
else:
    print("Declined insufficient funds.")    