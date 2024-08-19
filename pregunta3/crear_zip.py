import zipfile

def crear_zip(nombre_archivo_imagen, nombre_archivo_zip):
    with zipfile.ZipFile(nombre_archivo_zip, 'w', zipfile.ZIP_DEFLATED) as archivo_zip:
        archivo_zip.write(nombre_archivo_imagen)
        print(f"Archivo ZIP creado: {nombre_archivo_zip}")

if __name__ == "__main__":
    nombre_archivo_imagen = "imagen_descargada.jpg"
    nombre_archivo_zip = "imagen_comprimida.zip"
    crear_zip(nombre_archivo_imagen, nombre_archivo_zip)
