#Usar listas y diccionarios de Python
#Dadas n calificaciones (en la escala del 0 al 10) generadas aleatoriamente,
#calcular la frecuencia de c/u. Mostrar en pantalla los resultados

import random
n = int(input("¿Cuantas calificaciones quieres?"))
calificaciones = [random.randint(0, 10)
for _ in range(n)]
f={}
for cal in calificaciones:
    f[cal] = f.get(cal,0)+1
print("Calificaciones generadas: ", calificaciones)
print("Frecuencia de las calificaciones: ")
for cal, freq in sorted(f.items()):
        print(f"Calificaciones {cal}: {freq} veces")
