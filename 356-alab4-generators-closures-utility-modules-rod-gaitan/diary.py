'''
Task 3: Diary Entry Program (File I/O and OS Operations)

    Write a Python script (e.g., diary.py) that:
        Checks if a file named diary.txt exists in the current directory (using the os module).
        If not, creates a new file called diary.txt.
        Prompts the user to input a diary entry.
        Precedes the entry with a timestamp of the current date and time (using datetime.datetime.now()), and appends it to diary.txt.
        After appending, reads and prints the entire content of diary.txt so the user can see all past entries.
        Uses try/except blocks to catch and report errors during file operations.
'''

r''' 
# Checks if a file named diary.txt exists in the current directory (using the os module):
import os # imports 'os' module
# print(dir(os)) # fetches all the tools inside module 'os' for review.

if os.path.exists("diary.txt"):
    print("After adding 'diary.txt' to current directory: \nfile 'diary.txt' DOES exist in the current directory path")
else:
    print("Before adding 'diary.txt' to current directory: \nfile 'diary.txt' DOES NOT exist in the current directory path")
# VIP VIP: You must cd to correct directory before running the above. Otherwise, it will give inaccurate results
'''

r''' 
# Checks if a file named diary.txt exists in the current directory (using the os module):
# If not, creates a new file called diary.txt.
import os # imports 'os' module
# print(dir(os)) # fetches all the tools inside module 'os' for review.

if os.path.exists("diary_ii.txt"):
    print("'diary_ii.txt' DOES exist in the current directory path")
else:
    with open("diary_ii.txt", "a") as file:
        pass # this is a must, only because the 'with' block can’t be empty. Python requires at least one indented statement 
             # under 'with', so without 'pass' you’d get an IndentationError.
    print("A 'diary_ii.txt' file DID NOT exist in the current directory path, so a new one has been created! \n")
# VIP VIP: You must cd to correct directory before running the above. Otherwise, it will give inaccurate results
# Note: 1. created diary_ii.txt vs. diary.txt. I created 'diary_ii.txt' so I could test creation without deleting my real 'diary.txt'
'''

''' 
# Prompting the user to input a diary entry.
import os # imports 'os' module
# print(dir(os)) # fetches all the tools inside module 'os' for review.

if os.path.exists("diary.txt"):
    print("'diary.txt' DOES exist in the current directory path")
else:
    with open("diary.txt", "a") as file:
        pass # this is a must, only because the 'with' block can’t be empty. Python requires at least one indented statement 
             # under 'with', so without 'pass' you’d get an IndentationError.
    print("A 'diary.txt' file DID NOT exist in the current directory path, so a new one has been created! \n")
# VIP VIP: You must cd to correct directory before running the above. Otherwise, it will give inaccurate results
# Note: I switched back to 'diary.txt'

entry = input("Enter diary entry: ") # Prompting the user to input a diary entry.
'''

''' 
# Precedes the entry with a timestamp of the current date and time (using datetime.datetime.now()), and appends it to diary.txt.
import os # imports 'os' module
import datetime   #  imports 'datetime' module needed for the timestamp.
# print(dir(os)) # fetches all the tools inside module 'os' for review.

if os.path.exists("diary.txt"):
    print("'diary.txt' DOES exist in the current directory path")
else:
    with open("diary.txt", "a") as file:
        pass # this is a must, only because the 'with' block can’t be empty. Python requires at least one indented statement 
             # under 'with', so without 'pass' you’d get an IndentationError.
    print("A 'diary.txt' file DID NOT exist in the current directory path, so a new one has been created! \n")
# VIP VIP: You must cd to correct directory before running the above. Otherwise, it will give inaccurate results
# Note: I switched back to 'diary.txt'

entry = input("Enter diary entry: ") # Prompting the user to input a diary entry.

# 1) Build a timestamp for the current date and time:
print(dir(datetime)) # fetches all the tools inside module 'datetime' for review.
# timestamp = now() # Returns: NameError: name 'now' is not defined.
# timestamp = datetime.now() # Returns: AttributeError: module 'datetime' has no attribute 'now'
timestamp = datetime.datetime.now()  # Returns Timestamp components
# timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # AI answer: Returns Timestamp components and polished answer.
                                                                    # The .strftime(...) part just trims the output to 
                                                                    # 2026-10-22 19:49:03 instead of including microseconds. 
# print(timestamp) # For testing purposes. Returns entry plus time stamp of 2026-10-22 20:54:03.205640

# Append the timestamped entry to the file 
with open("diary.txt", "a") as file: # in this case, 'open' is not creating the file as seen previously, but updates it
                                     # "a" keeps old entries
    file.write(f"{timestamp}: {entry}")
    print(file) # wrong way to read the file!!
'''

