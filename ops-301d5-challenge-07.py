#!/usr/bin/python3

# Script Name: Creating/recalling) Directories
# Author: Shay Crane
# Date of last revision: 09/07/2022
# Description of purpose: Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.

# Requirements:
# Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.

# Ideas for script commands and structure were obtained by reading the following sites: 
# https://stackabuse.com/getting-user-input-in-python/ 
# https://www.pythonforbeginners.com/code-snippets-source-code/python-os-walk
# https://realpython.com/python-sleep/



# Import libraries

import os
import time


# Declaration of variables

print("when prompted, please enter your desired file path. ")
print(" ")
fpath = input("enter your desired file path now:  ")


# Declaration of functions
# Main
### Pass the variable into the function here

for root, dirs, files in os.walk(fpath):
    ### Add a print command here to print ==root==
    print("root:  ")
    print(" ")
    print(root)
    
    time.sleep(1) #slows down the operation of the script (optional)
    
    
    ### Add a print command here to print ==dirs==
    print("subdirectories:  ")
    print(" ")
    print(dirs)


    ### Add a print command here to print ==files==
    print("files:  ")
    print(" ")
    print(files)

# End

 