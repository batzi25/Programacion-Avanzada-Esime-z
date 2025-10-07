#escribe un programa de guarde en un diccionario los nombres
#y precios de las frutas.
#el programa debe preguntar al usuario por una frutay la cantidad (en kilos),
#y mostrar el precio total
import os

def pinta(dic):
    # .items() da llave y valor al mismo tiempo
    for dato, valor in dic.items():
        print(f'\t{dato} : \t{valor}')

if __name__ == '__main__':
    os.system('cls')  # limpia la consola en Windows

    # Lista de frutas con su costo por kilo
    F = [['uva', 32], ['mango', 25], ['manzana', 35]]
    Dicresultados = {}
    pago = 0.0

    # Recorremos la lista
    for fruta, costo in F:
        p = float(input(f'Peso de la fruta {fruta} en kilos: '))
        texto = f'El costo de {fruta} (costo por kilo ${costo})'
        Dicresultados[texto] = round(p * costo, 2)
        pago += p * costo

    # Mostramos resultados
    pinta(Dicresultados)
    print(f'\nTotal a pagar: ${round(pago, 2)}')
