
# ===================================== CONTACT BOOK APPLICATION  ================================================== #
# ============================================ CODE BEGINS ========================================================= #

# MENU
# Defining a function to display the menu:
r'''
# Attempt 1 - Incomplete:
contacts = {} # starting with creating empty dictionary
contacts["Rod"] = "5551234"  # adding a contact to my dictionary
print(contacts["Rod"]) # Testing. Renders 5551234. 
'''

def show_menu():
    print("\nContact Book Menu:") # displays menu option
    print("1) Add New Contact")  # displays menu option
    print("2) View All Contacts")  # displays menu option
    print("3) Search Contact")  # displays menu option
    print("4) Delete Contact")  # displays menu option
    print("5) Exit")  # displays menu option
# print(show_menu()) # Testing. Renders the whole menu. 

# 1) ADDING CONTACT
# 1A) # Defining add_contact() to...
## validate input
## store a new contact
r'''
# Attempt 1 - Works but Incomplete:
def add_contact(contacts):
    name = input("Please enter name: ")
    phone = input("Please enter phone_number: ")
    contacts[name] = phone
'''
# This function's job is to ask for a name and phone number, then add them to contacts.
def add_contact(contacts): # defining the function
    name = input("Enter name: ").strip() # takes in string input from a user, while removing any whitespaces from the string.

    # Conditional branch chain used to validate input data stored in 'name' from 'input().strip()'
    if name == "": # if no data entered....
        print("Name cannot be empty.") # this is the message that renders as output when return executes
        return # returns when function "add_contact(contacts)" is called and conditional branch "if name == ''" is True

    if name in contacts: # if key data entered is already stored in dictionary....
        print("That name already exists. Contact not added.")  # this is the message that renders as output when return executes
        return # returns when function "add_contact(contacts)" is called and conditional branch " if name in contacts:" is True
            # [We use it to bail out early when something is wrong, so the code below doesn’t run.]
    # Conditional branch chain used to validate input data stored in 'phone' from 'input().strip()'
    phone = input("Enter phone number (digits only): ").strip()  # takes in string input from a user, while removing any whitespaces from the string.

    if not phone.isdigit() or len(phone) < 7 or len(phone) > 15: # if key data entered is NOT of integer type OR the lenght of
                                                                 # such number entered is greater than 7...
        print("Invalid phone number. Use 7 to 15 digits only.") # this is the message that renders as output when return executes
        return # returns when function "add_contact(contacts)" is called and conditional branch 
               # "if not phone.isdigit() or len(phone) < 7 or len(phone) > 15:" is True.
               # [We use it to bail out early when something is wrong, so the code below doesn’t run.]

    contacts[name] = phone # If we got past every check, this stores the contact: key name, value phone.
                           # otherwise, add both the 'name' key and ''phone number' value as contact to 'contacts', which if
                           # you noticed the "adding" action is already performed by the 'input()' to ''name' & 'phone' variables
    print("Contact added.") # and consequently the confirmation message is displayed


# 2) VEWING CONTACTS
# 2A) # Defining view_contacts() to display every stored contact.
r'''
# Attempt 1 - Works but Incomplete:
def view_contacts(contacts):
    print(contacts)
'''
r'''
# Attempt 2 - Works but Incomplete:
def view_contacts(contacts):
    if len(contacts) == 0:
        print("Your contacts list is currently empty! Please add at least 1 contact")
    else:
        print(contacts)
'''
# Attempt 3 - Complete:
def view_contacts(contacts): # defining the function
    if len(contacts) == 0: # validating for existance of at least 1 contact, as no point in mooving forward if there is none.
        print("Your contacts list is currently empty! Please add at least 1 contact") # if the condition above is True, this
                                                                                      # this is the message that renders as output when return 
                                                                                      # execute.
    else: # otherwise.....
        for contact in contacts:  # it loops throught the 'contacts' dictionary and for each contact.....
            # print(f"{contacts[name]} = {contacts[number]}")
            # print(contact)
            # print(contacts[contact])
            print(f"{contact}: {contacts[contact]}") #...it prints the contact key (name) and the contact value (phone #)

# 3) SEARCHING CONTACTS
# 3A) # Defining 'search_contacts()' to find contacts by full or partial name
r'''
# Attempt 1 - Failed:
def search_contacts(contacts):
    search = input("Enter name to search: ")
    for contact in contacts:
    # search = input("Enter name to search: ")
        if search in contacts:
            # print(search)
            print(print(f"{contact}: {contacts[contact]}"))
        else:
            print("Name not found")
'''

r''' 
# Attempt 2 - Worked but Inaccurately:
def search_contact(contacts):
    search = input("Enter name to search: ")
    for name in contacts:
    # search = input("Enter name to search: ")
        # if search in contacts:
        if search in name:
            # print(search)
            print(print(f"{name}: {contacts[name]}"))
        else:
            print("Name not found")
'''

# # Attempt 3 - Completed:
def search_contact(contacts): # defining the function
    search = input("Enter a name to search: ").strip() # takes in string input from a user, while removing any whitespaces from the string.
    found = False # is a flag as a variable that remembers whether anything matched. Starting assuming nothing did.

    for name in contacts:  # it loops throught the 'contacts' dictionary and for each name.....
        if search in name: # ...if the name entered by the user, matches the 'name' key in the 'contacts' dictionary
            print(f"{name}: {contacts[name]}") # ...it prints the contact key (name) and the contact value (phone #)
            found = True # this flips the flag whenever a match is printed. There’s no break because we want to check every contact.

    if not found:
        print("No matching contact found.")



