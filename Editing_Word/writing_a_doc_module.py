# pip install docx-mailmerge

from __future__ import print_function
from mailmerge import MailMerge
from datetime import date



def saving_word_letter(business, send_to_txt, department_txt, greetings, reason_to_contact, person_name_txt,
                       id_number_txt, path_file):
    #send_to_txt = input ("\nPara: ")
    #department_txt = input ("Departamento: ")
    #greetings = input ("Saludos: ")
    #reason_to_contact = input ("Razon de la carta: ")
    #person_name_txt = input ("Nombre de la persona que solicita: ")
    #id_number_txt = input ("Número de Cédula: ")

    path = path_file

    #print (str(business))

    if business != 0:
        template = "carta_generica_RS.docx"
    else:
        template = "carta_generica_NI.docx"

    document = MailMerge(path + template)

# To check the merge fields on word Template
#print(document.get_merge_fields())

    document.merge(
        current_date='{:%d-%m-%Y}'.format(date.today()),
        send_to=send_to_txt,
        department=department_txt,
        greetings=greetings,
        reason_to_contact=reason_to_contact,
        person_name=person_name_txt,
        id_number=id_number_txt)

    document.write(path + 'carta_final.docx')


def saving_word_letter_mediciones(business, send_to_txt, department_txt, greetings,
                                  reason_to_contact, person_name_txt, id_number_txt,
                                  sphere_l_txt, sphere_r_txt, cylinder_l_txt, cylinder_r_txt,
                                  axis_l_txt, axis_r_txt, av_l_txt, av_r_txt,
                                  path_file):
    #send_to_txt = input ("\nPara: ")
    #department_txt = input ("Departamento: ")
    #greetings = input ("Saludos: ")
    #reason_to_contact = input ("Razon de la carta: ")
    #person_name_txt = input ("Nombre de la persona que solicita: ")
    #id_number_txt = input ("Número de Cédula: ")

    path = path_file

    #print (str(business))

    if business != 0:
        template = "carta_generica_RS_recetas.docx"
    else:
        template = "carta_generica_NI_recetas.docx"

    document = MailMerge(path + template)

# To check the merge fields on word Template
#print(document.get_merge_fields())

    document.merge(
        current_date='{:%d-%m-%Y}'.format(date.today()),
        send_to=send_to_txt,
        department=department_txt,
        greetings=greetings,
        reason_to_contact=reason_to_contact,
        person_name=person_name_txt,
        id_number=id_number_txt,
        sphere_l=sphere_l_txt,
        sphere_r=sphere_r_txt,
        cylinder_l=cylinder_l_txt,
        cylinder_r=cylinder_r_txt,
        axis_l=axis_l_txt,
        axis_r=axis_r_txt,
        av_l=av_l_txt,
        av_r=av_r_txt)

    document.write(path + 'carta_final.docx')
