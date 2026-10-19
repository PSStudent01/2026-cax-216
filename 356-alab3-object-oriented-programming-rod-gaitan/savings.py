r''' 
Task 2: Subclassing and Inheritance (SavingsAccount)

    In the same file or a new file (e.g., savings.py), create a subclass SavingsAccount that inherits from BankAccount:
        Additional Attribute:
            interest_rate (representing the annual interest rate as a percentage).
        Initializer:
            Modify the initializer to accept interest_rate along with other parameters and call the base class initializer using super().__init__().
        Additional Method:
            apply_interest(self): Calculate the interest based on the current balance and interest_rate, and add it to the balance. For example, if the interest rate is 5%, add balance * 0.05 to the balance.
        Method Overriding:
            Override the __str__ method to include the interest rate in the account's string representation.

    Write test code that:
        Creates an instance of SavingsAccount.
        Demonstrates the inherited deposit and withdraw functionalities.
        Calls apply_interest() and prints the account to verify that the balance updates correctly and the interest rate is displayed.
'''

# In this file (e.g., savings.py), create a subclass 'SavingsAccount' that inherits from 'BankAccount':

from bank import BankAccount # importing the SUPERCLASS 'BankAccount' from the file 'bank.py'

class SavingsAccount(BankAccount): # Declaring that SUBCLASS 'SavingsAccount' inherits from SUPERCLASS 'BankAccount'
                                   # iows, 'SavingsAccount' is a 'BankAccount', and gets everything 'BankAccount' has.
    pass

    # Additional Attribute and Modify the Initializer :
    # Add attribute 'interest_rate=0' and modify the initializer to accept interest_rate along with other parameters and call 
    # the base class initializer using super().__init__():
    # def __init__(self, interest_rate): # only listed the new attribute, but not those being inherited from 'BankAccount'
    def __init__(self, account_number, owner, balance=0, interest_rate=0): # listing the addtl attribute 'interest_rate', in 
                                                                           # addition to those being inherited from 'BankAccount'.
        super().__init__(account_number, owner, balance) # this subclass 'SavingsAccount' has to call 'super().__init__(...)', 
                                                         # so the parent’s setup (account_number, owner, balance) still runs 
                                                         # before you add 'interest_rate' attribute here in the subclass.
                                                         # 'super()' is one of Python’s built-in functions temporary stand-in 
                                                         # for the parent class, so you can call the parent’s methods from 
                                                         # inside the child class.
                                                         # VIP hands the 3 shared values up to BankAccount.__init__, which sets 
                                                         ## self.account_number, self.owner, and self.balance.
        self.interest_rate = interest_rate # This line stores the one new attribute 'interest_rate', directly on the savings 
                                           # account 'SavingsAccount' subclasss. 
                                           # Note that 'interest_rate' is not passed to 'super().__init__()', because BankAccount 
                                           # doesn’t know about it.
                                           # {THINK OF IT AS modiying the 'interest_rate' attribute to 'self.interest_rate'}

    # Additional Method:
    # apply_interest(self): Calculate the interest based on the current balance and interest_rate, and add it to the balance. 
    # For example, if the interest rate is 5%, add balance * 0.05 to the balance:
    def apply_interest(self):
        pass
        # return 0.05 * balance  # this wont work, bc it requires savings acct balance (aka self.balance, since we in 'savings.py)
                                # and even after fixing that, it'd require the interest rate to be hardcoded.
        # return interest_rate * balance  # this wont work, bc it requires savings acct balance (aka self.balance, since we in
                                          # 'savings.py). And even after fixing that, it'd require the INTEREST to be 
                                          # calculated, bc it is the INTEREST RATE (ex, 5.0) you're passing as a value, NOT
                                          # the INTEREST itself.
        # interest = (interest_rate / 100) * 1) self.balance # 'interest_rate' by itself will not work here to calculate 'interest'.
        interest = (self.interest_rate / 100) * self.balance # 2) 'self.interest_rate' will work bc it specificies that it
                                                              # is not just interest rate that we want, but rather 
                                                              # the 'interest rate for the SAVINGS ACCOUNT' to calc the interest.
        self.balance += interest # this tracks the new balance after the most recent interest rate has been applied.
        # print(f"Interest Applied: {interest_rate}") # 3) again, this line references some 'interest_rate', so it will not work
        print(f"Interest rate applied: {self.interest_rate}") # 4) rather, 'self.interest_rate' specifies that it is the 'interest rate
                                                        # for the SAVINGS ACCOUNT' that we want print
        print(f"Interest earned: ${interest:.2f}") # Optional for claritny purposes only
        print(f"New balance: ${self.balance:.2f}")  # 5)'self.balance' specifies that it is the 'balance for the SAVINGS ACCOUNT'
                                                    # that we want print and NOT the balance for 'BankAccount' in file 'bank.py' .
 
    # Method Overriding:
    # Override the __str__ method to include the interest rate in the account’s string representation.
    def __str__(self):                     
        return f"{super().__str__()}, Interest Rate: {self.interest_rate}%" 
    # Note: do not comment out line in the '__init__' method:   'super().__init__(account_number, owner, balance)'


