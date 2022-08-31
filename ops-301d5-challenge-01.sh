#! /bin/bash

# Script: Ops Challenge Class 02 - Append; Date and Time 
# Author: Shay Crane
# Date of latest revisions 08/30/2022
# Purpose: Copies a file in a specified directory to the current working directory, while appending the file name with a timestamp.


# establishes the date and time variable
today=$(date +%Y%m%d_%H-%M-%S)

# locates the filepath/directory; this command inspired by the following article: https://linuxize.com/post/how-to-find-files-in-linux-using-the-command-line/
find /var/log/syslog

# copies directory and renames the file path with the date and time appended
# I got help from a classmate after hours, but the script did not work after making the suggested changes. I continued by editing per the output from the terminal regarding what was missing from my commands. 
cp /var/log/syslog $today.syslog

# moves the directory copy to the current working directory; this command is not necessary.  cp does the whole job. 
# mv -v syslog. /"$PWD"/$today.syslog



    

