print("Sistema de notas básico ✿ ")

def calcular_condicion(promedio, asistencia):
    if asistencia == 0:
        return "Ausente"
    elif promedio >= 8 and asistencia >= 75:
        return "Promociona"
    elif promedio >= 6 and asistencia >= 75:
        return "Regular"
    else:
        return "Libre"

alumno = input("Nombre del alumno: ")
materia = input("Materia: ")

nota1 = float(input("Ingresá la nota 1: "))
nota2 = float(input("Ingresá la nota 2: "))
nota3 = float(input("Ingresá la nota 3: "))
asistencia = float(input("Ingresá el porcentaje de asistencia: "))

promedio = (nota1 + nota2 + nota3) / 3
condicion = calcular_condicion(promedio, asistencia)

nota_mayor = max(nota1, nota2, nota3)
nota_menor = min(nota1, nota2, nota3)

print("\nResultados:\n")
print("Alumno:", alumno)
print("Materia:", materia)
print("Promedio:", round(promedio, 2))
print("Asistencia:", asistencia, "%")
print("Nota más alta:", nota_mayor)
print("Nota más baja:", nota_menor)
print("Condición:", condicion)

with open("resultados.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"Alumno: {alumno} | Materia: {materia} | Promedio: {round(promedio, 2)} | Condición: {condicion}\n")