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
from smb.SMBConnection import SMBConnection

date_time=dt.datetime.now()



print ("Script start at: " + str(date_time))

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
    print ("Input date is valid ..")
else :
    print ("Input date is not valid..")
    #goto .begin
    sys.exit()

############################# Setting path where locate attachements
path = os.path.expanduser("~/Desktop/NSSR/")
    
 
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

print("Aldea email: " + aldea_email)


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
                attachment.SaveAsFile(os.path.join(path, str(attachment)))
                ### Store File Names in an array
                attachement_file_names.append(str(attachment))

print ("Processed " + str(counter) + " file(s)")


############################# Reading parameters

parameters = []
remote_server = ""
user=""
passw=""
domain=""
host=""


### Reading config file
path_config = os.path.expanduser("~/Desktop/python/config.yaml")
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
        if (item == "host"):
            host = doc
            
            

print ("Connecting to remote server: " + remote_server + " - " + fqdn)
#print ("File Names to send: " + str(attachement_file_names[1]))

############################# Sending files to remote serve

#remote_path="F:\Shares\NSSR\SP Files"
### Register Session
#smbclient.register_session(str(remote_server), username=str(user), password=str(passw))

#smbclient.mkdir(r"\\server\share\directory", username="user", password="pass")

conn = SMBConnection(user, passw, host, server_name, domain=domain_name, use_ntlm_v2=True,is_direct_tcp=True)



print("Finished Succesfully")

