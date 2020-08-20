# pip install docx-mailmerge

from __future__ import print_function
from mailmerge import MailMerge
from datetime import date


def saving_word_letter(business, send_to_txt, department_txt, greetings, reason_to_contact, person_name_txt,
                       id_number_txt, path_file, codigo_txt):
    # send_to_txt = input ("\nPara: ")
    # department_txt = input ("Departamento: ")
    # greetings = input ("Saludos: ")
    # reason_to_contact = input ("Razon de la carta: ")
    # person_name_txt = input ("Nombre de la persona que solicita: ")
    # id_number_txt = input ("Número de Cédula: ")

    path = path_file

    # print (str(business))

    if business != 0:
        template = "carta_generica_RS.docx"
    else:
        template = "carta_generica_NI.docx"

    document = MailMerge(path + template)

    # To check the merge fields on word Template
    # print(document.get_merge_fields())

    fecha = formattingDate()

    document.merge(
        current_date=fecha,
        send_to=send_to_txt,
        department=department_txt,
        greetings=greetings,
        reason_to_contact=reason_to_contact,
        person_name=person_name_txt,
        id_number=id_number_txt,
        codigo=codigo_txt)

    document.write(path + 'carta_final.docx')


def saving_word_letter_mediciones(business, send_to_txt, department_txt, greetings,
                                  reason_to_contact, person_name_txt, id_number_txt,
                                  sphere_l_txt, sphere_r_txt, cylinder_l_txt, cylinder_r_txt,
                                  axis_l_txt, axis_r_txt, av_l_txt, av_r_txt,
                                  path_file, codigo_txt):
    # send_to_txt = input ("\nPara: ")
    # department_txt = input ("Departamento: ")
    # greetings = input ("Saludos: ")
    # reason_to_contact = input ("Razon de la carta: ")
    # person_name_txt = input ("Nombre de la persona que solicita: ")
    # id_number_txt = input ("Número de Cédula: ")

    path = path_file

    # print (str(business))

    if business != 0:
        template = "carta_generica_RS_recetas.docx"
    else:
        template = "carta_generica_NI_recetas.docx"

    document = MailMerge(path + template)

    # To check the merge fields on word Template
    # print(document.get_merge_fields())

    fecha = formattingDate()

    document.merge(
        current_date=fecha,
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
        av_r=av_r_txt,
        codigo=codigo_txt)

    document.write(path + 'carta_final.docx')


def formattingDate():

    fechaYear = '{:%Y}'.format(date.today())
    fechaMonth = '{:%m}'.format(date.today())
    fechaDay = '{:%d}'.format(date.today())
    fechaMonthName = ""

    if fechaMonth == "01":
        fechaMonthName = "Enero"
    if fechaMonth == "02":
        fechaMonthName = "Febrero"
    if fechaMonth == "03":
        fechaMonthName = "Marzo"
    if fechaMonth == "04":
        fechaMonthName = "Abril"
    if fechaMonth == "05":
        fechaMonthName = "Mayo"
    if fechaMonth == "06":
        fechaMonthName = "Junio"
    if fechaMonth == "07":
        fechaMonthName = "Julio"
    if fechaMonth == "08":
        fechaMonthName = "Agosto"
    if fechaMonth == "09":
        fechaMonthName = "Septiembre"
    if fechaMonth == "10":
        fechaMonthName = "Octubre"
    if fechaMonth == "11":
        fechaMonthName = "Noviembre"
    if fechaMonth == "12":
        fechaMonthName = "Diciembre"

    fecha = fechaDay + " de " + fechaMonthName + " de " + fechaYear

    return fecha
