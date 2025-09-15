from bank_account import BankAccount

#SavingsAccount is a normal account but it accumulates interest over time
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        #Call the parent class (BankAccount) to set up the basics
        super().__init__(account_holder, balance)
        #For savings accounts: the interest rate
        self.interest_rate = interest_rate

     # Adds interest to the balance
    def apply_interest(self):
        # balance increases by: multiplying it with (1 + interest_rate)
        self.balance *= (1 + self.interest_rate)
