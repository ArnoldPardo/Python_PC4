import os

def guardar_tabla_multiplicar(n):
    """Genera y guarda la tabla de multiplicar del número n en un archivo."""
    nombre_archivo = f"tabla-{n}.txt"
    with open(nombre_archivo, 'w') as archivo:
        for i in range(1, 11):
            archivo.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en {nombre_archivo}")

def mostrar_tabla_multiplicar(n):
    """Lee y muestra la tabla de multiplicar del número n desde el archivo."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(f"Tabla de multiplicar del {n}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

def mostrar_linea_tabla(n, m):
    """Lee el archivo de la tabla de multiplicar del número n y muestra la línea m."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= len(lineas):
                print(f"Línea {m} de la tabla de multiplicar del {n}: {lineas[m-1].strip()}")
            else:
                print(f"La línea {m} no está en el archivo.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

def menu():
    """Muestra el menú y ejecuta las opciones seleccionadas por el usuario."""
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea específica de la tabla")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                guardar_tabla_multiplicar(n)
            else:
                print("Número fuera de rango. Debe estar entre 1 y 10.")
        
        elif opcion == '2':
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                mostrar_tabla_multiplicar(n)
            else:
                print("Número fuera de rango. Debe estar entre 1 y 10.")
        
        elif opcion == '3':
            n = int(input("Introduce el número de la tabla (entre 1 y 10): "))
            m = int(input("Introduce la línea que quieres mostrar (entre 1 y 10): "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                mostrar_linea_tabla(n, m)
            else:
                print("Número fuera de rango. Debe estar entre 1 y 10.")
        
        elif opcion == '4':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

if __name__ == "__main__":
    menu()
