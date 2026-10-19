
r'''
Task 1: Defining a Base Class (BankAccount)

    Create a class BankAccount in a file (e.g., bank.py) that includes:
        Attributes:
            account_number
            owner
            balance
        Initializer:
            __init__(self, account_number, owner, balance=0) that sets the initial values.
        Methods:
            - deposit(self, amount): Adds the given amount to balance. Allow only positive amounts; if a non-positive amount is passed, raise a ValueError with an appropriate message.
            - withdraw(self, amount): Subtracts the given amount from balance if sufficient funds exist. If the withdrawal amount is greater than the current balance, raise a ValueError (or your custom exception, if you choose to implement Task 3) indicating insufficient funds. Otherwise, deduct the amount and return the new balance.
            - __str__(self): Returns a string representation of the account (e.g., "Account 12345 – Owner: Alice, Balance: $500").

    Write test code (either within a main section in bank.py or in a separate test file) to:
        Create an instance of BankAccount.
        Demonstrate a successful deposit and withdrawal.
        Attempt a withdrawal that exceeds the balance to trigger and catch the exception, printing an error message.
'''

r'''  
# Attempt 1 - Failed!
# FAILED METHOD deposit(self, amount)!
class BankAccount:

    # Define initializer / constructor:
    def __init__(self, account_number, owner, balance=0):

        account_number.self = account_number
        owner.self = owner
        balance.self = balance

    # Define methods:
    def deposit(self, amount):
        # if deposit < .01:
        balance = balance + amount
        # print(balance)

    def main():
        try:
            amount = int(input("Enter deposit amount: "))
        except ValueError:
            print("Please enter a depsoit amount greater than $0.00")
    main()
'''

r'''  
# Attempt 2 - Failed!
class BankAccount:

    # Define initializer / constructor:
    def __init__(self, account_number, owner, balance=0):

        account_number.self = account_number # wrong backwards setup!!!
        owner.self = owner # wrong backwards setup!!!
        balance.self = balance # wrong backwards setup!!!

    # Define methods:
    def deposit(self, amount):
        if deposit < .01: # 1a) if a non-positive amount is passed, raise a ValueError
            raise ValueError("Invalid amount. Enter a deposit amount greater than $0.00.") # 1b) if a non-positive amount is passed, raise a ValueError
        else:
            balance = balance + amount
            print(f"Amount deposited: {amount}")
            print((f"New balance: {balance}"))

    # Define Objects:
    # dog1 = Dog(name = 'Max', breed = 'Boxer', color = 'blue')
    # deposit1 = BankAccount(account_number = '103345465', owner = 'Rod', balance = 0)

    def main():
        try:
            amount = float(input("Enter deposit amount: "))
            # deposit(self, amount)
        except ValueError as e:  # 1c) if a non-positive amount is passed, raise a ValueError
            print(e)  # 1d) if a non-positive amount is passed, raise a ValueError

        # deposit(self, amount)
    main()
''' 

