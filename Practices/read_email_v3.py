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

for message in messages:
    index1 = message.Subject.find("Undeliverable")
    index2 = message.Subject.find("failed")
    ### Skip incorrect emails subjects
    if (index1 == -1 ):
        message_date = message.SentOn.strftime("%Y-%m-%d")
        ### Get emails attachements from input date
        if (inputDate == message_date):
            counter = counter + 1
            print(message.SentOn.strftime("%Y-%m-%d") + message.Subject)
            attachments = message.Attachments
            for attachment in message.Attachments:
                attachment.SaveAsFile(os.path.join(path, str(attachment)))

print ("Processed " + str(counter) + " file(s)")


############################# Sending files to remote server

### Reading config file
path_config = os.path.expanduser("~/Desktop/python/config.yaml")
with open(path_config) as file:
    #config_list = yaml.load(file, Loader=yaml.FullLoader)
    documents = yaml.full_load(file)
    #print(config_list)
    for item, doc in documents.items():
        if (item == "remote_server"):
            remote_server = item
        if (item == "fqdn"):
            fqdn = item
        if (item == "user"):
            user = item
        #if (item == "pass"):
        #    pass = str(item)
        #    print(item, ":", doc)
        #if (item == "domain"):
        #    domain = item
        #    print(item, ":", doc)

print("Sending files to: " + remote_server + " - FQDN : " + fqdn)

#remoteConn = winrm.Session('windows-host.example.com', auth=('john.smith', 'secret'))


print("Finished Succesfully")