''' 
# After appending, code will now read and print the entire content of 'diary.txt' so the user can see all past entries.
import os # imports 'os' module
import datetime   #  imports 'datetime' module needed for the timestamp.
# print(dir(os)) # fetches all the tools inside module 'os' for review.

if os.path.exists("diary.txt"):
    print("'diary.txt' DOES exist in the current directory path")
else:
    with open("diary.txt", "a") as file:
        pass # this is a must, only because the 'with' block can’t be empty. Python requires at least one indented statement 
             # under 'with', so without 'pass' you’d get an IndentationError.
    print("A 'diary.txt' file DID NOT exist in the current directory path, so a new one has been created! \n")
# VIP VIP: You must cd to correct directory before running the above. Otherwise, it will give inaccurate results
# Note: I switched back to 'diary.txt'

entry = input("Enter diary entry: ") # Prompting the user to input a diary entry.

# 1) Build a timestamp for the current date and time:
print(dir(datetime)) # fetches all the tools inside module 'datetime' for review.
# timestamp = now() # Returns: NameError: name 'now' is not defined.
# timestamp = datetime.now() # Returns: AttributeError: module 'datetime' has no attribute 'now'
timestamp = datetime.datetime.now()  # Returns Timestamp components
# timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # AI answer: Returns Timestamp components and polished answer.
                                                                    # The .strftime(...) part just trims the output to 
                                                                    # 2026-10-22 19:49:03 instead of including microseconds. 
# print(timestamp) # For testing purposes. Returns entry plus time stamp of 2026-10-22 20:54:03.205640

# Append the timestamped entry to the file 
with open("diary.txt", "a") as file: # in this case, 'open' is not creating the file as seen previously, but UPDATES it
                                     # "a" stands for 'append' and thus allows you to keep old entries while adding new ones.
    file.write(f"{timestamp}: {entry}\n")  # '\n' is critical here for each individual entry to be stored in its own line!
                                           # otherwise, input for individual entries will be appended in the same line, making
                                           # output messy as you can see below. 

with open("diary.txt", "r") as file: # in this case, 'open' is not creating the file as seen previously, but READS it
    contents = file.read()

print("#======== Diary Entries =======#")
print(contents)
'''

# Using try/except blocks to catch and report errors during file operations:
# The idea is to wrap each file operation in its own try/except so the error message tells you which step failed.
import os
import datetime

# FILENAME = "nonexistent_folder/diary.txt" # line to test Error handling for bad path
FILENAME = "diary.txt" # allows us to modify the file name or even directory path from this location, across the entire script
                       # wherever the 'FILENAME' variable is plugged in.

# Step 1: Create the file if it doesn't exist
try:  # <----------------------------------{1) exception handler try/except block starts}
    if os.path.exists(FILENAME):
        print(f"'{FILENAME}' exists in the current directory.")
    else:
        with open(FILENAME, "a"):
            pass
        print(f"'{FILENAME}' did not exist, so a new one has been created.\n")
