from bank_account import BankAccount

# CheckingAccount is made like a normal bank account but every time u take money out,
# the bank also charges u a fee
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, transaction_fee=1):
        #call the parent class (BankAccount) in order to set up the basics
        super().__init__(account_holder, balance)
         #A fee on every withdrawal
        self.transaction_fee = transaction_fee

    #Replace the normal withdraw from BankAccount
    def withdraw(self, amount):
        #Total= is what you want to take out + the fee
        total = amount + self.transaction_fee
         #Only possible if the account has enough money for both
        if total <= self.balance:
            self.balance -= total
        else:
            print("Insufficient funds")
