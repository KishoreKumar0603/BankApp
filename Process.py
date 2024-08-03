from bank_account import *
import os
from time import sleep as sl

import colorama
from colorama import Fore,Style,Back



accounts = dict()
def clr():
        os.system('cls')
        
def creating_acc():
        print(Fore.BLACK + Back.WHITE + Style.BRIGHT +"<<<< Creating account >>>>")
        print(Back.RESET+"\n"+Fore.WHITE)
        print("Fill the details\n")
        accName = input("Name : " + Fore.BLUE)
        PhoneNo = int(input(Fore.WHITE + "Phone No : "+ Fore.BLUE)) 
        if len(str(PhoneNo))!=10:
                raise InvalidPhoneException(Fore.LIGHTRED_EX + 'Phone Numbe be length of 10!!!')
        initialAmount = int(input(Fore.WHITE + "Initial Deposit: " + Fore.BLUE))
        clr()
        print(Fore.LIGHTGREEN_EX + "Account Processing",end='')
        for i in range(3):
                sl(3)
                print(".",end="")
        print("")
        sl(5)
        clr()
        accounts[accName] = BankAccount(initialAmount,accName,PhoneNo)
        accounts[accName].getBalance()
        return accounts

def deposit_():
        print(Fore.BLACK + Back.WHITE + Style.BRIGHT +"<<<< Deposit >>>>")
        print(Back.RESET+"\n")
        accName = input(Fore.WHITE + "Account Holder Name : "+ Fore.BLUE)
        AccountVerify(accName)
        amount = int(input(Fore.WHITE + "Amount : "+ Fore.BLUE))
        clr()
        sl(3)
        accounts[accName].deposit(amount)

def transfer_():
        print(Fore.BLACK + Back.WHITE + Style.BRIGHT +"<<<< Transfer >>>>")
        print(Back.RESET+"\n")
        accName = input(Fore.WHITE + "Account Holder Name : "+ Fore.BLUE)
        AccountVerify(accName)
        account = input(Fore.WHITE + "To acc : "+ Fore.BLUE)
        AccountVerify(account)
        amount = int(input(Fore.WHITE + "Amount : "+ Fore.BLUE))
        clr()
        sl(3)
        accounts[accName].transfer(amount,accounts[account])
        
def AccountVerify(acc):
        if acc not in accounts:
                raise AccountNotFoundException(Fore.LIGHTRED_EX + "Account Not Found in Our Data !!!" + Fore.RESET)