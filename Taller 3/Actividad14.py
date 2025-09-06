#Diseña un programa que simule el control de temperatura en una habitación. Debes solicitar al usuario
#ingresar la temperatura actual y el valor deseado. Utiliza un bucle para ajustar gradualmente la temperatura
#actual hacia el valor deseado. Si la temperatura actual supera el valor deseado, activa el aire
#acondicionado. Si la temperatura está por debajo, activa la calefacción. Detén el bucle cuando la
#temperatura actual esté dentro de un rango aceptable. Utilizar el método rondón para realizar valores de
#temperatura


def pedir_temperatura():
    temp_actual = float(input("Ingrese la temperatura actual de la habitación: "))
    temp_deseada = float(input("Ingrese la temperatura deseada de la habitación: "))
    return temp_actual, temp_deseada

def ajustar_temperatura(temp_actual, temp_deseada):
    
    import random
    rango_aceptable = 0.5 
    while abs(temp_actual - temp_deseada) > rango_aceptable:
        if temp_actual > temp_deseada:
            print(f"Temperatura actual: {temp_actual}°C. Activando aire acondicionado...")
            temp_actual -= random.uniform(0.5, 1.5) 
        else:
            print(f"Temperatura actual: {temp_actual}°C. Activando calefacción...")
            temp_actual += random.uniform(0.5, 1.5) 
        
        print(f"Nueva temperatura: {temp_actual}°C")
    
    print(f"Temperatura ajustada a {temp_actual}°C, dentro del rango aceptable.")
    
def proceso():
    temp_actual, temp_deseada = pedir_temperatura()
    ajustar_temperatura(temp_actual, temp_deseada)
    
#***************************************************#
proceso()

