from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount
# Making a normal bank account for Bill
b = BankAccount("Bill")
b.deposit(100)
b.withdraw(50)
print(b.account_info())
b.withdraw(100)

#Makin a savings bank account for Bob
s = SavingsAccount("Bob", 200)
print(s.account_info())
s.apply_interest()
print(s.account_info())

#Making a normal bank account for Goerge
c = CheckingAccount("Goerge", 100)
print(c.account_info())
c.withdraw(20)
print(c.account_info())
c.withdraw(90)
