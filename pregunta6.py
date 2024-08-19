import os

def contar_lineas_codigo(ruta_archivo):
    """Cuenta las líneas de código en un archivo .py, excluyendo comentarios y líneas en blanco."""
    # Verificar que el archivo tenga la extensión .py
    if not ruta_archivo.endswith('.py'):
        print("El archivo no tiene una extensión .py")
        return
    
    # Verificar si el archivo existe
    if not os.path.isfile(ruta_archivo):
        print("Ruta inválida o el archivo no existe.")
        return
    
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            count = 0
            for linea in lineas:
                linea = linea.strip()
                if linea and not linea.startswith('#'):
                    count += 1
            print(f"Número de líneas de código en {ruta_archivo}: {count}")
    except FileNotFoundError:
        print("El archivo no se encuentra.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def main():
    """Solicita la ruta del archivo al usuario y cuenta las líneas de código."""
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()
