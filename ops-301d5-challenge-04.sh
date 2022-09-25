#!/bin/bash

# Script: Ops Challenge Class 03 - System Info 
# Author: Shay Crane
# Date of latest revisions 09/01/2022
# Purpose: Creates a bash script that launches a menu system with the following options for the user to choose from: 

# - prints Hello World to the screen
# - ping self (pings this computer’s loopback address)
# - IP info (print the network adapter information for this computer)
# - exits script

# Parts of the script were inspired by: 
# https://askubuntu.com/questions/1705/how-can-i-create-a-select-menu-in-a-shell-script

# I have completely overhauled my original script.  I've left both previous versions below the working script for review.  

PS3='Please enter your choice: '
options=("Hello World!" "Ping your pc's loopback address" "Print IP info to the screen" "Quit menu")
select opt in "${options[@]}"
do
    case $opt in
        "Hello World!")
            echo "you chose to ping Hello World! to your screen... hurray..."
            echo "Hello World!"
            ;;
        "Ping your pc's loopback address")
            echo "you chose to ping your loopback address... and there was much rejoicing... yay..."
            ping -c 5 127.0.0.1 
            ;;
        "Print IP info to the screen")
            echo "you chose to print your ip info to the screen... woah, slow down there, friend... don't get too"
            ifconfig 
            ;;
        "Quit menu")
            break
            ;;
        *) echo "invalid option";;
    esac
done


# echo "Options Menu:" 
# echo "  1) Print: Hello World!" 
# echo "  2) Ping Loopback" 
# echo "  3) Network Adapter Info" 
# echo "  4) Exit"

# read NUM
# if [ $NUM -eq 1 ]; then 
#     echo "Hello World!"
# elif [ $NUM -eq 2 ]; then
#     ping -c 5 127.0.0.1
# elif [ $NUM -eq 3 ]; then
#     ifconfig
# # elif [ $NUM -eq 4 ]; then
# else    
#     echo "You have exited the menu."
#     exit 0 
# fi


 
# versions of the script i tried: 
# None worked. 
#
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


# echo "Options Menu:" 
# echo "  1) Print: Hello World!" 
# echo "  2) Ping Loopback" 
# echo "  3) Network Adapter Info" 
# echo "  4) Exit"
# # Infinite for loop with break
# read NUM
# for (( ; ; ))
# do
#     echo "Iteration: ${NUM}"
#     (( $NUM++ ))
#     if [[ $NUM -lt 2 ]]
#     then
#     echo "Hello World!"
    
#     if [[ $NUM -lt 2 ]]
#     then
#     echo "Hello World!"

#     if [[ $NUM -lt 2 ]]
#     then
#     echo "Hello World!"

#     if [[ $NUM -lt 2 ]]
#     then
#         break;
# fi
# echo "You have exited the menu."