r''' 
#[PERFECT!!!! Methods, point 1] - deposit(self, amount): Adds the given amount to balance. Allow only positive amounts; if a 
# non-positive amount is passed, raise a ValueError with an appropriate message.
 
class BankAccount:  # Defining the class
    # Define initializer / constructor:
    def __init__(self, account_number, owner, balance=0):  # Defining initialzer with dunder '__init__' (aka 'dunder init method')
                                                          # to hold parameters:
                                                          # 'self', 'account_number', 'owner', 'balance=0' 
        self.account_number = account_number # an argument conitnues to get passed to 'account_number', which in turn gets
                                            # assigned to 'self.account_number'
        self.owner = owner                  # "                 "                   "              "                "          "
        self.balance = balance               # "                 "                   "              "                "          "

    # Define methods:
    def deposit(self, amount):  # Defining method 'deposit(self, amount)' to hold 2 parameters ('self' and 'amount')
        # if deposit < .01: # 1a) if a non-positive amount is passed, raise a ValueError # replace with below line!
        if amount <= 0:  # 1a) Conditional branch: if a non-positive amount is passed.....
            raise ValueError("Invalid amount. Enter a deposit amount greater than $0.00.") # 1b) ....raise a ValueError with a
                                                                                           # a personalized messaged. This 
                                                                                           # is known as "raising an exception"
        # else: # removed, as not relevant here.
            #balance = balance + amount  #  # removed, as not relevant here.
            #print(f"Amount deposited: {amount}")   # removed, as not relevant here.
            #print((f"New balance: {balance}"))    # removed, as not relevant here.
        # balance = balance + amount # Here the method tracks the account balance after each deposit.
                                    # Remember! 'balance' has been resassigned to 'self.balance', so 'amount' no loger relevant
                                    # for reference/calling/etc purposes any more, so we replaced with line below...
        # self.balance = self.balance + amount # Great!!!
        self.balance += amount # Excellent!!!

        print(f"Amount deposited: {amount}")  # Here the method prints a message staitng the amount deposited.
        print((f"New balance: {self.balance}")) # Here the method tracks and prints a new balance total after each deposit.

    # Define Objects: 
    # Notice!!! that our objects WERE NOT defined next as we did in my 'dog.py' code
    # deposit1 = BankAccount(account_number = '103345465', owner = 'Rod', balance = 0) # removed, as not relevant here.

# Define your main() function:
def main():
    account = BankAccount(12345, "Alice", 500) # 2) Correct way to call the class, while simultaneaously creating the object 'account'
                                               # SO YOU CREATE YOUR OBJECT HERE!! by assigning the entire call to class 'BankAccount()'
                                               # variable 'account', which as of now is to referred as an OBJECT.
    try:            # Creting your 'try'/'except' block....
        amount = float(input("Enter deposit amount: ")) # ...around that part of the code that is expected to trigger exception.
        # deposit(self, amount) # Wrong way to call function! 
        # deposit(amount) # Wrong way to call function! 
        # BankAccount.deposit(amount) # 1) Wrong to call function! why? bc you have not defined/created any objects for 'BankAccount'
        account.deposit(amount) # 3) and so NOW you can correctly call the METHOD 'deposit(amount)' ONTO the OBJECT 'account'
    except ValueError as e:  # 1c) replaces the typical 'ValueError' meesage with the personalized one you raised in '1b)'
                            # whinch you envoked here by 'as e'
        # print(e)  # 1d) prints personalized error raised in '1b)'
        print(f"Error: {e}")  # 1d) prints personalized error raised in '1b)', but more polished!!

    # deposit(self, amount)
main() # immediately calling 'main()'
'''

