'''Bank Account Class'''
import random
class BankAccount:
    '''Bank account class'''

    interest_rate = 0.00083

    def __init__(self, full_name: str = '', balance=0.0, acc_type ="Checking"):
        self.full_name = full_name
        self.account_number = random.randint(1000000, 9999999)
        self.balance =  balance
        self.acc_type = acc_type

    def generate_account_number(self):
        '''Generates a random 8-digit'''
        return str(random.randint(10**7, 10**8 -1))
    def deposit(self, amount):
        '''Deposits given amount to bank account'''
        if amount > 0:
            self.balance += amount
            print(f"Amount Deposited: ${amount} New Balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount")


    def withdraw(self, amount):
        '''Withdrawal from account'''
        if amount > self.balance:
            print("Insufficient funds. Applying a $10 overdraft fee.")
            self.balance -= 10
            print(f"New Balance: {self.balance:.2f}")
        elif amount > 0:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount:.2f} New Balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawn amount.")


    def print_balance(self):
        '''Shows account balance'''
        print(f"Account Balance: ${self.balance:.2f}")


    def add_interest(self):
        '''Adds interest to account'''
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        return interest


    def print_statement(self):
        '''Print statement with account name, account number, balance'''
        hidden_number = "****" + str(self.account_number)[-4:]
        print(f'''Account Name: {self.full_name}\nAccount Number: {hidden_number}\nBalance: ${self.balance:.2f}''')


# Testing
mitchell = BankAccount("Mitchell")
mitchell.account_number = "03141592"
print("Mitchell: ")
print("Deposit: ")
mitchell.deposit(400000)
mitchell.print_statement()
print("------------------")
print("interest: ")
mitchell.add_interest()
mitchell.print_statement()
print("------------------")
print("Withdrawn: ")
mitchell.withdraw(150)
mitchell.print_statement()
print("------------------")
print("Withdrawn: ")
mitchell.withdraw(500000)
mitchell.print_statement()
print("--------------------------")

# create 3 different accounts
account = BankAccount("Angela", balance = 1000)
print("Full name:", account.full_name)
print("Account number:", account.account_number)
print("Balance:", account.balance)
print("------------------")
account_1 = BankAccount("Nessa Begay", balance = 400)
account_2 = BankAccount("Meghan Mealer", balance = 10)
account_3 = BankAccount("Necole Begay", balance = 95)

# testing different methods
print("Account number:", account_1.account_number)
print("Account number:", account_2.account_number)
print("Account number:", account_3.account_number)

print("Deposit: ")
account_1.deposit(100000)
account_2.deposit(20000.56)
account_3.deposit(543675723)

account_1.print_statement()
account_2.print_statement()
account_3.print_statement()
print("--------------------------")


print("Withdraw: ")
account_1.withdraw(10.89)
account_2.withdraw(200.89)
account_3.withdraw(5409)

account_1.print_statement()
account_2.print_statement()
account_3.print_statement()
print("--------------------------")


account_1.print_statement()
account_2.print_statement()
account_3.print_statement()
print("--------------------------")


print("Add interest: ")
account_1.add_interest()
account_2.add_interest()
account_3.add_interest()

account_1.print_statement()
account_2.print_statement()
account_3.print_statement()

#plan
# class BankAccount():

    # interest_rate = 0.00083

    # def __init__(self, full_name):
        #self.full_name = full_name
        #self.account_number = randomly generate number 8 digits
        #self.balance = balance

    # def deposit(self, amount):
        #deposits money and adds to balance
        # prints amount deposited and prints new balance

    # def withdraw(self, amount):
        # if amount withdrawn is greater than balance then
        # print message for insufficient funds, adding $10 fee
        #balance -= 10
        # print amount withdrawn and print new balance

    # def get_balance(self)
        # print account balance
        #return account balance

    # def add_interest(self):
        # interest assigned to balance * interest_rate
        # add balance and interest together
        # return balance

    # def print_statement(self):
        # create variable to hide first 4 digits
        # print message with account name, acount number, and balance
