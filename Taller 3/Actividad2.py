#Realizar un programa en donde se ingresa los nombres de tres estudiantes con sus respectivas notas (p1,
#p2, p3), luego calcular la nota final de cada estudiante, preguntar si desea continuar en caso de no seguir
#ingresando datos, presentar al final un resumen de cuantos aprobados, cuantos reprobados y el promedio
#total de las definitivas de los estudiantes.


def calcular_definitiva(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def ingresar_estudiantes():
    estudiantes = []
    while True:
        for i in range(3):
            nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
            nota1 = float(input("Ingrese la nota 1: "))
            nota2 = float(input("Ingrese la nota 2: "))
            nota3 = float(input("Ingrese la nota 3: "))
            definitiva = calcular_definitiva(nota1, nota2, nota3)
            estudiantes.append({"nombre": nombre, "definitiva": definitiva})
        continuar = input("¿Desea ingresar más estudiantes? (s/n): ").lower()
        if continuar != "s":
            break
    return estudiantes

def resumen(estudiantes):
    aprobados = 0
    reprobados = 0
    suma_definitivas = 0
    for est in estudiantes:
        if est["definitiva"] >= 3:
            aprobados += 1
        else:
            reprobados += 1
        suma_definitivas += est["definitiva"]
    promedio = suma_definitivas / len(estudiantes) if estudiantes else 0
    print(f"\nResumen:")
    print(f"Total de estudiantes: {len(estudiantes)}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")
    print(f"Promedio de definitivas: {promedio:.2f}")

def proceso():
    estudiantes = ingresar_estudiantes()
    resumen(estudiantes)

#***************************************************#
proceso()


        