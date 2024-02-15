class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance = Rs.{self.balance:.2f}")
        
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = Rs.{self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit Complete.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of Rs.{self.balance:.2f}")
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount 
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
    
    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! ✅\n\n***********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌ {error}')