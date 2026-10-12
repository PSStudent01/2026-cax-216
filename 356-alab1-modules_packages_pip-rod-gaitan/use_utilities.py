from mypackage import utilities

print(utilities.greet('Rod'))

# print(utilities.factorial(5))
print(f"The factorial of 5 is {utilities.factorial(5)}") # 1c) ...whicc I did.

'''
When running this 'main' file as follows, you should get back:
%
psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/356-alab1-modules_packages_pip-rod-gaitan (main)
$ python use_utilities.py
Hello Rod!
120
...indicating that your package import works: 
- VIP CONCLUSION: The 'use_utilities.py' found 'mypackage', loaded 'utilities', and called both functions 'greet('Rod')' and 'factorial(5)'.
'''