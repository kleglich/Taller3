#Diseña un programa para controlar el riego automático de un jardín. Pide al usuario ingresar la humedad
#actual del suelo y el umbral deseado. Utiliza un bucle para monitorear la humedad. Si la humedad está por
#debajo del umbral, activa el sistema de riego durante un tiempo determinado y luego vuelve a verificar la
#humedad. Usar método rondón para generar la humedad del suelo

def pedir_datos():
    humedad_actual = float(input("Ingrese la humedad actual del suelo (0-100): "))
    umbral_deseado = float(input("Ingrese el umbral de humedad deseado (0-100): "))
    return humedad_actual, umbral_deseado

def controlar_riego(humedad_actual, umbral_deseado):    
    import random

    while humedad_actual < umbral_deseado:
        print(f"Humedad actual: {humedad_actual}%. Humedad por debajo del umbral de {umbral_deseado}%. Activando riego...")
        humedad_actual += random.uniform(5, 15)  # Incrementa la humedad de forma aleatoria
        if humedad_actual > 100:
            humedad_actual = 100
        print(f"Humedad después del riego: {humedad_actual}%")
    
    print(f"Humedad actual: {humedad_actual}%. Humedad adecuada. Riego desactivado.")
    
def proceso():
    humedad_actual, umbral_deseado = pedir_datos()
    controlar_riego(humedad_actual, umbral_deseado)

#***************************************************#
proceso()