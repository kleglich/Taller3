#Desarrolla un programa que solicite al usuario una palabra y determine si es un palíndromo (se lee igual de
#izquierda a derecha que de derecha a izquierda). Utiliza un bucle y condicionales para realizar la verificación
#y muestra el resultado al final

def pedir_palabra():
    palabra = input("Ingrese una palabra: ")
    return palabra

def palindromo(palabra):
    palabra = palabra.lower()
    longitud = len(palabra)
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - 1 - i]:
            return False
    return True

def proceso():
    palabra = pedir_palabra()
    if palindromo(palabra):
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")
        
#***************************************************#
proceso()