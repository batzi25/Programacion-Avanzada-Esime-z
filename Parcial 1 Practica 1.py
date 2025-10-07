#* Escribir un programa que pida al usuario una frase y muestre en pantalla el número de veces que contiene cada palabra.
from os import system
if __name__ =='__main__':
    system ('cls')
frase = input ('escribe una frase por favor')
print ('hola tu frase es',frase)
L1 = frase.split()
#usamos el split() para separar
print(f'lista de palabras en {L1}')
for palabra in L1:
#usamos .count() para contar los valores
    contados = L1.count(palabra)
    print (f'la apalabra {palabra} se encuentra', contados, 'veces')
    
