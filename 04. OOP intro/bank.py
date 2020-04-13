import random


class Bank_Account:

    def __init__(self, account_num, currency, balance=0):
        self.__account_num = account_num
        self.__balance = balance
        self.__currency = currency
        self.__transactions = []
        print("Welcome to the deposit & withdrawal machine")

    def add_money(self, amount):
        amount = float(input("Enter amount to be Deposited: "))
        self.__balance += amount
        self.__transactions.append(+amount)
        return amount

    def withdraw_money(self, amount):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(-amount)
            return amount
        else:
            print("\n Insufficient balance  ")

    def recent_transactions(self):
        if len(self.__transactions) < 1:
            return None
        else:
            return self.__transactions.pop()

    def get_account_num(self):
        return self.__account_num

    def get_balance(self):
        return self.__balance

    def get_currency(self):
        return self.__currency


account = Bank_Account(random.randint(100000,999999), "$")
print('account number =', account.get_account_num())
print('account balance =', account.get_balance())

print('account currency =', account.get_currency())
print('deposit =', account.add_money(20), "$")
print('recent transaction is:', account.recent_transactions(), "$")
print('account balance =', account.get_balance(), "$")
print('withdrawal =', account.withdraw_money(50), "$")
print('recent transaction is:', account.recent_transactions(), "$")
print('account balance =', account.get_balance(), "$")
