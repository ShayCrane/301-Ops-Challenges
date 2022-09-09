# Script Name: PowerShell Command, "New-ADUser"
# Author: Shay Crane
# Date of last revision: 09/08/2022
# Description of purpose: a Powershell script that adds the given user to AD

# Requirements: Windows Server with AD DS installed and the server promoted to Domain Controller

# In your Windows Server, access Powershell ISE.

# Write a Powershell script that adds the below person to AD.
# Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. Franz is part of the TPS Department. Franz’s email is ferdi@GlobeXpower.com.
# Test your script. Verify in ADAC that the user was created with the correct attributes. If anything is missing, delete the user in ADAC and re-attempt from Powershell ISE.

New-ADUser -SamAccountName "ferdi" -Name "Franz Ferdinand" -Title "TPS Report Lead" -Department "TPS Department" -Office "Springfield, OR" -Company "Globex USA" -EmailAddress "ferdi@GlobeXpower.com"