except FileNotFoundError: # <----{4a) exception handler is triggered (instead of traceback 'FileNotFoundError' if the file or even
                                # the file path in an Absolute or Relative file path is incorrect )}
                                # Initally placed after 'OSError', causing a potential bug.
    print(f"Error: '{FILENAME}' could not be found.")  # <---{4b) message replacing the default traceback message for the 
                                                           # exception 'FileNotFoundError'.}
except PermissionError: # <----{2a) exception handler is triggered (instead of traceback 'PermissionError' if user lacks 
                                # needed permissions to access the file.)}
    print(f"Error: no permission to create '{FILENAME}'.") # <---{2b) message replacing the default traceback message for the 
                                                           # exception 'PermissionError'.}
except OSError as e: #  <-----{3a) exception handler is triggered (instead of traceback 'OSError' if operating-system-related 
                                # errors occur)}
    print(f"Error while checking/creating the file: {e}") # <---{3b) message replacing the default traceback message for the 
                                                           # exception 'OSError'.}

# Step 2: Get the entry and build the timestamp
entry = input("Enter diary entry: ")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Step 3: Append the entry
try: # <----------------------------------{1) exception handler try/except block starts}
    with open(FILENAME, "a") as file:
        file.write(f"- {timestamp}: {entry}\n")
except FileNotFoundError: # <----{4a) exception handler is triggered (instead of traceback 'FileNotFoundError' if the file or even
                                # the file path in an Absolute or Relative file path is incorrect )}
    print(f"Error: '{FILENAME}' could not be found.")  # <---{4b) message replacing the default traceback message for the 
                                                           # exception 'FileNotFoundError'.}
                                                            # Initally placed after 'OSError', causing a potential bug.
except PermissionError: # <-----{2a) exception handler is triggered (instead of traceback 'PermissionError' if user lacks needed
                                # permissions to access the file. )}
    print(f"Error: no permission to write to '{FILENAME}'.")  # <---{2b) message replacing the default traceback message for 
                                                              #the exception 'PermissionError'.}
except OSError as e: #  <-----{3a) exception handler is triggered (instead of traceback 'OSError' if operating-system-related 
                                # errors occur)}
    print(f"Error while writing to the file: {e}") # <---{3b) message replacing the default traceback message for the exception 
                                                   # 'OSError'.}

# Step 4: Read and display all entries
try:  # <----------------------------------{1) exception handler try/except block starts}
    with open(FILENAME, "r") as file:
        contents = file.read()
    print("#======== Diary Entries =======#")
    print(contents)
except FileNotFoundError: # <----{2a) exception handler is triggered (instead of traceback 'FileNotFoundError' if the file or even
                                # the file path in an Absolute or Relative file path is incorrect )}
                                 # Initally placed here, which was teh correct place to begin with.
    print(f"Error: '{FILENAME}' could not be found.")  # <---{2b) message replacing the default traceback message for the 
                                                           # exception 'FileNotFoundError'.}
except PermissionError: # <-----{3a) exception handler is triggered (instead of traceback 'PermissionError' if user lacks needed 
                                # permissions to access the file. )}
    print(f"Error: no permission to read '{FILENAME}'.") # <---{3b) message replacing the default traceback message for the 
                                                           # exception 'PermissionError'.}
except OSError as e:  # <-----{4a) exception handler is triggered (instead of traceback 'OSError' if operating-system-related 
                                # errors occur)}
    print(f"Error while reading the file: {e}")  # <---{4b) message replacing the default traceback message for the exception 
                                                   # 'OSError'.}
# Per AI - the comments are accurate !!!

# ///////////////////////////////////// Side Notes //////////////////////////////////////////////

'''
Q:
- Why Error: 'nonexistent_folder/diary.txt' could not be found gets printed twice?
A:
Each step has its own try/except, and each one fails independently:
Step 3 (write): open(FILENAME, "a") fails because nonexistent_folder/ doesn’t exist, so the FileNotFoundError handler prints 
its message.
Step 4 (read): open(FILENAME, "r") fails for the same reason, so its own FileNotFoundError handler prints a message.

'''