r'''
# [PERFECT!!!! Methods, point 2 and 3] 
# - withdraw(self, amount): Subtracts the given amount from balance if sufficient funds exist. If the withdrawal amount is greater 
# than the current balance, raise a ValueError (or your custom exception, if you choose to implement Task 3) indicating 
# insufficient funds. Otherwise, deduct the amount and return the new balance.
# - str__(self): Returns a string representation of the account (e.g., "Account 12345 – Owner: Alice, Balance: $500").

class BankAccount:
    # Define initializer / constructor:
    def __init__(self, account_number, owner, balance=0): # Defining initialzer with dunder '__init__' (aka 'dunder init method')
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    # Define methods:
    def deposit(self, amount):
        if amount <= 0:  
            raise ValueError("Invalid amount. Enter a deposit amount greater than $0.00.") 
        self.balance += amount 
        print(f"Amount deposited: {amount}")
        # print((f"New balance: {self.balance}")) # rounds decimal to tenths place
        # print((f"New balance: {self.balance: .2f}"))  # rounds decimal to hundreths place
        print((f"New balance: ${self.balance:.2f}"))  # rounds decimal to hundreths place
        return self.balance

# AFTER Check-order change:
    def withdraw(self, amount):
        # 1)
        if amount <= 0:  # WITHOUT this condition branch guard, It doesn’t reject non-positive amounts and account.withdraw(-100) 
                         # would pass the self.balance < amount check (500 < -100 is false), and then self.balance - (-100) 
                         # would add $100 to the account, rather than deducting.
            raise ValueError("Invalid amount. Enter a withdrawal amount greater than $0.00.") 
        # 2)
        if self.balance < amount:
            raise ValueError("Insufficient funds: cannot withdraw more than the current balance.")  
        self.balance = self.balance - amount 
        print(f"Amount withdrawn: {amount}")
        # print((f"New balance: {self.balance}"))
        print((f"New balance: ${self.balance:.2f}"))  # rounds decimal to hundreths place
        return self.balance
        # Instructions say '(or your custom exception, if you choose to implement Task 3) indicating insufficient funds.'..go over!

    def __str__(self):
        return f"Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance}" #2a) Displays cs dashboard by default.

    # Define Objects:
    # dog1 = Dog(name = 'Max', breed = 'Boxer', color = 'blue')
    # deposit1 = BankAccount(account_number = '103345465', owner = 'Rod', balance = 0)

def main():
    # Creating an instance of BankAccount:
    account = BankAccount(12345, "Alice", 500) # 2c) VIP note!! eventhough you later defined a '__str__' method above, this line
                                                # is still necessary bc this is where the object is being deifned.
                                                # Also, this is NOT the line used to display the customer's dashboard
    print(account) # 2b) Prints the argument value passed to object 'account' by the class 'BankAccount' (see right above!)

    try:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    except ValueError as e: 
        # print(e)  
        print(f"Error: {e}") 

    try:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    except ValueError as e: 
        # print(e)  
        print(f"Error: {e}") 

main()
'''

r''' 
#  [PERFECT!!!! Hadrcoding for test code: ] 
Write test code (either within a main section in bank.py or in a separate test file) to:
    Create an instance of BankAccount.
    Demonstrate a successful deposit and withdrawal.
    Attempt a withdrawal that exceeds the balance to trigger and catch the exception, printing an error message.

class BankAccount:
    # Define initializer / constructor:
    def __init__(self, account_number, owner, balance=0): # Defining initialzer with dunder '__init__' (aka 'dunder init method')
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    # Define methods:
    def deposit(self, amount):
        if amount <= 0:  
            raise ValueError("Invalid amount. Enter a deposit amount greater than $0.00.") 
        self.balance += amount 
        print(f"Amount deposited: ${amount:.2f}")
        # print((f"New balance: {self.balance}")) # rounds decimal to tenths place
        # print((f"New balance: {self.balance: .2f}"))  # rounds decimal to hundreths place
        print((f"New balance: ${self.balance:.2f}"))  # rounds decimal to hundreths place
        return self.balance

# AFTER Check-order change:
    def withdraw(self, amount):
        # 1)
        if amount <= 0:  # WITHOUT this condition branch guard, It doesn’t reject non-positive amounts and account.withdraw(-100) 
                         # would pass the self.balance < amount check (500 < -100 is false), and then self.balance - (-100) 
                         # would add $100 to the account, rather than deducting.
            raise ValueError("Invalid amount. Enter a withdrawal amount greater than $0.00.") 
        # 2)
        if self.balance < amount:
            raise ValueError("Insufficient funds: cannot withdraw more than the current balance.")  
        self.balance = self.balance - amount 
        print(f"Amount withdrawn: ${amount:.2f}")
        # print((f"New balance: {self.balance}"))
        print((f"New balance: ${self.balance:.2f}"))  # rounds decimal to hundreths place
        return self.balance
        # Instructions say '(or your custom exception, if you choose to implement Task 3) indicating insufficient funds.'..go over!

    def __str__(self):
        return f"Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance:.2f}" #2a) Displays cs dashboard by default.

    # Define Objects:
    # dog1 = Dog(name = 'Max', breed = 'Boxer', color = 'blue')
    # deposit1 = BankAccount(account_number = '103345465', owner = 'Rod', balance = 0)

def main():
    # Creating an instance of BankAccount:
    account = BankAccount(12345, "Alice", 500) # 2c) VIP note!! eventhough you later defined a '__str__' method above, this line
                                                # is still necessary bc this is where the object is being deifned.
                                                # Also, this is NOT the line used to display the customer's dashboard
    print(account) # 2b) Prints the argument value passed to object 'account' by the class 'BankAccount' (see right above!)

    # 'Piece 1' used to be here!

    # Hadrcoding for test code:
    # I)
    try:
        account.deposit(100)
    except ValueError as e: 
        print(f"Error: {e}") 

    # III)
    try:
        account.withdraw(50)
    except ValueError as e: 
        print(f"Error: {e}") 

    # IV)
    try:
        account.withdraw(800)
    except ValueError as e: 
        print(f"Error: {e}") 

    # V)
    try:
        account.withdraw(-1)
    except ValueError as e: 
        print(f"Error: {e}") 

    # II)
    try:
        account.deposit(-10)
    except ValueError as e: 
        print(f"Error: {e}") 

    print(account)

main()
'''


