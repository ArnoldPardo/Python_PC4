import zipfile

def descomprimir_zip(nombre_archivo_zip, ruta_extraer):
    with zipfile.ZipFile(nombre_archivo_zip, 'r') as archivo_zip:
        archivo_zip.extractall(ruta_extraer)
        print(f"Archivos extraídos en: {ruta_extraer}")

if __name__ == "__main__":
    nombre_archivo_zip = "imagen_comprimida.zip"
    ruta_extraer = "."  # Extraer en el directorio actual
    descomprimir_zip(nombre_archivo_zip, ruta_extraer)
