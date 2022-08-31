#! /bin/bash

# Script: Ops Challenge Class 03 - File Permissions 
# Author: Shay Crane
# Date of latest revisions 08/31/2022
# Purpose: Alters file permissions of everything in a given directory.



# Prompts user for input directory path.
echo enter path of the desired directory
read DNUM 


# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
echo enter your three digit permissions number
read PNUM

# Navigates to the directory input by the user and changes all files inside it to the input setting.
# Thank you to the following website for guidance regarding the chmod command in this context: 
# https://www.pluralsight.com/blog/it-ops/linux-file-permissions
cd /"$DNUM" | chmod "$PNUM" /"$DNUM"


# Prints to the screen the directory contents and the new permissions settings of everything in the directory.
# Command found at: https://clas.uiowa.edu/linux/help/start/permissions
ls -v -l "$DNUM" 





# -----------------------------------------------
# Pursue stretch goals if you are a more advanced user or have remaining lab time:
# Design your script to output a log file of all actions that were taken by the script.
# Design your script to output to the screen each file changed one by one, with a slight delay between each file changed.