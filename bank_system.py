import json
import random

class AccountNotFoundError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, account_number, name, address, email, phone, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def transfer(self, dest_account, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount
        dest_account.balance += amount
        print(f"Transferred {amount} to account {dest_account.account_number}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, name, address, email, phone, initial_deposit):
        account_number = random.randint(10000000000, 99999999999)
        account = Account(account_number, name, address, email, phone, initial_deposit)
        self.accounts.append(account)
        self.save_accounts()
        print(f"Account created successfully! Account Number: {account_number}")

    def find_account(self, account_number, name):
        for account in self.accounts:
            if account.account_number == account_number and account.name == name:
                return account
        raise AccountNotFoundError(f"Account not found or name does not match.")

    def remove_account(self, account_number, name, phone):
        account_to_remove = None
        for account in self.accounts:
            if account.account_number == account_number and account.name == name and account.phone == phone:
                account_to_remove = account
                break
        if account_to_remove:
            self.accounts.remove(account_to_remove)
            self.save_accounts()
            print(f"Account {account_number} removed successfully.")
        else:
            raise AccountNotFoundError(f"Account not found or details do not match.")

    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts to show.")
            return
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}")

    def save_accounts(self):
        data = [
            {
                "account_number": account.account_number,
                "name": account.name,
                "address": account.address,
                "email": account.email,
                "phone": account.phone,
                "balance": account.balance
            }
            for account in self.accounts
        ]
        with open("accounts.json", "w") as f:
            json.dump(data, f)
        print("Accounts saved to file.")

    def load_accounts(self):
        try:
            with open("accounts.json", "r") as f:
                data = json.load(f)
                self.accounts = [Account(**account) for account in data]
            print("Accounts loaded from file.")
        except FileNotFoundError:
            print("No saved accounts found.")


def main():
    bank = Bank("My Bank")
    bank.load_accounts()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Funds")
        print("5. Balance Inquiry")
        print("6. Remove Account")
        print("7. Show All Accounts")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter account holder name: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(name, address, email, phone, initial_deposit)

        elif choice == 2:
            acc_number = int(input("Enter account number: "))
            name = input("Enter account holder name: ")
            try:
                account = bank.find_account(acc_number, name)
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                bank.save_accounts()
            except AccountNotFoundError as e:
                print(e)

        elif choice == 3:
            acc_number = int(input("Enter account number: "))
            name = input("Enter account holder name: ")
            try:
                account = bank.find_account(acc_number, name)
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
                bank.save_accounts()
            except (AccountNotFoundError, InsufficientFundsError) as e:
                print(e)

        elif choice == 4:
            src_acc_number = int(input("Enter your account number: "))
            src_name = input("Enter your account holder name: ")
            dest_acc_number = int(input("Enter destination account number: "))
            dest_name = input("Enter destination account holder name: ")
            try:
                src_account = bank.find_account(src_acc_number, src_name)
                dest_account = bank.find_account(dest_acc_number, dest_name)
                amount = float(input("Enter amount to transfer: "))
                src_account.transfer(dest_account, amount)
                bank.save_accounts()
            except (AccountNotFoundError, InsufficientFundsError) as e:
                print(e)

        elif choice == 5:
            acc_number = int(input("Enter account number: "))
            name = input("Enter account holder name: ")
            try:
                account = bank.find_account(acc_number, name)
                print(f"Current balance: {account.get_balance()}")
            except AccountNotFoundError as e:
                print(e)

        elif choice == 6:
            acc_number = int(input("Enter account number to remove: "))
            name = input("Enter account holder name: ")
            phone = input("Enter phone number: ")
            try:
                bank.remove_account(acc_number, name, phone)
            except AccountNotFoundError as e:
                print(e)

        elif choice == 7:
            bank.show_all_accounts()

        elif choice == 8:
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
