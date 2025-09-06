#Escribe un programa que pida al usuario un número entero y determine si es un número primo o no. Utiliza
#un bucle y condicionales para realizar la verificación y muestra el resultado al final

def pedir_numero():
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 1:
        print("ingrese un número positivo")
        return pedir_numero()
    else:
        return numero
    
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def proceso():  
    numero = pedir_numero()
    if es_primo(numero):
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")
        
#***************************************************#
proceso()