r'''   
The Permission Matrix (Bitwise vs. Logical)

Goal: Spot the difference between logical operators (and, or) which evaluate whole truths, and bitwise operators (&, |) which manipulate raw binary data.
Your Mission
Let's pretend we are defining user permissions using binary flags.
READ = 4 (In binary: 100)
WRITE = 2 (In binary: 010)
EXECUTE = 1 (In binary: 001)
If a user has Read and Write permissions, their combined total is 4 + 2 = 6 (Binary: 110).
Write a quick script to test if a user with a permission score of 6 has the WRITE permission enabled using the
bitwise & (AND) operator.
'''

''' 
print(bin(4)) # 100
print(bin(2)) # 010
print(bin(1)) # 001
print(bin(6)) # 110
'''


#print(bin(6)) # 100 + print(bin(2)) # 010  = 6 (Binary: 110).

# score = int(input("Enter score: "))

''' 
if bin(4):
    print("If score is 4, user has 'READ' permissions")

if bin(2):
    print("If score is 2, user has 'WRiTE' permissions")

if bin(1):
    print("If score is 1, user has 'EXECUTE' permissions")
'''

r'''  
# Attempt 1 - takes a score, only by calling the function while passing a specific argument, and returns its binary value :
# n = int(input("Enter score: "))

def score(n):
    print(bin(n))
    # return
    # return bin(n)

# score()
score(1)
'''


r'''  
# Attempt 2 - takes a score from user and returns it binary value:
n = int(input("Enter score: "))

def score(n):
    print(bin(n))
    # return
    # return bin(n)

# score()
score(n)
'''


r'''  
# Attempt 3 - takes a score from user and returns it binary value and ______________________________:
n = int(input("Enter score: "))

def score(n):
    if n == 4:
        binary = bin(4)
        print(f"User has a binary score of {binary} and therefore 'READ' permissions")
    elif n == 2:
        binary = bin(2)
        print(f"User has a binary score of {binary} and therefore 'WRITE' permissions")
    elif n == 1:
        binary = bin(1)
        print(f"User has a binary score of {binary} and therefore 'EXECUTE' permissions")
    else:
        print("Enter a score!")
    
# score()
score(n)
'''

r''' 
# Attempt 4 - logig off
n = int(input("Enter score: "))

if n == 4:
    binary = bin(4)
    print(f"User has a binary score of {binary} and therefore 'READ' permissions")
elif n == 2:
    binary = bin(2)
    print(f"User has a binary score of {binary} and therefore 'WRITE' permissions")
elif n == 1:
    binary = bin(1)
    print(f"User has a binary score of {binary} and therefore 'EXECUTE' permissions")
else:
    print("Enter a score!")
'''
    

READ = 4      # 100
WRITE = 2     # 010
EXECUTE = 1   # 001

n = int(input("Enter score: "))
print(f"Score {n} in binary: {n:03b}")

if n & WRITE: # So '&' with 'WRITE' asks the question “is the WRITE 'position' (position 2) switched on in this score of 6 {iows, is the '2' switched 'on' (1) or 'off'(2)}?”
              # {iows, does score of 6 (110) have score 2 (010) INCLUDED in it? and the answer is yes}  
    print("User has WRITE permission")
else:
    print("User does NOT have WRITE permission")


# ////////////////////// VIP Note://///////////////////////////////
'''
Q:
- what is 7 in binary?
A:
position:   4s  2s  1s
7        =   1   1   1  = [111]

Q:
- what is 8 in binary?
A:
position:   8s  4s  2s  1s
8        =   1   0   0   0 = [1000]
{- had to borrow a bit to get position 8
- consequently 8 = 1000 in binary
- bc the 2 position is '0' (off)...
- we can conclude that the user does NOT have WRITE permission}
- and so on:
%
psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials
$ C:/Users/psrga/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/psrga/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/python_in-class_activities/bonus-mission-labs/the-permission-matrix/the-permission-matrix.py"
Enter score: 9
Score 9 in binary: 1001 <--------------{*}  
User does NOT have WRITE permission <--------------{*}
%
psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials
$ C:/Users/psrga/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/psrga/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/python_in-class_activities/bonus-mission-labs/the-permission-matrix/the-permission-matrix.py"
Enter score: 10
Score 10 in binary: 1010  <--------------{*}
User has WRITE permission  <--------------{*}

side note:
1) lay out as many base 2 positions as possible:
...512  256  128  64  32  16  8  4  2  1
2) then to make a binary, you simply turn on a switch for the number that you want by assiging a '1' to it, and leave the rest at 0.” 
3) for example, by referencing the base 2 posiiton table above, you can do:
1 = 001
2 = 010
3 = 011
4 = 100
5 = 101
6 = 110
7 = 111
8 = 1000
9 = 1001
10 = 1010
- Please note, my padding is inconsistent. FOr example. I wrote 1 as 001 but 8 as 1000
'''


# ///////////////////////// Spare Parts ///////////////////////////////

'''
if bin(4) == 0b100:
    print("User has 'READ' permissions")

if bin(2) == 0b10:
    print("User has 'WRiTE' permissions")

if bin(1) == 0b1:
    print("User has 'EXECUTE' permissions")
'''

'''
    if bin(4) == 0b100:
        print("User has 'READ' permissions")
    elif bin(2) == 0b10:
        print("User has 'WRiTE' permissions")
    elif bin(1) == 0b1:
        print("User has 'EXECUTE' permissions")
    else:
        print("Enter a score!")
'''
#'''


'''  
n = int(input("Enter score: "))

if n == 4:
        binary = bin(4)
        print(f"User has a binary score of {binary} and therefore 'READ' permissions")
if n == 2:
        binary = bin(2)
        print(f"User has a binary score of {binary} and therefore 'WRITE' permissions")
if n == 1:
        binary = bin(1)
        print(f"User has a binary score of {binary} and therefore 'EXECUTE' permissions")
else:
        print("Enter a score!")
'''

#//////////////////////////////////////// Side Notes /////////////////////////////////////////

r''' 
[[[[ 
- In the case of checking all 3 permissions:
Because each check is independent, use three separate if statements instead of if/elif. With elif, only the first match would ever print:
%
if n & READ:
    print("READ")
if n & WRITE:
    print("WRITE")
if n & EXECUTE:
    print("EXECUTE")

For 6, this prints READ and WRITE.

Why & and not and

This is the logical vs. bitwise point the exercise is after:

python
print(6 & 2)     # 2  -> bitwise: compares bits, keeps the shared ones
print(6 and 2)   # 2  -> logical: both are truthy, so it just returns the last value
print(5 & 2)     # 0  -> bitwise: no shared bits, WRITE is off
print(5 and 2)   # 2  -> logical: both are nonzero, so it "succeeds" even though WRITE is off

5 and 2 treats both numbers as simply “true,” so it would wrongly suggest the user has WRITE. Only & looks inside the binary. ]]]
'''


