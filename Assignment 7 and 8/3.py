# 3. Write a Python program to create a class representing a bank. Include methods for managing
# customer accounts and transactions.
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance is {self.balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def get_balance(self):
        return f"Current balance is {self.balance}."

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number in self.accounts:
            return "Account already exists."
        else:
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            return "Account created successfully."

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)
        else:
            return "Account not found."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        else:
            return "Account not found."

    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        else:
            return "Account not found."

    def __str__(self):
        return "\n".join(str(account) for account in self.accounts.values())


# Example usage
bank = Bank()
print(bank.create_account("123456", "John Doe"))
print(bank.deposit("123456", 500))
print(bank.withdraw("123456", 200))
print(bank.get_balance("123456"))
print(bank)