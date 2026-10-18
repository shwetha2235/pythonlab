"""Program 13: Encapsulated Banking System with Inheritance Models
This micro-application models a real-world financial engine using OOP principles, featuring a base
BankAccount class and specialized derived classes (SavingsAccount, CurrentAccount). It encapsulates
lab_program_list.md 2026-08-04
private attributes, implements method overriding for balance transactions via super(), and manages
polymorphism using polymorphic interfaces."""


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 0:
            super().withdraw(amount)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        print("Current Account Withdrawal")
        super().withdraw(amount)


savings = SavingsAccount("Ravi", 5000)
current = CurrentAccount("Raju", 3000)

for account in [savings, current]:
    account.deposit(1000)
    account.withdraw(2000)
    print(account.name, "Balance:", account.get_balance())
