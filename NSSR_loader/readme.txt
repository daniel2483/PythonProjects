NSSR Load Project

Description:

Read Emails from outlook account and send to Windows Remote server Share Directory. This script runs from Windows machine.
Dependencies


Install PIP

1.    Download get-pip.py from https://phoenixnap.com/kb/install-pip-windows
2.    Run python get-pip.py

Installing module to read emails from Outlook and send to Remote Server

1.    pip install pywin32 -> To connect to outlook
2.    pip install pywinrm
3.    pip install pyyaml -> To configure user credentials on remote server
4.    pip install smbprotocol[kerberos] -> To tranfer files using SMBConnection documentation here https://pysmb.readthedocs.io/en/latest/api/smb_SMBConnection.html

or just run install all dependencies using

pip install -r requirements.txt 

process_system_incident
process_software_incident

create_l2_system_baseline.pl
create_l2_software_baseline.pl


create_l2_inc_automation.pl


perf_inc


Configuring config.yaml file


L1 charts history

remote_server: server_ip
fqdn: server_fqdn
user: username
passw: password
domain: domain
server_name: hostname
my_name: pc_computer_name