'''
Q:
so is "except OSError" the same as "except" by itself, where it catches everything?
A:
No. except OSError is much narrower than a bare except:
- except OSError catches only operating-system-related errors: missing files or folders, permission problems, a full disk, 
invalid file names, and similar. Anything else still crashes the program with a traceback, which is usually what you want, 
since an unrelated error probably means a real bug.
- Bare except: catches literally everything, including errors that have nothing to do with files, and even Ctrl+C 
(KeyboardInterrupt) and SystemExit. That’s why it’s discouraged: it can hide typos and bugs in your own code.

'''

'''
To Test the File:
- cd into the lab folder and run the script.
- Type an entry.
- Open diary.txt. You should see a line like 2026-10-22 19:49:03 - Today I learned closures.
- Run it again with a different entry and confirm the file now has two lines.
'''

'''
Q:
- is it only classes that live inside modules?

A:
- What can live inside a Python module?
Item	                Example
Variables	            name = "Python"
Functions	            def greet():
Classes	                class Dog:
Imports	                import math
Constants	            PI = 3.14159
Executable statements	print("Hello!")
- For example in module 'os', the following tools exist:
['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 
'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 
'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 
'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', '_check_methods', '_create_environ', '_execvpe', '_exists', '_exit', '_fspath', 
'_get_exports_list', '_walk_symlinks_as_files', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 
'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 
'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchmod', 
'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_blocking', 'get_exec_path', 
'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 
'getppid', 'isatty', 'kill', 'lchmod', 'linesep', 'link', 'listdir', 'listdrives', 'listmounts', 'listvolumes', 'lseek', 
'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'process_cpu_count', 'putenv', 
'read', 'readinto', 'readlink', 'reload_environ', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 
'sep', 'set_blocking', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 
'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids',
'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 
'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']

'''


# ///////////////////////////////////////// VIP Attempt: //////////////////////////////////////////////

