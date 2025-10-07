n = input("Escribe nombres  separados por una coma: ")
nombres = [nombre.strip() for nombre in n.split(",") if
           nombre.strip()]
t = {}
for nombre in nombres:
     n = nombre[0].upper()
     Telosforo[n] = Telosforo.get(n,0) + 1
print("Conteo de iniciales: ", t)
