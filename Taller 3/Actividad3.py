#Realizar un programa que solicite al usuario un número de acuerdo a ese número solicitado calcular el
#factorial del número indicado, a su vez el programa debe indicar la cantidad de números pares y la
#cantidad de números impares y el valor acumulado de los pares y el valor acumulados de los impares.

def pedir_numero():
    numero = int(input("Ingrese un número para calcular su factorial: "))
    if numero < 0:
        print("ingrese un numero positivo")
        return pedir_numero()
    else:
        return numero
    
def calcular_factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial

def analizar_pares_impares(num):
    pares = 0
    impares = 0
    suma_pares = 0
    suma_impares = 0
    for i in range(1, num+1):
        if i % 2 == 0:
            pares += 1
            suma_pares += i
        else:
            impares += 1
            suma_impares += i
    return pares, impares, suma_pares, suma_impares


def proceso():
    numero = pedir_numero()
    factorial = calcular_factorial(numero)
    pares, impares, suma_pares, suma_impares = analizar_pares_impares(numero)
    print(f"El factorial de {numero} es: {factorial}")
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")
    print(f"Suma de números pares: {suma_pares}")
    print(f"Suma de números impares: {suma_impares}")


#***************************************************#
proceso()