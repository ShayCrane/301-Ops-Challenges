A#!/bin/bash

# Script: Ops Challenge Class 03 - File Permissions 
# Author: Shay Crane
# Date of latest revisions 09/01/2022
# Purpose: Creates a bash script that launches a menu system with the following options for the user to choose from: 

# - prints Hello World to the screen
# - ping self (pings this computer’s loopback address)
# - IP info (print the network adapter information for this computer)
# - exits script

B# Parts of the script were inspired by: 
# - https://linuxhint.com/bash_conditional_statement/
# - https://askubuntu.com/questions/1705/how-can-i-create-a-select-menu-in-a-shell-script

echo "Options Menu:" 
echo "  1) Print: Hello World!" 
echo "  2) Ping Loopback" 
echo "  3) Network Adapter Info" 
echo "  4) Exit"

read NUM
if [ $NUM -eq 1 ]; then 
    echo "Hello World!"
elif [ $NUM -eq 2 ]; then
    ping -c 5 127.0.0.1
elif [ $NUM -eq 3 ]; then
    ifconfig
elif [ $NUM -eq 4 ]; then
    exit 0 
fi


# if [[ $NUM == 1 ]]; then

# read NUM
#case $NUM in 
#    1) echo "Hello World!" ;;
#    2) ping -c 5 "127.0.0.1" ;;
#    3) ifconfig | grep -v 127.0.0.1 ;;
#    4) echo "You have exited the menu." ;;
# B   exit ;;
# esac
 

# PS3=Options Menu: 
# options=(Print Hello World! to the screen" "Ping Loopback" "Network Adapter Info" "Exit Menu)
# select opt in "${options[@]}"
# do 
#     case $opt in
#         "Option 1")
#             echo "Hello World!"
#             ;;
#         "Option 2")
#             ping -c 5 127.0.0.1
#             ;;
#         "Option 3")
#             ifconfig -a
#             ;;
#         "Exit Menu")
#             break
#             ;;
#     esac
# done



# Below is a record of the second attempt at writing the above script, kept for posterity and learning purposes.
# Parts of the script were inspired by: 
# - https://linuxhint.com/bash_conditional_statement/
# - https://askubuntu.com/questions/1705/how-can-i-create-a-select-menu-in-a-shell-script

# echo "Options Menu:" 
# echo "1. Hello World" 
# Becho "2. Ping Loopback" 
# echo "3. Network Adapter Info" 
# echo "4. Exit"
# echo "What would you like to do? Enter the option number below:"
# read NUM

# if [ "$NUM" = 1 ]; then 
#     echo "Hello World!"
# elif [ "$NUM" = 2 ]; then
#     ping -c 5 127.0.0.1
# elif [ "$NUM" = 3 ]; then
#     ifconfig -a
#B elif [ "$NUM" = 4 ]; then
#     exit 0
# fi


