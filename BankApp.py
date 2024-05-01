from time import sleep as sl
from bank_account import *
import Process




accounts = dict()
choice = 0



while choice ==0:
    Process.clr()
    print("*************** Welcome ***************")
    print("""1.Create Account\n2.Balance Enquiry\n3.Withdraw\n4.Deposit\n5.Transfer""")
    option = int(input("Enter Option: "))
    
    
    match option:
        case 1:
            Process.clr()
            accounts = Process.creating_acc()
            print(accounts)
            
        case 2:
            Process.clr()
            accName = input("Account Holder Name : ")
            accounts[accName].getBalance()
        case 3:
            Process.clr()
            accName = input("Account Holder Name : ")
            amount = int(input("Amount : "))
            accounts[accName].withdraw(amount)
        case 4:
            Process.clr()
            Process.deposit_()
        case 5:
            Process.clr()
            Process.transfer_()
        case _:
            print("Invalid option")
            
            
            
            
    print("\n")
    choice = int(input("if you want to continue click 0 else any int>>>"))
        