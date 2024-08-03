import colorama
from colorama import Back,Style,Fore

class BalanceException(Exception):
    pass
class InvalidPhoneException(Exception):
    pass
class AccountNotFoundException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName, PhoneNo):
        self.balance = initialAmount
        self.name = accName
        self.PhoneNo = PhoneNo
        print(Fore.LIGHTMAGENTA_EX +f"\nAccount '{self.name}' created.\nBalance = Rs.{self.balance:.2f}")
        
        
    def getBalance(self):
        print(Fore.LIGHTMAGENTA_EX + f"Account '{self.name}' balance = Rs.{self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(Fore.LIGHTGREEN_EX + f"\nDeposit Complete.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(Fore.LIGHTRED_EX + f"\nSorry, account '{self.name}' only has a balance of Rs.{self.balance:.2f}")
    def withdrawl(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount 
            print(Fore.GREEN + "\nWithdrawl complete.")
            self.getBalance()
        except BalanceException as error:
            print(Fore.LIGHTRED_EX + f"\nWithdrawl interrupted: {error}")
    
    def transfer(self, amount, account):
        try:
            print(Fore.LIGHTCYAN_EX + "\n**********\n\nBeginning Transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(Fore.LIGHTGREEN_EX + '\nTransfer complete! ✅\n\n***********')
        except BalanceException as error:
            print(Fore.LIGHTRED_EX + f'\nTransfer interrupted. ❌ {error}')