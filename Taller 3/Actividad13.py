#Crea un programa que genere una lista de números enteros desde 1 hasta un número ingresado por el
#usuario. Luego, separa los números en dos listas diferentes: una para números pares y otra para números
#impares

def pedir_numero():
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 1:
        print("ingrse un número positivo")
        return pedir_numero()
    else:
        return numero

def separar_pares_impares(num):
    pares = []
    impares = []
    for i in range(1, num + 1):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

def proceso():
    numero = pedir_numero()
    pares, impares = separar_pares_impares(numero)
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    
#***************************************************#
proceso()