# 1B) Defining a main loop program to run the program and keep the contacts dictionary in one place. 
def main(): # 'main()' function. It represents the whole app
    contacts = {} # starting with an empty dictionary

    while True: # 'while' loop is set to True, to always run until breaking out of it by 'break'. And for as long as it's True (iow, 
                # until it has gone through the entire conditional brnach chain), it'll do as follows:
        show_menu() # call the function, while priting at the same time because the function has at least 1 'print()' function
                    # in it. Also, because it’s inside the loop, it prints again after every action.
        selection = input("Enter your choice (1-5): \n") # take input from the user and stores it inside the 'selection' variable for its
                                                       # value to be used anywhere else in the program.
        # Self-explanatory conditional branch chain:
        #if selection == "1": # Replaced with conditional branch below.
            # print("Add contact selected") # Replaced with conditional branch below.
        if selection == "1": # 1B)CALL TO 'add_contact(contacts)'so that if selection 1 pressed...
            add_contact(contacts) # ...call to function is executed, which allows you to add contacts to the dictionary
            # print(contacts) # VIP VIP  Testing. Renders the gradual expansion of the contacts dictionary as you add 1 contact 
                            # at a time. it will retain the input for as long as program runs, otherwise, it will lose all 
                            # obtained contact data.
        # elif selection == "2": # Replaced with conditional branch below.
            # print("View contacts selected") # Replaced with conditional branch below.
        elif selection == "2": # 2B)CALL TO 'view_contact(contacts)'so that if selection 2 pressed...
            view_contacts(contacts) #...call to function is executed, which allows you to view contacts from the dictionary
        # elif selection == "3": # Replaced with conditional branch below.
            # print("Search contact selected") # Replaced with conditional branch below.
        elif selection == "3": # 3B)CALL TO 'search_contacts(contacts)'so that if selection 3 pressed...
            search_contact(contacts) #...call to function is executed, which allows you to search contacts for a full/partial name
        elif selection == "4":
            print("Delete contact selected")
        elif selection == "5":
            print("Goodbye!")
            break # breaks the 'while' loop to prevent it from looping endlessly, since there is no increment/de-crement counter
                  # to count towards an end
        else:
            print("Invalid choice. Please enter a number from 1 to 5.") # if all of the above elif conditions retuns 'False',
                                                                        # the 'else' statement is excuted as a final alternative

main() # calls the 'main' function to run all of its actions within it


# =================================================== CODE ENDS ================================================== #



# =============================== PENDING ================================================== #

# =============================== SIDE NOTES ================================================== #
'''
#
- Because dictionary keys must be unique, a name can only exist once.
#
- We place 'contacts = {}' inside the 'main()', but before the loop. That placement is important bc if we put it inside the loop,
it would be reset to empty every time the menu repeats, and you'd lose all your contacts.
#
- so between "while True:" and "break",   it's a way to control   how  long the loop runs, without necessarily using a 
condition? Yes, that's the right way to see it. However, keeping in mind that:
1) There is still a condition, it just never changes. 'while True:' is technically a condition, but one that's always true, so it can never be the thing that stops the loop. That’s 
why the stopping job passes to break. So the two work as a pair:
-- while True: says “keep going.”
-- break says “stop now.”
2) The stopping decision moves inside the loop.
With a normal condition, Python decides whether to continue at the top of each pass. With while True: plus break, the decision 
happens in the middle, at the exact moment something specific occurs (here, the user typing 5).
#
- in reality 'main()' isn't required by Python, it's there to make your code cleaner and safer.
- In this case, defining the function by itself doesn't run it. Without that 'main()' call, you'd run the file and nothing would 
happen.
- In part,  main() handles the input and the “traffic direction,” but not all of the input/output. What main() does:
-- Asks for the menu choice (input(...))
-- Prints some messages (“Goodbye!”, “Invalid choice”)
-- Decides which feature to run, using the if / elif / else chain
- Putting it together: main() creates the empty contact book, then enters a loop that shows the menu, asks for a choice, and
 handles it, over and over until the user picks 5.
# 
In 3A), 'found = False'; 'found = True' flags Right are used here because 'break' would be wrong for this job, at least if you want partial matching to show every match.
What break does inside a for loop: it stops the loop immediately, so the remaining items are never checked.
'''

#============================= PARTS TO CONSIDER REPLACING INTO CODE AI Verified ==============================#
r''' 
# 3) VEWING CONTACTS
# 3A) # Defining view_contacts() to display every stored contact.
# Defining view_contacts() to display every stored contact
def view_contacts(contacts):
    """Print all contacts, or a message if there are none."""
    if len(contacts) == 0:
        print("Your contact list is empty.")
        return

    print("\nAll Contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
'''
r''' 
# 3) SEARCHING CONTACTS
# 3A) # Defining 'search_contacts()' to find contacts by full or partial name
def search_contact(contacts): # defining the function
    search = input("Enter a name to search: ").strip().lower()
    found = False

    for name in contacts:
        if search in name.lower():
            print(f"{name}: {contacts[name]}")
            found = True

    if not found:
        print("No matching contact found.")
'''
