#Escribe un programa que simule el control de iluminación en una casa inteligente. Pide al usuario que
#ingrese la hora actual y si alguien está en casa. Si es de noche y alguien está en casa, enciende las luces. Si
#no hay nadie en casa, apaga todas las luces. Si es de día, no importa si alguien está en casa o no, mantiene
#las luces apagadas.

def pedir_datos():
    hora = int(input("Ingrese la hora actual (0-23): "))
    presencia = input("¿Hay alguien en casa? (s/n): ").lower()
    return hora, presencia

def controlar_luces(hora, presencia):
    if 19 <= hora or hora < 6:
        if presencia == "s":
            return "Luces encendidas."
        else:
            return "Luces apagadas."
    else:
        return "Luces apagadas."

def proceso():
    hora, presencia = pedir_datos()
    resultado = controlar_luces(hora, presencia)
    print(resultado)

#***************************************************#
proceso()