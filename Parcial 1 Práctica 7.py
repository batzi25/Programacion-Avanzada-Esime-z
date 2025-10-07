# Programa de Quiniela de Fútbol en Python
# El usuario solo introduce los goles, sin registrar nombres de equipos.
# Se usan listas y diccionarios para guardar los resultados.
import random
equipos = ["Chivas", "América", "Atlante", "cruz azul"]
num_partidos = 15
resultados = []
for i in range(num_partidos):
    eq1, eq2 = random.sample(equipos, 2)
    print(f"\nPartido {i+1}: {eq1} vs {eq2}")
    g1 = int(input(f"Goles de {eq1}: "))
    g2 = int(input(f"Goles de {eq2}: "))
    resultados.append([eq1, g1, eq2, g2])
print("\n=== Resultados Finales ===")
for i, partido in enumerate(resultados):
    eq1, g1, eq2, g2 = partido
    print(f"Partido {i+1}: {eq1} {g1} - {g2} {eq2}")
    if g1 > g2:
        print(f"   Ganó {eq1}")
    elif g1 < g2:
        print(f"   Ganó {eq2}")
    else:
        print("   Empate")




