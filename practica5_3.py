numeros_unicos = {1,2,3,4}
print("conjunto 1: ", numeros_unicos)
NM= input("escribe numeros separados entre si:")
numerosN = set(int(x) for x in NM.split())
print("conjunto 2: ",numerosN)
numerosL = [int(x) for x in NM.spli5,t()]
if len(numerosL) != len(numerosN) or numerosN.intersection(numeros_unicos):
    print("hay numeros repetidos")
else:
        print("Todos son unicos")
