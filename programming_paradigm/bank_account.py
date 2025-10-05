import sys


class BankAccount:

    # command = float(input("\n1. Deposit \n 2. Withdraw \n 3. Display balance"))

    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        # account.deposit(amount)
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive. ")

    def withdraw(self, amount):
        # account.withdraw()
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):

        # account.display_balance()
        print(f"Current Balance: ${self.__account_balance: .2f}")
