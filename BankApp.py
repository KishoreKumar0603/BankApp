from time import sleep as sl
from bank_account import *
import Process

import colorama
from colorama import Fore,Back,Style
from colorama import init


accounts = dict()
choice = 0



while choice ==0:
    Process.clr()
    print( Back.WHITE + Fore.BLACK + Style.BRIGHT +"*************** Welcome ***************")
    print('\n')
    print(Back.RESET + Fore.WHITE +"""1.Create Account\n2.Balance Enquiry\n3.Withdraw\n4.Deposit\n5.Transfer""")
    option = int(input("Enter Option: " + Fore.BLUE))
    
    
    match option:
        
        #Account Opening
        case 1:
            Process.clr()
            accounts = Process.creating_acc()
            print(accounts)
            
            
        #Balance Enquiry
        case 2:
            Process.clr()
            print(Fore.BLACK + Back.WHITE + Style.BRIGHT +"<<<< Balance Enquiry >>>>")
            print(Back.RESET+"\n")
            accName = input(Fore.WHITE + "Account Holder Name : "+ Fore.BLUE)
            Process.AccountVerify(accName)
            Process.clr()
            Process.sl(3)
            accounts[accName].getBalance()
        
        
        #Withdrawl
        case 3:
            Process.clr()
            print(Fore.BLACK + Back.WHITE + Style.BRIGHT +"<<<< Withdrawl >>>>")
            print(Back.RESET+"\n")
            accName = input(Fore.WHITE + "Account Holder Name : "+ Fore.BLUE)
            Process.AccountVerify(accName)
            amount = int(input(Fore.WHITE + "Amount : "+ Fore.BLUE))
            Process.clr()
            Process.sl(3)
            accounts[accName].withdrawl(amount)
        case 4:
            Process.clr()
            Process.deposit_()
        case 5:
            Process.clr()
            Process.transfer_()
        case _:
            print(Fore.WHITE + "Invalid option")
            
            
            
            
    print("\n")
    choice = int(input(Fore.WHITE + "if you want to continue click 0 else any int>>> "+ Fore.BLUE))
        