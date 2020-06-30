# Python Project

## Description:
Read Emails from outlook account and send to Windows Remote server Share Directory. This script runs from Windows machine.


## Dependencies

### Install PIP
1) Download get-pip.py from https://phoenixnap.com/kb/install-pip-windows
2) Run python get-pip.py


### Installing module to read emails from Outlook and send to Remote Server
1) pip install pywin32 -> To connect to outlook
2) pip install pywinrm  
3) pip install pyyaml -> To configure user credentials on remote server
4) pip install smbprotocol[kerberos] -> To tranfer files using SMBConnection
