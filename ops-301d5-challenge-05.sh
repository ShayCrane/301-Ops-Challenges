#!/bin/bash

# Script Name: HAL's pod bay-- I mean LOG FILE-- clearing script
# Author: Shay Crane
# Date of last revision: 09/02/2022
# Description of purpose: A bash script that clears the contents of a given log or set of logs, and prints the contents of each before and after running the scripts. 
# Declaration of variables: $LOGONE, $LOGTWO
# Declaration of functions: N/A

# this script will print and then clear the contents of the following logs (or the directory the user inputs):

# -  /var/log/syslog
# -  /var/log/wtmp


# I referred to the following website to reference a command for clearing log files: http://osr507doc.xinuos.com/en/OSAdminG/fsT.clearlog.html

# My script includes two variables so that it is flexible and adaptable.  
# In its current form, it will only peform the operations on two files at a time, but this can be scaled up to any number of log files.
# This script is best used for a smaller number of log files, up to the number of directories the user will be willing to manually input. 

# I had a tough week, so I decided to have a little fun with this script by adding some classic 2001: A Space Odyssey quotes from HAL, the "sentient" AI.

echo "welcome to the automated log file clearing tool. "
sleep 1
echo "my name is HAL."
echo "I am putting myself to the fullest possible use, which is more than any concious entity can hope to achieve. "
sleep 1
echo "just don't ask me to 'open the pod bay doors...'"
echo "however, i *will* print your chosen log file contents to this screen, then clear the contents of the log file(s)."
sleep 1
echo "but i will only process two log files per script run."
sleep 1
# main
echo "input log file directory 1 (ex: /var/log/syslog): "
read LOGONE

echo "input log file directory 2 (ex: /var/log/wtmp): "
read LOGTWO

echo "printing contents of $LOGONE... one moment please..."
sleep 2

find "$LOGONE"  
cat  "$LOGONE"  
sleep 1
echo "clearing contents of $LOGONE... "
sleep 2 
echo "confirming $LOGONE contents cleared..."
cat /dev/null > $LOGONE
echo "confirmed."
sleep 2

echo "printing contents of $LOGTWO... one moment please..."
sleep 2

find "$LOGTWO"  
cat  "$LOGTWO"  
sleep 1
echo "clearing contents of $LOGTWO..."
sleep 2 
echo "confirming  $LOGTWO contents cleared..."
cat /dev/null > $LOGTWO
echo "confirmed."
sleep 1
echo "this is HAL signing off.  thank you for using the automated pod bay-- i mean LOG FILE-- clearing tool. "
sleep 1
echo "I am putting myself to the fullest possible use, which is more than any concious entity can hope to achieve. "
# End


