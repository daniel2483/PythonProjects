####################### Simple Caclulator
#    Creator: Jose Daniel Rodriguez Sanchez

import sys
import math

def menu():
    ########## Menu

    print ("\n\n")
    print ("\t##################################################")
    print ("\t#                                                #")
    print ("\t# Esto es una calculadora simple hecha en python #")
    print ("\t#                                                #")
    print ("\t##################################################")

    print ("\n\n\tOpciones:\n")
    print ("\t1. Presiona esta opcion para sumar dos numeros.")
    print ("\t2. Presiona esta opcion para restar dos numeros.")
    print ("\t3. Presiona esta opcion para multiplicar dos numeros.")
    print ("\t4. Presiona esta opcion para dividir dos numeros.")
    print ("\t5. Presiona esta opcion para optener el residuo de la division de dos numeros.")
    print ("\t6. Presiona esta opcion para optener la parte entera de la division.")
    print ("\t7. Presiona esta opcion para optener la parte entera y residuo de division.")
    print ("\t8. Presiona esta opcion para sacar la potencia de valor1^valor2.")
    print ("\t9. Presiona esta opcion para optener factorial de un numero.")
    print ("\t10. Presiona esta opcion para salir del programa.")

    print ("\n\n\tSelecciona una opcion de arriba...")
    opcion = input ("\n\tIngresa la operacion: ")

    # Salir
    if (str(opcion) == "10"):
        salir()
        sys.exit()

    num1 = input ("\tEl valor 1: ")
    
    ### Para Calculo de Facorial, solo se necesita un numero
    if (str(opcion) != "9"):
        num2 = input ("\tEl valor 2: ")
    else:
        num2=0
    
    return opcion,num1,num2
    
def operacion(opcion,num1,num2):
    ### Opciones de calculadora
    # Sumando
    if (str(opcion) == "1"):
        suma(num1,num2)

    # Restando
    elif (str(opcion) == "2"):
        resta(num1,num2)

    # Multiplicando
    elif (str(opcion) == "3"):
        mult(num1,num2)

    # Dividiendo
    elif (str(opcion) == "4"):
        div(num1,num2)
        
    # Residuo
    elif (str(opcion) == "5"):
        res(num1,num2)
        
    # Parte entera
    elif (str(opcion) == "6"):
        floor(num1,num2)
        
    # Floor y Residuo
    elif (str(opcion) == "7"):
        floor_res(num1,num2)
        
    # Potencia
    elif (str(opcion) == "8"):
        pot(num1,num2)
    
    # Factorial
    elif (str(opcion) == "9"):
        fac(num1)

    # Mensaje Error
    else:
        print("Elija una option correcta!")
        input("Presione enter para continuar...")
        opcion,num1,num2 = menu()
        operacion(opcion,num1,num2)

def suma(number1,number2):
    sum_result = float(number1) + float(number2)
    print ("\n\tSuma: " + str(number1) + " + " + str(number2) + " = " + str(sum_result))
    input("\n\tPresione enter para realizar otra operacion")
    opcion,num1,num2 = menu()
    operacion(opcion,num1,num2)
    

def resta(number1,number2):
    res_result = float(number1) - float(number2)
    print ("\n\tSuma: " + str(number1) + " - " + str(number2) + " = " + str(res_result))
    input("\n\tPresione enter para realizar otra operacion")
    opcion,num1,num2 = menu()
    operacion(opcion,num1,num2)
    
def div(number1,number2):
    div_result = float(number1) / float(number2)
    print ("\n\tSuma: " + str(number1) + " / " + str(number2) + " = " + str(div_result))
    input("\n\tPresione enter para realizar otra operacion")
    opcion,num1,num2 = menu()
    operacion(opcion,num1,num2)
    
def mult(number1,number2):
    mul_result = float(number1) * float(number2)
    print ("\n\tSuma: " + str(number1) + " * " + str(number2) + " = " + str(mul_result))
    input("\n\tPresione enter para realizar otra operacion")
    opcion,num1,num2 = menu()
    operacion(opcion,num1,num2)
    
def res(number1,number2):
    res_result = float(number1) % float(number2)
    print ("\n\tResiduo: " + str(number1) + " % " + str(number2) + " = " + str(res_result))
    input("\n\tPresione enter para realizar otra operacion")
    opcion,num1,num2 = menu()
    operacion(opcion,num1,num2)
    
def floor(number1,number2):
    floor_result = float(number1) // float(number2)
    print ("\n\tParte entera: " + str(number1) + " / " + str(number2) + " = " + str(floor_result))
    input("\n\tPresione enter para realizar otra operacion")
    opcion,num1,num2 = menu()
    operacion(opcion,num1,num2)

def floor_res(number1,number2):
    floor_result = int(number1) // int(number2)
    print ("\n\tParte entera: " + str(number1) + " / " + str(number2) + " = " + str(floor_result))
    res_result = float(number1) % float(number2)
    print ("\n\tResiduo: " + str(number1) + " % " + str(number2) + " = " + str(res_result))
    input("\n\tPresione enter para realizar otra operacion")
    opcion,num1,num2 = menu()
    operacion(opcion,num1,num2)

def pot(number1,number2):
    mul_result = pow(float(number1),float(number2))
    print ("\n\tPotencia: " + str(number1) + " ^ " + str(number2) + " = " + str(mul_result))
    input("\n\tPresione enter para realizar otra operacion")
    opcion,num1,num2 = menu()
    operacion(opcion,num1,num2)

def fac(number1):
    mul_result = math.factorial(int(number1))
    print ("\n\tFactorial: " + str(number1) + "! = " + str(mul_result))
    input("\n\tPresione enter para realizar otra operacion")
    opcion,num1,num2 = menu()
    operacion(opcion,num1,num2)

def salir():
    print ("\n\tSaliendo de la aplicacion")
    


### Imprimiento Menu Principal del Inicio


opcion,num1,num2 = menu()
operacion(opcion,num1,num2)
