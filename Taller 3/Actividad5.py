# Realizar un programa que ayude a controlar las ventas por días (lunes a domingo), debe tener un menú que
#permita ingresar datos y valores por días, imprimir el total de ventas, y el promedio de ventas de la semana.

def total_ventas(ventas):
    return sum(ventas)

def promedio_ventas(ventas):
    return sum(ventas) / len(ventas)

def proceso():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    ventas = []
    
    print("Bienvenido al sistema de control de ventas semanales")
    
    for dia in dias:
        venta = float(input(f"Ingrese las ventas del {dia}: "))
        ventas.append(venta)
    
    total = total_ventas(ventas)
    promedio = promedio_ventas(ventas)
    
    print(f"El total de ventas de la semana es: {total}")
    print(f"El promedio de ventas diarias es: {promedio}")
    
#***************************************************#
proceso()