r''' 
# Test code 1:  for interest rate:
savings = SavingsAccount(989998, "Bob", 500, 15) # creating the object 'savings'
print(savings.interest_rate) # cherrypicking attribute: extracting/accessing new 'interest_rate' attribute from the just-created
                            # 'savings' object.
print(savings.balance)  # cherrypicking attribute: extracting/accessing new 'balance' attribute from the just-created 'savings' 
                        # object.
print(savings) # extracting/accessing the entire just-created 'savings' object.
               # still the inherited '__str__' (no interest rate yet).
'''

if __name__ == "__main__":  # This line prevents this entire code from running on another file's code, after this file is 
                           # imported into another file and its attributes/functionality inherited by the file that imports it.
                           # IOWs " # Runs the indented test code only when this file is run directly. If another file imports
                           # savings.py, this block is skipped, but the SavingsAccount class is still available to it."
                           # [&&&]


    # Test code 2:  for object: 
    savings = SavingsAccount(989998, "Bob", 500, 15) # Creating the object 'savings' which is an instance of class 'SavingsAccount'.  
    print(savings)             # Printing the contents/values of the 'savings' object, BEFORE interest being applied. 
    savings.apply_interest()   # Applying the method 'apply_interest()' to the 'savings' object: 15% of 500 = 75
    print(savings)             # Printing the contents/values of the 'savings' object AFTER interest being applied., in which only
                            # the attributes 'balance' and 'interest_rate' are targeted/modified by the act of calling the
                            # 'apply_interest()' upon the 'savings' object

    # Demonstrates the inherited deposit and withdraw functionality:
    # I) Inherited 'deposit' functionality:
    # account.deposit(100) # 'account' is the incorrect object
    # savings.deposit(100) # 'savings' is the correct object
    try:
        savings.deposit(100)
    except ValueError as e:
        # print(e)
        print(f"Error: {e}")

    # II) Inherited 'withdraw' functionality.
    # account.withdraw(10)  # 'account' is the incorrect object
    # savings.withdraw(10)  # 'savings' is the correct object
    try:
        savings.withdraw(10)
    except  ValueError as e:
        # print(e)
        print(f"Error: {e}")

    # III) Exception handling of insufficient funds.
    try:
        savings.withdraw(1000)
    except  ValueError as e:
        # print(e)
        print(f"Error: {e}")

    # IV) Exception handling of invalid deposit input.
    try:
        savings.deposit(-1)
    except  ValueError as e:
        # print(e)
        print(f"Error: {e}")

    # V) Exception handling of invalid withdraw input.
    try:
        savings.withdraw(-1)
    except  ValueError as e:
        # print(e)
        print(f"Error: {e}")

    print(savings)


# ///////////////////////////////////////////Side Notes //////////////////////////////////////////////
r'''  
from bank import BankAccount # importing the SUPERCLASS 'BankAccount' from the file 'bank.py'

class SavingsAccount(BankAccount): # Declaring that SUBCLASS 'SavingsAccount' inherits from SUPERCLASS 'BankAccount'
                                   # iows, 'SavingsAccount' is a 'BankAccount', and gets everything 'BankAccount' has.
    pass
    
# Test code to prove inheritance from 'BankAccount' SUPERCLASS to 'SavingsAccount' CHILD class:
savings = SavingsAccount(67890, "Bob", 1000)
print(savings)         # uses the inherited __str__
savings.deposit(100)   # uses the inherited deposit
- these lines work because they inherit the '__init__' method,  'deposit' method, 'withdraw' method, and '__str__' method 
- from the 'BankAccount' SUPERCLASS . 
- Note: __init__ method is stil referred to as 'constructor' or 'initializer'!s
''' 

