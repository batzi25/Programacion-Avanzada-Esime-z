#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, etc.)
#a) en una lista, pregunte al usuario la calificación que ha obtenido en cada asignatura
#b) Muestre el promedio del semestre
#c) Indique cual fue la calificación más alta
#d) Muestre cual fue la calificación más baja
#e) Genere otra lista con las asignaturas aprobadas.
#f) Genere otra lista con las asignaturas que el usuario tiene que repetir.
# Lista de asignaturas
asignaturas = ["calculo", "Física", "Química", "ecuaciones", "humanidades"]
calificaciones = []
for materia in asignaturas:
    nota = float(input(f"Introduce la calificación de {materia}: "))
    calificaciones.append(nota)
print("\nCalificaciones obtenidas:")
for i in range(len(asignaturas)):
    print(f"{asignaturas[i]}: {calificaciones[i]}")
promedio = sum(calificaciones) / len(calificaciones)
print(f"\nPromedio del semestre: {promedio:.2f}")

# Calificación más alta y baja
calificacion_alta = max(calificaciones)
print(f"Calificación más alta: {calificacion_alta}")
calificacion_minima = min(calificaciones)
print(f"Calificación más baja: {calificacion_minima}")

# Lista de asignaturas aprobadas y reprobadas
aprobadas = [asignaturas[i]
             for i in range(len(asignaturas))
             if calificaciones[i] >= 6]
reprobadas = [asignaturas[i]
              for i in range(len(asignaturas))
              if calificaciones[i] < 6]

print("\nAsignaturas aprobadas:", aprobadas)
print("Asignaturas a re''probadas y tenddras que repetir:", reprobadas)

    

