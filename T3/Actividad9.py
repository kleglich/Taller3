#Escribe un programa que convierta una lista de temperaturas en grados Celsius a grados Fahrenheit. Pide al
#usuario que ingrese una serie de temperaturas en Celsius, y muestra la conversión correspondiente en
#Fahrenheit para cada una.

def pedir_temperaturas():
    n = int(input("¿Cuántas temperaturas va a ingresar?: "))
    temperaturas = []
    for i in range(n):
        temp = float(input(f"Ingrese la temperatura {i+1} en Celsius: "))
        temperaturas.append(temp)
    return temperaturas


def convertir_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def mostrar_conversiones(temperaturas):
    for c in temperaturas:
        f = convertir_a_fahrenheit(c)
        print(f"{c}°C = {f:.2f}°F")

def proceso():
    temperaturas = pedir_temperaturas()
    mostrar_conversiones(temperaturas)

#***************************************************#
proceso