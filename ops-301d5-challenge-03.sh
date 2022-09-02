#!/bin/bash

# Script: Ops Challenge Class 03 - File Permissions 
# Author: Shay Crane
# Date of latest revisions 09/01/2022
# Purpose: Creates a bash script that launches a menu system with the following options for the user to choose from: 

# - prints Hello World to the screen
# - ping self (pings this computer’s loopback address)
# - IP info (print the network adapter information for this computer)
# - exits script

# the following websites helped me with advice regarding the creation of this script:
# - https://linuxhint.com/bash_conditional_statement/

echo "Choose from the following options: 1. Hello World; 2. Ping Self; 3. IP Info; 4. Exit"
read NUM
if [ "$NUM" = 1 ]; then 
    echo "Hello World!"
        elif [ "$NUM" = 2 ]; then
            ping -c 5 "127.0.0.1"
                elif [ "$NUM" = 3 ]; then
                    ifconfig -a
                        elif [ "$NUM" = 4 ]; then
                            exit 0
fi
