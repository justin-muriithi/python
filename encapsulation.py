#encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance #private attributte
        self._name = name #protected atribute
        self.accNo = accNo #piblic view

    def deposit (self, amount):
        self.__balance += amount
        return f"New Balance: {self.__balance}"

    def get_balance(self):
        return self.__balance

account = BankAccount(1000, "John", 1234)
print(account.get_balance())
#print(account.__balance)
#print(account._name)
print(account.accNo)
