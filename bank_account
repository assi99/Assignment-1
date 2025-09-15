class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    #Defining a deposite function, to recive the amount to deposite
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    #Defining a withdraw function, to recive the amount to withdraw
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    #to display the balance in the account
    def account_info(self):
        return f"{self.account_holder}: Balance = {self.balance}"
