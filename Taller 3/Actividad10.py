#Desarrolla un programa que solicite al usuario un número entero y genere la tabla de multiplicar
#correspondiente utilizando un bucle. Imprime la tabla de multiplicar del número ingresado.

def pedir_numero():
    numero = int(input("Ingrese un número entero para generar su tabla de multiplicar: "))
    return numero

def tabla_multiplicar(num):
    tabla = []
    for i in range(1, 11):
        tabla.append(f"{num} x {i} = {num * i}")
    return tabla

def proceso():
    numero = pedir_numero()
    tabla = tabla_multiplicar(numero)
    print(f"Tabla de multiplicar del {numero}:")
    for p in tabla:
        print(p)
        
#***************************************************#
proceso()