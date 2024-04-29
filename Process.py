from bank_account import *
import os
from time import sleep as sl
from oop_project import *




class Processing:
    def clr():
        os.system('cls')

    def creating_acc():
            print("<<<< Creating account >>>>")
            print("\n\n")
            print("Fill the details\n")
            accName = input("Name : ")
            PhoneNo = int(input("Phone No : ")) 
            initialAmount = int(input("Initial Deposit: "))
            clr()
            print("Account Processing")
            sl(3)
            clr()
            accounts[accName] = BankAccount(initialAmount,accName)
            accounts[accName].getBalance()