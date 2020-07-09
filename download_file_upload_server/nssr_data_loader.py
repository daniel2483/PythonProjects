import win32com.client
import win32com
import os
import sys
import re
import time
import datetime as dt
import goto
import winrm
import yaml
import subprocess
import shutil
from smb.SMBConnection import SMBConnection
from pathlib import Path

date_time_start=dt.datetime.now()

#####################################################################
#                              Functions                            #
#####################################################################

############################# Help Usage message function
def HelpMessage():
        print ("\n*************Usage Guide************\n\n")
        print (" Description: This script is inteded to Load Data into NSSR Share Directory for OC Platform\n\n")
        print (" Usage:\n")
        print (" nssr_data_loader.py -h\t\t\tThis will show help usage guide")
        print (" nssr_data_loader.py\t\t\tThis will ask in prompt for a particular date with the following format YYYY-MM-DD")
        print (" nssr_data_loader.py -d YYYY-MM-DD\tAdding date Argument to start download for a particular date with YYYY-MM-DD format\n\n")
        #input ("Press enter to continue...")
        sys.exit()




#####################################################################
#                              Main                                 #
#####################################################################

############################# Help Guide to use this script and Date option

arguments = (sys.argv)

#print (arguments)
counter_arg = 0
date_arg = ""
date_arg_flag = "False"

for arg in arguments:
    if ( arg == "-h"):
        HelpMessage()
    if ( arg == "-d"):
        next_arg = counter_arg + 1
        try:
            date_arg = arguments[next_arg]
            date_arg_flag = "True"

            ### Check Date argument format. 3 values split by -

            date_arg_chk = date_arg.split("-")
            date_arg_length = len(date_arg_chk)

            if (date_arg_length != 3):
                print ("\nDate Argument has incorrect Format Try again..\n\n")
                HelpMessage()

            print ("Processing Data from: " + str(arguments[next_arg]))
        except IndexError:
            print ("\nMissing Date value...")
            HelpMessage()
    counter_arg = counter_arg + 1




# Printing start datetime of execution
print ("Script started at: " + str(date_time_start.strftime("%Y-%m-%d %H:%M:%S")))

############################# Ask for the date the files are going to process or Use arguments

if (date_arg_flag == "True"):
    inputDate = date_arg
else:
    inputDate=input ("Enter a date with format YYYY-MM-DD: ")



############################# Check if is a valid date
year,month,day = inputDate.split('-')
isValidDate = True

try :
    date_to_process = dt.datetime(int(year),int(month),int(day))
except ValueError :
    isValidDate = False

if(isValidDate) :
    print ("\nInput date is valid ..\n")
else :
    print ("\nInput date has incorrect Date Format Try again..\n\n")
    HelpMessage()
    #input ("\nPlease press enter and try again...")
    #sys.exit()

############################# Setting path where locate attachements and check if NSSR directoy exists on Desktop

path = os.path.expanduser("~/Desktop/NSSR/")
isDirectory = os.path.isdir(path)

print ("Checking if " + str(path) + " exists: " + str(isDirectory))

if (isDirectory == False):
    print ("\nCreating Local Directory " + str(path) + "\n\n")
    os.mkdir(path)

############################# Clearing the local directory
#shutil.rmtree(os.path.expanduser("~/Desktop/NSSR/"))
for filename in os.listdir(path):
    print (filename)
    os.remove(path + filename)
    print ("Deleted: " + str(filename))



############################# Reading Email

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
accounts= win32com.client.Dispatch("Outlook.Application").Session.Accounts;

aldea_account="no"
index=-1

############################# Loop to check if aldea account is set on outlook
for list in accounts:
    #print ("Account " + str(list))
    index=index +1 # this is the index pointer of the array
    if "aldea" in str(list):
            aldea_account="yes"
            aldea_email= str(list)
            index_email=index
            #print("There is an aldea account set on Outlook")
            #print(str(list))
            break

# Terminate the script if there is no aldea account set on outlook
if (aldea_account == "no"):
    print("There is no aldea account set on Outlook...")
    input("Press enter to exit the program...")
    sys.exit()

