#!/usr/bin/python3

# Script Name: Bash in Python
# Author: Shay Crane
# Date of last revision: 09/06/2022
# Description of purpose: Create a Python script that executes the bash script I created in course 201 that fetches the hardware specs of my pc.

# Requirements:

# The Python library “os” must be utilized
# At least three variables must be declared in Python that contain bash operations
# The Python function print() must be used at least three times
# Indicate in comments how you achieved this.


# Do not know how to achieve the below by adding two more variables.  
# Since I am using my bash script from 201, I only have the one operation required to perform the requested action. 


# importing the linux/bash library: 
import os


# declaring variables
var = ("bash /home/shannon/201_Ops_Challenges/oc07.sh")


# defining functions
def pythonbash(command):
    print("locating bash script that fetches system data...")
    print("running commands to execute bash script... one moment...")
    print () #to leave space btwn printed text
    print ("script found. executing...")
    print () 
    print ("just a moment...")
    print () 
    print ("just a moment...")
    print () 
    print ("executing bash script oc07.sh...")
    os.system(command)


# Main

# calling back the variables
pythonbash(var)
print()
print("the operation has ended.  that will be $550.00, please...")


# End






