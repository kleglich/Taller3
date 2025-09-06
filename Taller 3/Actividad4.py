#Realizar un programa en donde muestre un menú en donde tenga la opciones de solicitar dos números por
#consola, dentro del menú se pueda multiplicar, dividir, sumar y restar mostrando el resultado de la
#operación, de igual el programa debe quedar activo solicitando los datos hasta que el usuaria seleccione la
#opción de salir

def proceso(): 
    print("Bienvenido a la calculadora básica")
    while True:
        print("Seleccione una opción:")
        print("1. Sumar \n2. Restar \n3. Multiplicar \n4. Dividir \n5. Salir")
        
        opcion = int(input("Ingrese el número de la opción deseada: "))
        
        match (opcion):
            case 1:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                resultado = sumar(a, b)
                print(f"El resultado de la suma es: {resultado}")
                
            case 2:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                resultado = restar(a, b)
                print(f"El resultado de la resta es: {resultado}")
                
            case 3:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                resultado = multiplicar(a, b)
                print(f"El resultado de la multiplicación es: {resultado}")
                
            case 4:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                resultado = dividir(a, b)
                print(f"El resultado de la división es: {resultado}")
                
            case 5:
                exit()
                


def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b    
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."
    
    
    
#***************************************************#
proceso()

