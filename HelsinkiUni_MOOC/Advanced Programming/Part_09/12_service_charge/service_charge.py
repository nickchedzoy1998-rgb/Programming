# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self, owner: str, account_no: str, balance: float):
        self.__owner = owner
        self.__account_no = account_no
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__balance -= self.__service_charge()

    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__balance -= self.__service_charge()

    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        return self.__balance * 0.01


if __name__ == '__main__':
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)