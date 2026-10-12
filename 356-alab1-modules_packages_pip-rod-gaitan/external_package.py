
r'''
Task 3: Using PIP and an External Package
- Choose a third-party package (for example, colorama or requests).
- Using PIP, install the selected package.
- Write a script (e.g., external_package.py) that:
-- Imports the package.
-- Demonstrates a simple usage of the package. For instance, if using colorama, print a colored text message; if using requests, fetch a URL and print the HTTP status code.
- Include a comment at the top of your script explaining that the package must be installed (e.g., # Requires colorama; install with: pip install colorama).
'''

# Requires colorama; install with: pip install colorama
from colorama import init, Fore, Style

# print(style.greet('Rod')) # testing call to function before moving forward. However, for this to work I had to do:
                            # "from mypackage import utilities"

init()  # makes colors work on Windows terminals

print(Fore.BLUE + "This text is in blue!")
print(Fore.RED + "This text is in red!")

print(Style.RESET_ALL + "Returns back to normal text")