print("Is there an aldea account? " + aldea_account)

print("\nAldea email: " + aldea_email)


############################# Reading aldea email inbox
inbox = outlook.Folders(aldea_email).Folders('Inbox')

messages=inbox.Items
#message = messages.GetLast()
#body_content = message.body
#subject_content = message.Subject
#print (body_content)


############################# Filtering emails

counter = 0
attachement_file_names = []

print ("\nDownloading Files from Email:")
for message in messages:
    index1 = message.Subject.find("Undeliverable")
    index2 = message.Subject.find("failed")
    ### Skip incorrect emails subjects
    if (index1 == -1 ):
        message_date = message.SentOn.strftime("%Y-%m-%d")
        ### Get emails attachements from input date
        if (inputDate == message_date):
            counter = counter + 1
            print(message.SentOn.strftime("%Y-%m-%d : ") + message.Subject)
            attachments = message.Attachments
            for attachment in message.Attachments:
                ### Downloading Files from Email
                attachment.SaveAsFile(os.path.join(path, str(attachment)))
                ### Store File Names in an array
                attachement_file_names.append(str(attachment))

print ("Processed " + str(counter) + " file(s)")


############################# Reading config file

parameters = []
remote_server = ""
user=""
passw=""
domain=""


### Reading YAML config file
path_config = "./config.yaml"
with open(path_config) as file:
    #config_list = yaml.load(file, Loader=yaml.FullLoader)
    documents = yaml.full_load(file)
    #print(config_list)
    for item, doc in documents.items():
        #print ("Parameters: " + item + " : " + doc)
        parameters.append(item + ":" + doc)
        if (item == "remote_server"):
            remote_server = doc
        if (item == "fqdn"):
            fqdn = doc
        if (item == "user"):
            user = doc
        if (item == "passw"):
            passw = doc
        if (item == "domain"):
            domain = doc
        if (item == "server_name"):
            server_name = doc
        if (item == "my_name"):
            my_name = doc


print ("\n################## Remote Windows Connection ##################")
print ("Connection to remote server: " + remote_server + " - " + fqdn)
#print ("File Names to send: " + str(attachement_file_names[1]))

############################# Sending files to remote server, but first check if the file already exists

### Stablished connection
counter = 0
conn = SMBConnection(user, passw, my_name, server_name, domain=domain, use_ntlm_v2=True,is_direct_tcp=True)

print ("Connecting...")
connected = conn.connect(remote_server, 445)
print ("Is connection stablished? " + str(connected))

print ("\nStoring files...\n")

for files in attachement_file_names:

    counter = counter + 1
    file_name= path + files

    name,type = files.split('.')
    file_size = Path(file_name).stat().st_size
    print (str(counter) + "- Reading File: " + files + " | Type: " + type + " | Size: " + str(file_size) + " bytes")


    print ("Path: " + file_name)

    # Read the file in binary mode
    file2transfer = open(file_name,"rb")

    conn.storeFileFromOffset('NSSR','SP Files/' + files , file2transfer, offset=0, truncate=False, timeout=30)

    file2transfer.close()

print ("\nClosing connection...")


############################# Deleting downloaded local files

print ("\n\nDeleting Local Files:")
for files in attachement_file_names:
    print ("Deleting: " + files)
    os.remove(path + files)

# Listing remote Share Directory
#print ("Listing Remote Share Directory")
#conn.listPath('NSSR', 'SP Files/', pattern='*', timeout=30)

print("Script Finished Succesfully!\n\n")

conn.close()

############################# Getting the Elapse Time

date_time_end=dt.datetime.now()

print ("Script finished at: " + str(date_time_end.strftime("%Y-%m-%d %H:%M:%S")))

date = dt.date(1, 1, 1)
datetime1 = dt.datetime.combine(date, date_time_start.time())
datetime2 = dt.datetime.combine(date, date_time_end.time())

time_elapse = datetime2 - datetime1

print ("\nElapse Time: " + str(time_elapse))

input("\n*************************\nPress enter to finish...")
