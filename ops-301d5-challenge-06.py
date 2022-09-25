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
var1 = ("lshw -class CPU | grep 'product\|vendor\|physical\|bus\|width'")
var2 = ("lshw -class RAM | grep 'description\|physical\|size'")
var3 = ("lshw -class DISPLAY | grep 'description\|product\|vendor\|physical\|bus\|width\|clock\|capabilities\|configuration\|resources'")
var4 = ("lshw -class NETWORK | grep 'description\|product\|vendor\|physical\|bus\|logical\|version\|serial\|size\|size\|capacity\|width\|clock\|capabilities\|configuration\|resources'")
# defining functions
def pythonbash(command):
    print("locating bash scripts that fetch system data...")
    print("running commands to execute bash script... one moment...")
    print () #to leave space btwn printed text
    print ("scripts found. executing...")
    print () 
    print ("just a moment...")
    print () 
    print ("executing bash scripts using lshw command...")
    os.system(command)


# Main

# calling back the variables
pythonbash(var1)
pythonbash(var2)
pythonbash(var3)
pythonbash(var4)
print()
print("the operation has ended.  that will be $550.00, please...")


# End






