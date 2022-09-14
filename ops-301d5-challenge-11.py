#!/usr/bin/python3

# Script Name: Python file Handling
# Author: Shay Crane
# Date of last revision: 09/13/2022
# Purpose: Using Python’s file handling capabilities to open and manipulate an existing file. 
#    This can be useful in generating log files or working with CSV or JSON data files.
#
# Objective: Using file handling commands, create a Python script that: 
#    1. creates a new .txt file; 
#    2. appends three lines; 
#    3. prints to the screen the first line; and 
#    4. deletes the .txt file.
#
# The following sites are where I found examples of the python3 commands that append contents of a given file and delete that file. 
# https://www.geeksforgeeks.org/python-append-to-a-file/
# https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/




# declares the variable; 
# creates a new .txt file; and 
# writes three lines to the body of the file for the purpose of applying the appendation. 
file = open("ops301-oc11.txt", "w")
compose = ["Python is much easier to use \n for scripting \n than bash."]
file.writelines(compose)
file.close()

# appends the text within the created file
file = open("ops301-oc11.txt", "a")
file.write("\n")
file.write("But I still like bash.")
file.close()

# prints to the screen the first line of the .txt file
file = open("ops301-oc11.txt")
print(file.read())
print()
file.close()

# imports os module in order to run the commands that will...
import os

# ...delete the .txt file
# location = "/home/shannon/test-directory/"
# path = os.path.join(location/file)

os.remove("ops301-oc11.txt")

# End. 
