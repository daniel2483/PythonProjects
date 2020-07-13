# pip install docx-mailmerge
from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import os

path = os.path.expanduser("~/Desktop/python/Templates/")

template = "carta_generica_RS.docx"

document = MailMerge( path + template)

# To check the merge fields on word Template
#print(document.get_merge_fields())

document.merge(
    current_date='{:%d-%b-%Y}'.format(date.today()),
    send_to='Municipalidad',
    department='Departamento de Patentes',
    reason_to_contact='la siguiente carta es para ...',
    person_name='Alejandro Rodríguez Sánchez',
    id_number='1-4433-4343')

document.write(path + 'carta_final.docx')
