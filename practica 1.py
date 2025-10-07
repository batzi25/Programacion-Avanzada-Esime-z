from os import system
if __name__ =='__main__':
    system ('cls')
palabra = input ('escribe una palabra por favor')
print ('hola tu palabra es',palabra)
L1 = list(palabra)
print(f'lista{L1}')
for dato in L1:
    contados = L1.count(dato)
    print (f'la letra {dato} se encuentra', contados, 'veces')
    
