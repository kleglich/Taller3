#Crea un programa que solicite al usuario un número entero positivo y calcule la suma de todos los números
#pares desde 2 hasta el número ingresado, utilizando un bucle. Muestra el resultado al final

def pedir_numero():
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 1:
        print("ingrese un numero positivo")
        return pedir_numero()
    else:
        return numero
    
def sumar_pares(num):
    suma = 0
    for i in range(2, num + 1, 2):
        suma += i
    return suma

def proceso():
    numero = pedir_numero()
    suma = sumar_pares(numero)
    print(f"La suma de todos los números pares desde 2 hasta {numero} es: {suma}")
    
#***************************************************#
proceso()