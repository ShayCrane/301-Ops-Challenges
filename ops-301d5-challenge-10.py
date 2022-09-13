#!/usr/bin/python3

# Script Name: Conditionals in Python
# Author: Shay Crane
# Date of last revision: 09/12/2022
# Description of purpose: Practice using different conditional commands in Python3:

# Create if statements using these logical conditionals. 
# Each statement should print information to the screen depending on if the condition is met.


# declaring variables
a = 10
b = 20
c = 30
d = 40


# Equals: a == b
if a == 10:
    print("a is equal to 10")


# Not Equals: a != b
if b != c:
    print("b does not equal c")


# Less than: a < b
if a < b:
    print("a is less than b")


# Less than or equal to: a <= b
if c <= d: 
    print("c is less than-- or equal to-- d")


# Greater than: a > b
if b > a: 
    print("b is greater than a")


# Greater than or equal to: a >= b
if d >= b: 
    print("d is greater than-- or equal to-- b")


# Create an if statement using a logical conditional of your choice and include the 
# elif keyword that executes when other conditions are not met.
# Create an if statement that includes both elif and else to execute when both if and elif are not met.

# declaring variables
mynum = 12 

# input from user
guess = int(input("I'm thinking of a number between 1 and 20.  Guess the number I'm thinking of: "))

if guess < mynum:
    print("your guess is too low.  play again later.")
elif guess > mynum:
    print("your guess is too high. play again later.")
else: 
    print("you guessed my number!")

# End





