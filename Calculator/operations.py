import math

def sum(number1,number2):
    sum_result = float(number1) + float(number2)
    #print (str(number1) + " + " + str(number2) + " = " + str(sum_result))
    return sum_result

def sub(number1,number2):
    res_result = float(number1) - float(number2)
    return res_result
    
def div(number1,number2):
    try:
        div_result = float(number1) / float(number2)
    except ZeroDivisionError:
        div_result = "∞"
    return div_result
    
def mult(number1,number2):
    mul_result = float(number1) * float(number2)
    return mul_result
    
def res(number1,number2):
    res_result = float(number1) % float(number2)
    return res_result
    
def floor(number1,number2):
    floor_result = float(number1) // float(number2)
    return floor_result

def pot(number1,number2):
    pow_result = pow(float(number1),float(number2))
    return pow_result

def fac(number1):
    fac_result = math.factorial(int(number1))
    return fac_result
    
def sqr(number1):
    sqr_result = math.sqrt(float(number1))
    return sqr_result
