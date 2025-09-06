#Escribe un programa que solicite al usuario un número entero no negativo y calcule su factorial utilizando un
#bucle. Muestra el resultado al final.

def pedir_numero():
    numero = int(input("Ingrese un número entero no negativo para calcular su factorial: "))
    if numero < 0:
        print("ingrese un numero positivo")
        return pedir_numero()
    else:
        return numero
    
def calcular_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def proceso():
    numero = pedir_numero()
    factorial = calcular_factorial(numero)
    print(f"El factorial de {numero} es: {factorial}")
    
#***************************************************#
proceso()    