class BankAccount:
    # Define initializer / constructor:
    def __init__(self, account_number, owner, balance=0): # Defining initialzer with dunder '__init__' (aka 'dunder init method')
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    # Define methods:
    def deposit(self, amount):
        if amount <= 0:  
            raise ValueError("Invalid amount. Enter a deposit amount greater than $0.00.") 
        self.balance += amount 
        print(f"Amount deposited: ${amount:.2f}")
        # print((f"New balance: {self.balance}")) # rounds decimal to tenths place
        # print((f"New balance: {self.balance: .2f}"))  # rounds decimal to hundreths place
        print((f"New balance: ${self.balance:.2f}"))  # rounds decimal to hundreths place
        return self.balance

# AFTER Check-order change:
    def withdraw(self, amount):
        # 1)
        if amount <= 0:  # WITHOUT this condition branch guard, It doesn’t reject non-positive amounts and account.withdraw(-100) 
                         # would pass the self.balance < amount check (500 < -100 is false), and then self.balance - (-100) 
                         # would add $100 to the account, rather than deducting.
            raise ValueError("Invalid amount. Enter a withdrawal amount greater than $0.00.") 
        # 2)
        if self.balance < amount:
            raise ValueError("Insufficient funds: cannot withdraw more than the current balance.")  
        self.balance = self.balance - amount 
        print(f"Amount withdrawn: ${amount:.2f}")
        # print((f"New balance: {self.balance}"))
        print((f"New balance: ${self.balance:.2f}"))  # rounds decimal to hundreths place
        return self.balance
        # Instructions say '(or your custom exception, if you choose to implement Task 3) indicating insufficient funds.'..go over!

    def __str__(self):
        return f"Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance:.2f}" #2a) Displays cs dashboard by default.

    # Define Objects:
    # dog1 = Dog(name = 'Max', breed = 'Boxer', color = 'blue')
    # deposit1 = BankAccount(account_number = '103345465', owner = 'Rod', balance = 0)

def main(): 
    # Creating an instance of BankAccount:
    account = BankAccount(12345, "Alice", 500) # 2c) VIP note!! eventhough you later defined a '__str__' method above, this line
                                                # is still necessary bc this is where the object is being deifned.
                                                # Also, this is NOT the line used to display the customer's dashboard
    print(account) # 2b) Prints the argument value passed to object 'account' by the class 'BankAccount' (see right above!)

    # 'Piece 1' used to be here!

    # Hadrcoding for test code:
    # I)
    try:
        account.deposit(100)
    except ValueError as e: 
        print(f"Error: {e}") 

    # III)
    try:
        account.withdraw(50)
    except ValueError as e: 
        print(f"Error: {e}") 

    # IV)
    try:
        account.withdraw(800)
    except ValueError as e: 
        print(f"Error: {e}") 

    # V)
    try:
        account.withdraw(-1)
    except ValueError as e: 
        print(f"Error: {e}") 

    # II)
    try:
        account.deposit(-10)
    except ValueError as e: 
        print(f"Error: {e}") 

    print(account)
    
