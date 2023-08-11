# Encapsulation-EXAMPLE-2

"""
Write a Python code example showcasing encapsulation using a BankAccount class 
with private attributes for account number and balance. 
Include methods for depositing, withdrawing, and retrieving account information, and demonstrate their usage
"""
        
class BankAccount:
    def __init__(self, acc_no, initial_balance):
        self.__acc_no = acc_no
        self.__balance = initial_balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")
    
    def get_account_info(self):
        print(f"Account Number: {self.__acc_no}")
        print(f"Balance: {self.__balance}")


account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
account.get_account_info()
