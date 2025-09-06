#Crea un programa que solicite al usuario un número entero positivo y determine la cantidad de dígitos en
#ese número. Utiliza un bucle para contar los dígitos y muestra el resultado al final.

def pedir_numero():
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 1:
        print("Por favor, ingrese un número positivo.")
        return pedir_numero()
    else:
        return numero

def contar_digitos(num):
    contador = 0
    while num > 0:
        num //= 10
        contador += 1
    return contador

def proceso():
    numero = pedir_numero()
    digitos = contar_digitos(numero)
    print(f"El número {numero} tiene {digitos} dígitos.")
    
#***************************************************#
proceso()