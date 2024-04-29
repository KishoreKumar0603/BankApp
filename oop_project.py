from time import sleep as sl
from bank_account import *
from Process import *



accounts = dict()
print("*************** Welcome ***************")
print("""1.Create Account\n2.Balance Enquiry\n3.Withdraw\n4.Deposit""")
option = int(input("Enter Option: "))

match option:
    case 1:
        creating_acc()
        
    # case 2:
    #     print()
        
        
    # case 3:
    # case 4:
    # case _:
        print("Invalid option")
        