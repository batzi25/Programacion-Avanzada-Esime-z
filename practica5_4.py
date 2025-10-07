cantidad = int(input("¿Cuántas personas quieres registrar? "))
nombres = []
edades = []
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    nombres.append(nombre)
    edades.append(edad)
diccionario_nombres = dict(zip(nombres, edades))
print("Diccionario de nombres y edades:", diccionario_nombres)
