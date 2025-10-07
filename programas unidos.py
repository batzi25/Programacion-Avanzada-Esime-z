from os import system

# Definimos algunos conjuntos de ejemplo
s1 = {12, 22, 32}
s2 = {1, 2, 3, 4, 5}
s3 = {22, 32}   # subconjunto de s1
s4 = {100, 200} # disjunto de s1

# Función que muestra el menú
def mostrar_menu():
    print("\nMenú de Conjuntos:")
    print("0. Salir")
    print("1. difference")
    print("2. difference_update")
    print("3. isdisjoint")
    print("4. issubset")
    print("5. symmetric_difference")

# Función principal
def main():
    while True:
        system('cls')  # limpia pantalla en Windows (en Linux/Mac usa 'clear')
        
        # Mostramos conjuntos para referencia
        print(f"tus conjuntos son:")
        print(f"s1 = {s1}")
        print(f"s2 = {s2}")
        print(f"s3 = {s3}")
        print(f"s4 = {s4}")
        
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        match opcion:
            case '0':
                print("Saliendo del programa...")
                break

            case '1':
                # difference
                print(f"\nDiferencia s1 - s2 = {s1.difference(s2)}")

            case '2':
                # difference_update (sin modificar el original)
                temp = s1.copy()
                temp.difference_update(s2)
                print(f"\ns1 después de difference_update con s2 = {temp}")

            case '3':
                # isdisjoint
                print(f"\n¿s1 y s4 son disjuntos? {s1.isdisjoint(s4)}")
                print(f"¿s1 y s2 son disjuntos? {s1.isdisjoint(s2)}")

            case '4':
                # issubset
                print(f"\n¿s3 es subconjunto de s1? {s3.issubset(s1)}")
                print(f"¿s2 es subconjunto de s1? {s2.issubset(s1)}")

            case '5':
                # symmetric_difference
                print(f"\nDiferencia simétrica s1 Δ s2 = {s1.symmetric_difference(s2)}")

            case _:
                print("Opción no válida, intenta de nuevo.")

        input("\nPresiona Enter para continuar...")

# Punto de entrada
if __name__ == '__main__':
    main()
