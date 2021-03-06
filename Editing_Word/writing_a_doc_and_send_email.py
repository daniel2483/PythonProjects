# pip install docx-mailmerge

from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import os
import email_checker_and_domain_result as email_check
import sys
#import email_checker_and_select_smtp_server as smtp_detection
import checking_smtp_server as smtp_detection

########## Functions

def ask_for_email_address():
    send_email = input ("Desea enviar este documento a algún correo (S/N)? ")
    email = ""
    
    if (send_email == "S" or send_email == "s"):
        email = input("Ingrese el correo: ")
        domain,error = email_check.domain_name(email)
        print ("Dominio de correo: " + domain)
    elif (send_email == "N" or send_email == "n"):
        sys.exit()
    else:
        print ("Opción inválidad. Ingrese de nuevo una opción.")
        ask_for_email_address()
        
    return email


########## Main

print ("")
print ("# Elija una sucursal #")
print ("\nOpciones:\n")
print ("1. Óptica Nueva Imagen.")
print ("2. Óptica Rosan Banco Nacional.")
print ("3. Óptica Rosan Parque Central.")


local = input("Cuál sucursal: ")

send_to_txt = input ("Carta dirigida a: ")
department_txt = input ("Departamento: ")
greetings = input ("Saludos: ")
reason_to_contact = input ("Razon de la carta: ")
person_name_txt = input ("Nombre de la persona que solicita: ")
id_number_txt = input ("Número de Cédula: ")

path = os.path.expanduser("~/Desktop/python/Templates/")

if(local == "1"):
    template = "carta_generica_RS.docx"

if(local == "2" or local == "3"):
    template = "carta_generica_RS.docx"

document = MailMerge( path + template)

# To check the merge fields on word Template
#print(document.get_merge_fields())  

document.merge(
    current_date='{:%d-%b-%Y}'.format(date.today()),
    send_to=send_to_txt,
    department=department_txt,
    greetings=greetings,
    reason_to_contact=reason_to_contact,
    person_name=person_name_txt,
    id_number=id_number_txt)

document.write(path + 'carta_final.docx')

print ("Word Document already created...")

# Ask for email, and if is not correct ask again
send_email_to = ask_for_email_address()

# Get the Domain and errors if is presented
domain,error = email_check.email_address(str(send_email_to))

smtp_server = smtp_detection.getting_smtp_server(str(domain))

if (smtp_server == "none"):
    print ("The SMTP Server is not supported, please choose another Email Address...")
    sys.exit()
    
else:
    print ("SMTP Server: " + smtp_server + " is supported")


    


