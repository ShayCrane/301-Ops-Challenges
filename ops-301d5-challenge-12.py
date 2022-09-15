#!/usr/bin/python3

# Script Name: Psutil
# Author: Shay Crane
# Date of last revision: 09/14/2022
# Purpose: creates a Python script that fetches various process and system information using Psutil


import psutil 

# Time spent by normal processes executing in user mode
# Time spent by processes executing in kernel mode
# Time when system was idle
# Time spent by priority processes executing in user mode
# Time spent waiting for I/O to complete.
# Time spent for servicing hardware interrupts
# Time spent for servicing software interrupts
# Time spent by other operating systems running in a virtualized environment
# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print(psutil.cpu_times())

# End.