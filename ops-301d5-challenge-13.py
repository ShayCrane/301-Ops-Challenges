#!/usr/bin/python3

# Script Name: GET requests
# Author: Shay Crane
# Date of last revision: 09/15/2022
# Purpose: a Python script that peforms a GET request with the user's input 

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

# Using the requests library, perform a GET request against your lab web server.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

# For the given URL, print response header information to the screen.


import requests

# example from demo
# response = requests.get('https://www.google.com')

# declaration of variables
# ask user to input a web address
url = input("please enter a web address: ")


# Print a menu with choices of HTTP methods  (GET, POST, etc)
# and ask the user to pick an option from the menu
print("Options Menu: ")
print("  1) GET")
print("  2) POST") 
print("  3) PUT") 
print("  4) DELETE")
print("  5) HEAD")
print("  6) PATCH")
print("  7) OPTIONS")

opt = input("Please choose an option and enter its number here: ")

# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS




# Conditionals
# if user picked GET - do something
read NUM
if [ $NUM -eq 1 ]
    then print("Hello World!" 
elif [ $NUM -eq 2 ]; then
    ping -c 5 127.0.0.1
elif [ $NUM -eq 3 ]; then
    ifconfig
# elif [ $NUM -eq 4 ]; then
else    
    print("You have exited the menu."
    exit 0 
fi

# response code gets put into variable
# if 404 - print "Site not found"

