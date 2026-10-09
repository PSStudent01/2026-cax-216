
# ===================================== CONTACT BOOK APPLICATION  ================================================== #
# ============================================ CODE BEGINS ========================================================= #

# 1) MENU
# 1a) Defining a function to display the menu:
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

# 2) ADDING CONTACT
# 2a) # Defining add_contact() to...
## validate input
## store a new contact
r'''
# Attempt 1 - Works but Incomplete:
def add_contact(contacts):
    name = input("Please enter name: ")
    phone = input("Please enter phone_number: ")
    contacts[name] = phone
'''








# 1b) Defining a main loop program to run the program and keep the contacts dictionary in one place. 
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
            #print("Add contact selected") 
        if selection == "1": # if selection 1 pressed...
            add_contact(contacts) # call to function is executed, which allows you to add contacts to the dictionary
            # print(contacts) # Testing. Renders the gradual expansion of the contacts dictionary as you add 1 contact at a time.
        elif selection == "2":
            print("View contacts selected")
        elif selection == "3":
            print("Search contact selected")
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

'''

#============================= PARTS TO CONSIDER REINSTALLING ==============================#

r''' 
# 2) ADDING CONTACT - COMPLETE WITH ALL FEATURES!!!!!!
# Defining add_contact() to validate input and store a new contact
def add_contact(contacts):
    """Ask for a name and phone number, then add them to contacts."""
    name = input("Enter name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    if name in contacts:
        print("That name already exists. Contact not added.")
        return

    phone = input("Enter phone number (digits only): ").strip()

    if not phone.isdigit() or len(phone) < 7 or len(phone) > 15:
        print("Invalid phone number. Use 7 to 15 digits only.")
        return

    contacts[name] = phone
    print("Contact added.")
'''