'''  
# My Attempt to inserting exception handling to my code and It worked !!!!

# Using try/except blocks to catch and report errors during file operations:
import os # imports 'os' module
import datetime   #  imports 'datetime' module needed for the timestamp.
# print(dir(os)) # fetches all the tools inside module 'os' for review.

if os.path.exists("diary.txt"):
    print("'diary.txt' DOES exist in the current directory path")
else:
    with open("diary.txt", "a") as file:
        pass # this is a must, only because the 'with' block can’t be empty. Python requires at least one indented statement 
             # under 'with', so without 'pass' you’d get an IndentationError.
    print("A 'diary.txt' file DID NOT exist in the current directory path, so a new one has been created! \n")
# VIP VIP: You must cd to correct directory before running the above. Otherwise, it will give inaccurate results
# Note: I switched back to 'diary.txt'

entry = input("Enter diary entry: ") # Prompting the user to input a diary entry.

# 1) Build a timestamp for the current date and time:
print(dir(datetime)) # fetches all the tools inside module 'datetime' for review.
# timestamp = now() # Returns: NameError: name 'now' is not defined.
# timestamp = datetime.now() # Returns: AttributeError: module 'datetime' has no attribute 'now'
# timestamp = datetime.datetime.now()  # Returns Timestamp components
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # AI answer: Returns Timestamp components and polished answer.
                                                                    # The .strftime(...) part just trims the output to 
                                                                    # 2026-10-22 19:49:03 instead of including microseconds. 
# print(timestamp) # For testing purposes. Returns entry plus time stamp of 2026-10-22 20:54:03.205640

# Append the timestamped entry to the file 
try: # <----------------------------------{1) exception handler try/except block starts}
    with open("folder/diary.txt", "a") as file: # 2) added fictious directory 'folder' to trigger conflict/exception/exception handler
        file.write(f"- {timestamp}: {entry}\n")  

except FileNotFoundError: #3) once conflict/exception/exception handler is triggered you grab and paste the exception onto here
    print("Invalid file path! Fix the damn thing.") # 4a) <-----------------------------{exception handler try/except block ends}
                                                   # 4b) Returns: "Invalid file path! Fix the damn thing.".
                                                   # 4c) and it DOES NOT prevent the file from displaying the currently stored 
                                                   # entries. So this error alone will allow display of stored entries

try:  # <--------------------------------------{1) exception handler try/except block starts}
    with open("hello/diary.txt", "r") as file: # 2) added fictious directory 'hello' to trigger conflict/exception/exception handler
        contents = file.read()

    print("#======== Diary Entries =======#")
    print(contents)

except FileNotFoundError: # 3) once conflict/exception/exception handler is triggered you grab and paste the exception onto here
                          # itc, FileNotFoundError
    print("Invalid file path! Wring path dumb@$$") # 4a) <-----------------------------{exception handler try/except block ends}.
                                                   # 4b) Returns: "Invalid file path! Wring path dumb@$$".
                                                   # 4c)and it prevents the file from displaying the currently stored entries.
                                                   # So this error alone will NOT allow display of stored entries


############################  Notes: ##################################
#
Q:
- At first I thought my exception handler was not working, bc I only saw the retuned entries made and NOT the Exception message
that I had created to catch the 'FileNotFoundError' exception. It turns out I was wrong
A:
Your try/except is working. Look at the terminal output:
%
Enter diary entry: hkhkl
['MAXYEAR', 'MINYEAR', ...]
Invalid file path! Fix the damn thing.
#======== Diary Entries =======#

- That Invalid file path! line is your except FileNotFoundError: block catching the bad path and printing your message. No 
traceback appears, which is the point of exception handling: the error was caught and reported, and the program kept running. 
Earlier you got the traceback because the try/except wasn’t in the saved version.
- The diary entries listed afterward come from the read step, which opens the real diary.txt. Your new entry (hkhkl) isn’t in 
that list because the write failed, which is exactly what should happen with a bad path. So the behavior is correct end to end.

#
Q:
- At first AI did not include a "FileNotFoundError" exception handler here, when I asked why, I got the following response:
A:
- I left it out because with "a" mode, a missing file is created automatically, so I reasoned that FileNotFoundError wouldn’t come
up. That’s true for the file, but I overlooked the folder. When the folder in the path doesn’t exist, open(..., "a") raises 
FileNotFoundError, which is exactly what happened when you used /folder/diary.txt. I even mentioned this possibility in my 
explanation of the exceptions, but I didn’t carry it into the Step 3 code.
- Your script would still not crash without it. FileNotFoundError is a subclass of OSError, so the except OSError as e: clause 
would catch it and print something like Error while writing to the file: [Errno 2] No such file or directory: .... But a 
dedicated handler gives a clearer, more specific message, which is what you did.

#
VIP Personal Conclusion:
- From what I understand the most effective way to implement Exception Handling techniques, is to 
1) let Python trigger its own generic exceptions/Tracebacks
2) then from the message at the bottom of teh exception, copy the exception label (ex, 'FileNotFoundError')
3) insert that exception label after the keyword 'except' to define the exception label that you will replace with your
personal exception message.
[[Per AI's wording:
"Run the code, let Python raise the error, read the exception name on the last line of the traceback, and use that name in an 
except clause with a clear message. Then add a general catch-all (like OSError) for anything I didn’t anticipate."
Addt'l VIP Points:
a) 
Triggering errors yourself only finds the ones you think to trigger. You found FileNotFoundError because you tested a bad path.
You wouldn’t have found PermissionError that way unless you set up a read-only file. So it helps to also ask, “What else could 
realistically go wrong here?” and add handlers for those. The Python docs list built-in exceptions if you want to look them up.
b)
Keep a catch-all at the end. After your specific handlers, add except OSError as e: (for file operations) so unexpected problems 
still get reported instead of crashing. The as e lets you print the real system message with {e}.
c)
Avoid a bare 'except': with no label. It catches everything, including mistakes in your own code and Ctrl+C, which hides real bugs.
]]
'''