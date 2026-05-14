

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
        # 1) Add an attribute called withdrawal limit of $100
        self.withdraw_limit = 100

    # 2) Override the withdrawal behavior
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Transaction Declined: Cannot withdraw more than ${self.withdraw_limit}.")
        elif amount > self.balance:
            print("Transaction Declined: Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Success! Withdrew: ${amount}. Remaining balance: ${self.balance}")

# --- Example Usage ---
my_savings = SavingsAccount(500)

my_savings.withdraw(50)   # Works: under the limit
my_savings.withdraw(150)  # Fails: exceeds $100 limit