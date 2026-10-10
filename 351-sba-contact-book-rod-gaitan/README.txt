# Contact Book: Write-Up

## Overview
This project is a console Contact Book that lets a user add, view, search, and
delete contacts from a text menu. Contacts are stored in a dictionary where the
key is the contact's name and the value is the phone number. Because dictionary
keys must be unique, a name can only exist once.

## How I Structured the Program

| Function | Job  |
| show_menu() | Prints the menu options. |
| add_contact(contacts) | Asks for a name and phone number, validates them, and stores the contact. |
| view_contacts(contacts) | Prints every contact, or a message if the list is empty. |
| search_contact(contacts) | Finds contacts whose name contains the text the user types. |
| delete_contact(contacts) | Removes a contact by exact name, or reports that it doesn't exist. |
| main() | Creates the dictionary and runs the menu loop. |

## How Data Flows
main() creates the contacts dictionary once, before the loop, so it is not
reset each time the menu repeats. Inside a while True loop, main() shows
the menu, reads the user's choice, and calls the matching function, passing
contacts as a parameter. The functions change the same dictionary directly,
so nothing needs to be returned. The loop ends only when the user chooses 5,
which runs break.

## Validation and Error Handling
- Menu: the choice is converted to an integer inside a try/except
  ValueError block, so non-numeric input (like abc or just pressing Enter)
  shows a message instead of crashing. Numbers outside 1-5 are caught by the
  else branch.
- Names: empty names are rejected, spaces are removed with .strip(), and
  duplicate names are refused.
- Phone numbers: must contain digits only and be 7 to 15 digits long. I
  chose these rules myself because the assignment lets me decide what counts as
  valid.

## Challenges and How I Solved Them
1. Deleting while looping. My first delete_contact looped through the
   dictionary and deleted inside the loop. It crashed with RuntimeError:
   dictionary changed size during iteration, and it also removed the wrong
   contact (Rod1 when I asked for Rod2). I learned that you can't change a
   dictionary's size while looping over it, and that deleting by exact name
   doesn't need a loop at all. I replaced the loop with a check using
   "if name in contacts" followed by removing that key.
2. Calling the method on the wrong thing. I tried contacts[name].pop,
   which failed for two reasons: it had no parentheses, and contacts[name] is
   the phone number (a string), not the dictionary. The fix is to call the
   method on the dictionary itself.
3. Partial search. Search needed a loop because it checks inside every
   name. I used a found flag and no break, so that a search like rod
   shows every match instead of stopping at the first.
4. Testing every path. I tested success and failure for each feature (empty
   name, duplicate, short phone number, letters in the phone number, empty
   list, search with no match, deleting a missing contact). The results are in
   my interaction log.

##