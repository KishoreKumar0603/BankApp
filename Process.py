from bank_account import *
import os
from time import sleep as sl



accounts = dict()
def clr():
        os.system('cls')
        
def creating_acc():
        print("<<<< Creating account >>>>")
        print("\n")
        print("Fill the details\n")
        accName = input("Name : ")
        PhoneNo = int(input("Phone No : ")) 
        initialAmount = int(input("Initial Deposit: "))
        print("Account Processing")
        sl(3)
        accounts[accName] = BankAccount(initialAmount,accName)
        accounts[accName].getBalance()
        return accounts

def deposit_():
        accName = input("Account Holder Name : ")
        amount = int(input("Amount : "))
        accounts[accName].deposit(amount)

def transfer_():
        accName = input("Account Holder Name : ")
        account = input("To acc : ")
        amount = int(input("Amount : "))
        accounts[accName].transfer(amount,accounts[account])