# main() # Removed in order to replace it with the guard below:
if __name__ == "__main__": # 1) this prevents Python from running the whole imported file on import.
    main() # 2) this prevents Python from running the whole imported file on import.




# ///////////////////////////////////////// Temporary Removed Pieces ////////////////////////////////////

r''' 
# Piece  1
# BEFORE Check-order change:
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Invalid amount due to insufficient funds")
        if amount <= 0:  # WITHOUT this condition branch guard, It doesn’t reject non-positive amounts and account.withdraw(-100) 
                         # would pass the self.balance < amount check (500 < -100 is false), and then self.balance - (-100) 
                         # would add $100 to the account, rather than deducting.
            raise ValueError("Invalid amount. Enter a withdrawal amount greater than $0.00.") 
        self.balance = self.balance - amount 
        print(f"Amount withdrawn: {amount}")
        print((f"New balance: {self.balance}"))
        return self.balance
'''


r'''
    # Piece 2
    try:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    except ValueError as e: 
        # print(e)  
        print(f"Error: {e}") 

    try:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    except ValueError as e: 
        # print(e)  
        print(f"Error: {e}") 

'''

# //////////////////////////////////////// Side Notes: ///////////////////////////////////////////

r''' 
# VIP VIP:
self.account_number = account_number means: 
- this says "create an attribute called account_number on this object (self) and store the value that was passed in."
- ” The dot reads as “belonging to”: the thing on the left is the object, the name after the dot is the attribute. This is 
what you want.
VS
account_number.self = account_number means:
- this says "take the value that was passed in as account_number and try to attach an attribute called self to it." 
- So the object on the left of the dot is the argument, not your account. If you passed in 12345, Python would try to set .self 
on an integer and raise an AttributeError, because integers don’t allow that. Even where it didn’t error, your BankAccount
object would never get an account_number attribute, so later code like self.account_number would fail.
'''

r'''
VIP:
Check order. Your order works, but the usual convention is to validate the input first (is the amount even valid?) and then 
check the business rule (are there enough funds?). It reads more naturally, and it won’t matter for correctness here. 
Swapping them looks like this:
BEFORE:
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Invalid amount due to insufficient funds")
        if amount <= 0:  # WITHOUT this condition branch guard, It doesn’t reject non-positive amounts and account.withdraw(-100) 
                         # would pass the self.balance < amount check (500 < -100 is false), and then self.balance - (-100) 
                         # would add $100 to the account, rather than deducting.
            raise ValueError("Invalid amount. Enter a withdrawal amount greater than $0.00.") 
        self.balance = self.balance - amount 
        print(f"Amount withdrawn: {amount}")
        print((f"New balance: {self.balance}"))
        return self.balance
AFTER:
    def withdraw(self, amount):
        if amount <= 0:  # WITHOUT this condition branch guard, It doesn’t reject non-positive amounts and account.withdraw(-100) 
                         # would pass the self.balance < amount check (500 < -100 is false), and then self.balance - (-100) 
                         # would add $100 to the account, rather than deducting.
            raise ValueError("Invalid amount. Enter a withdrawal amount greater than $0.00.") 
        if self.balance < amount:
            raise ValueError("Invalid amount due to insufficient funds")
        self.balance = self.balance - amount 
        print(f"Amount withdrawn: {amount}")
        print((f"New balance: {self.balance}"))
        return self.balance













AFTER per AI:
def withdraw(self, amount):
    # Subtracts amount from balance and returns the new balance.
    # Raises ValueError if amount is not positive or exceeds the balance.
    if amount <= 0:
        raise ValueError("Invalid amount. Enter a withdrawal amount greater than $0.00.")
    if amount > self.balance:
        raise ValueError("Insufficient funds: cannot withdraw more than the current balance.")
    self.balance -= amount
    print(f"Amount withdrawn: {amount}")
    print(f"New balance: {self.balance}")
    return self.balance



'''
