#Diseñar un programa que muestre un menú, dicho menú debe mostrar el área y perímetro de triangulo,
#cuadrado, circunferencia.

def proceso ():
    print("bienvenido a la calculadora de áreas y perímetros")
    print("Seleccione una opción:")
    print("1. Área y perímetro de un triángulo \n2. Área y perímetro de un cuadrado \n3. Área y perímetro de una circunferencia \n4. Salir")
    
    opcion = int(input("Ingrese el número de la opción deseada: "))
    
    match (opcion):
        case 1:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            lado1 = float(input("Ingrese el lado 1 del triángulo: "))
            lado2 = float(input("Ingrese el lado 2 del triángulo: "))
            lado3 = float(input("Ingrese el lado 3 del triángulo: "))
            area, perimetro = area_perimetro_triangulo(base, altura, lado1, lado2, lado3)
            print(f"Área del triángulo: {area}")
            print(f"Perímetro del triángulo: {perimetro}")
            
        case 2:
            lado = float(input("Ingrese el lado del cuadrado: "))
            area, perimetro = area_perimetro_cuadrado(lado)
            print(f"Área del cuadrado: {area}")
            print(f"Perímetro del cuadrado: {perimetro}")    
        
        case 3:
            radio = float(input("Ingrese el radio de la circunferencia: "))
            area, perimetro = area_perimetro_circulo(radio)
            print(f"Área de la circunferencia: {area}")
            print(f"Perímetro de la circunferencia: {perimetro}")
            
        case 4:
            exit()        
            
def area_perimetro_triangulo (base, altura, lado1, lado2, lado3):
    area = (base * altura) / 2
    perimetro = lado1 + lado2 + lado3
    return area, perimetro

def area_perimetro_cuadrado (lado):
    area = lado * lado
    perimetro = lado * 4
    return area, perimetro

def area_perimetro_circulo (radio):
     area = 3.1416 * (radio ** 2)
     perimetro = 2 * 3.1416 * radio
     return area, perimetro



#***************************************************#
proceso()