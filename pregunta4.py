import requests

# Descargar el archivo desde la URL proporcionada
def descargar_archivo(url, nombre_archivo):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza un error si la solicitud no fue exitosa
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)
        print(f"Archivo descargado y guardado como {nombre_archivo}")
    except requests.RequestException as e:
        print(f"Error al descargar el archivo: {e}")

# Procesar el archivo de temperaturas y calcular estadísticas
def procesar_temperaturas(nombre_archivo):
    temperaturas = []

    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',')
                if len(partes) == 2:
                    fecha, temp_str = partes
                    try:
                        temperatura = float(temp_str)
                        temperaturas.append(temperatura)
                    except ValueError:
                        print(f"Valor de temperatura no válido: {temp_str}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encuentra.")
        return None, None, None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None, None, None

    if not temperaturas:
        print("No se encontraron temperaturas válidas en el archivo.")
        return None, None, None

    # Calcular estadísticas
    temperatura_max = max(temperaturas)
    temperatura_min = min(temperaturas)
    temperatura_promedio = sum(temperaturas) / len(temperaturas)

    return temperatura_promedio, temperatura_max, temperatura_min

# Guardar los resultados en un nuevo archivo
def guardar_resultados(nombre_archivo, promedio, maximo, minimo):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(f"Temperatura Promedio: {promedio:.2f}\n")
            archivo.write(f"Temperatura Máxima: {maximo:.2f}\n")
            archivo.write(f"Temperatura Mínima: {minimo:.2f}\n")
        print(f"Resultados guardados en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    # URL del archivo de temperaturas
    url_fichero = "https://github.com/gdelgador/ProgramacionPython202407/raw/main/Modulo4/src/temperaturas.txt"
    nombre_archivo_descargado = "temperaturas.txt"
    nombre_archivo_salida = "resumen_temperaturas.txt"

    # Descargar el archivo
    descargar_archivo(url_fichero, nombre_archivo_descargado)

    # Procesar el archivo de temperaturas
    promedio, maximo, minimo = procesar_temperaturas(nombre_archivo_descargado)

    if promedio is not None:
        # Guardar resultados en el archivo de salida
        guardar_resultados(nombre_archivo_salida, promedio, maximo, minimo)
