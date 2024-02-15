from bank_account import *

kishore = BankAccount(10000,"Kishore")
durai = BankAccount(20000,"Durai")

kishore.getBalance()

durai.getBalance()

durai.deposit(500)

kishore.withdraw(100000)
kishore.withdraw(10)

kishore.transfer(100,durai)
