# Data Abstraction Example 1

"""
Data abstraction using a BankAccount class as an abstract base class with 
abstract methods for displaying the balance, depositing funds, and withdrawing funds.
Derive a concrete class called SavingsAccount that provides specific implementations of these methods. 
Create an instance of the SavingsAccount class, perform deposit and withdrawal operations, and 
display the account balance before and after the transactions.
"""

from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    @abstractmethod
    def display_balance(self):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def display_balance(self):
        print(f"Account Number: {self.acc_no}")
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

account = SavingsAccount("123456789", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()
