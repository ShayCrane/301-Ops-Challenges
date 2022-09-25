#!/usr/bin/python3

# Script Name: Bash in Python
# Author: Shay Crane
# Date of last revision: 09/06/2022
# Description of purpose: PYthon Collections, Working with Lists


#          0         1        2         3        4        5         6         7         8        9
list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

print("printing entire list...")

print(list)

print("printing fourth element of the list...")

print(list[3])

print("printing the sixth through the tenth element of the list...")

print(list[5:9])

print("changing value of the seventh element to onion...")

list[6] = "onion" 

print("printing updated list...")

print(list)