r'''
Optional possible '__str__' overide:
def __str__(self):
    return f"Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate}%"
'''

r'''
Q:
ok I'm confused 1) what does the __str__ do again? 2) why do you all say 'override'? to me override means have somethings else 
superceed the __str__ method
A:
Your understanding of “override” is correct, so let’s connect it to what’s happening here.

1) What __str__ does
__str__ is the method Python calls whenever it needs to turn an object into text, such as when you do print(savings). Without it, printing an object gives something unhelpful like <__main__.SavingsAccount object at 0x000001A2B3C4>. With it, Python prints whatever string the method returns. That’s why print(account) in bank.py shows Account 12345 – Owner: Alice, Balance: $500.00.
2) Why “override”
Your definition is exactly right: override means a newer version supersedes the old one. Here, BankAccount has a __str__, and SavingsAccount inherits it. When you define a new __str__ inside SavingsAccount, Python uses that one for savings objects instead of the inherited one. The parent’s version is superseded, but only for SavingsAccount. BankAccount objects keep using the original.

So the sequence is:
print(savings) happens
Python looks for __str__ in SavingsAccount first
It finds your new one, runs it, and never reaches the parent’s version on its own
Where super().__str__() fits
The one thing that can feel contradictory is that my version of the override still calls the parent’s
 __str__ via super().__str__(). That’s because the override doesn’t have to throw the old version away. It can reuse it and 
add to it. Think of it as: “use my version, but start from the parent’s text and add the interest rate.”
You could write the override without super() and it would still be an override:
%
def __str__(self):
    return f"Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate}%"
Both produce the same output. The super() version just avoids retyping the parent’s formatting. Either one satisfies the lab.

'''

r'''
Optional cleanup before you submit, all cosmetic:
- Delete the # print(e) lines and the old # account.deposit(100) style comments.
- Delete the two leftover pass lines.
- Wrap the test code in if __name__ == "__main__":.
- Relabel Interest Applied: 15 so it’s clear that 15 is the rate, not the dollar amount.

Q:
- what do you mean "Wrap the test code in if __name__ == "__main__":."?
A:
The line if __name__ == "__main__": is a check that asks: “Was this file run directly, or was it imported by another file?” Code indented under it only runs in the first case.

Why it matters in your project
savings.py starts with from bank import BankAccount. That means Python loads bank.py as a module. You already protected bank.py, so its test code (main()) doesn’t run during that import.
But savings.py has no such protection. If someone (or a future file of yours) did from savings import SavingsAccount, Python would run the whole file, including your test code at the bottom. You’d see all the “Bob” output and the error messages appear, even though they only wanted the class.

How the check works
Python gives every file a built-in variable called __name__:
When you run the file directly (like you do in VS Code or the terminal), __name__ is set to "__main__". The condition is true, so the indented code runs.
When another file imports it, __name__ is set to the file’s name ("savings"). The condition is false, so the indented code is skipped.
The classes still get defined either way. Only the test code is skipped on import.

How it would look in your file
You take your test code and indent it one level under the if. Here is a trimmed version of your bottom section: - See [&&&]
Running it directly gives the same output as now. The guard only changes what happens on import, so your terminal output won’t 
change at all.
'''

r'''
When uploading to remote HitHUb repo, don’t commit '__pycache__'. The __pycache__/bank.cpython-314.pyc file was created when savings.py imported bank.py. 
It’s generated automatically and doesn’t belong in the repo. Create a file named .gitignore in the lab folder (or in the repo 
root if one already exists) containing:
'''

# ////////////////////////////////////// Pending: ///////////////////////////////////////////////////

r'''
Task 3: Custom Exception Class (Optional Extension)

    (Optional) Define a custom exception class InsufficientFundsError in your module:
        The class should inherit from Python’s built-in Exception class.
    Modify the withdraw method in BankAccount so that when a withdrawal amount exceeds the balance, it raises InsufficientFundsError (instead of ValueError).
    Update your test code to catch InsufficientFundsError specifically and print an appropriate error message (e.g., “Insufficient funds: cannot withdraw $X from account Y”).

'''