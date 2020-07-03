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

date_time_start=dt.datetime.now()

argument = (sys.argv[1])

############################# Help list to use this script

#print (arguments)

if ( argument == "-h"):
    print ("*************Usage Guide************\n\n")
    input ("Press enter to continue...")
    sys.exit()
    

print ("Script started at: " + str(date_time_start.strftime("%Y-%m-%d %H:%M:%S")))

############################# Ask for the date the files are going to process
#label .begin
inputDate=input ("Enter a date with format YYYY-MM-DD: ")


############################# Check if is a valid date
year,month,day = inputDate.split('-')
isValidDate = True

try :
    date_to_process = dt.datetime(int(year),int(month),int(day))
except ValueError :
    isValidDate = False
    
if(isValidDate) :
    print ("\nInput date is valid ..")
else :
    print ("\nInput date is not valid..")
    #goto .begin
    input ("\nPlease press enter and try again...")
    sys.exit()

############################# Setting path where locate attachements
path = os.path.expanduser("~/Desktop/NSSR/")

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


#print("Index of array " + str(index_email))

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
    name,type = files.split('.')
    
    print (str(counter) + "- Reading File: " + files + " | Type: " + type)
    
    file_name= path + files
    print ("Path: " + file_name)
    
    # Read the file in binary mode
    file2transfer = open(file_name,"rb")

    #conn.storeFileFromOffset('NSSR','SP Files/' + files , file2transfer, offset=0, truncate=False, timeout=30)

    file2transfer.close()
    
print ("\nClosing connection...")

    
############################# Deleting downloaded local files

print ("\n\nDeleting Local Files:")
for files in attachement_file_names:
    print ("Deleting: " + files)
    os.remove(path + files)

# Listing remote Share Directory
print ("Listing Remote Share Directory")
conn.listPath('NSSR', 'SP Files/', pattern='*', timeout=30)

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

