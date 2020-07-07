####################### Simple Caclulator
#    Creator: Jose Daniel Rodriguez Sanchez

import sys

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
    print ("\t5. Presiona esta opcion para dsacar la potencia de valor1^valor2.")
    print ("\t6. Presiona esta opcion para salir del programa.")

    print ("\n\n\tSelecciona una opcion de arriba...")
    opcion = input ("\n\tIngresa la operacion: ")

    # Salir
    if (str(opcion) == "6"):
        salir()
        sys.exit()

    num1 = input ("\tEl valor 1: ")
    num2 = input ("\tEl valor 2: ")
    
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
        
    # Potencia
    elif (str(opcion) == "5"):
        pot(num1,num2)
        

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

def pot(number1,number2):
    mul_result = pow(float(number1),float(number2))
    print ("\n\tPotencia: " + str(number1) + " ^ " + str(number2) + " = " + str(mul_result))
    input("\n\tPresione enter para realizar otra operacion")
    opcion,num1,num2 = menu()
    operacion(opcion,num1,num2)
    
def salir():
    print ("\n\tSaliendo de la aplicacion")
    


### Imprimiento Menu Principal del Inicio


opcion,num1,num2 = menu()
operacion(opcion,num1,num2)
