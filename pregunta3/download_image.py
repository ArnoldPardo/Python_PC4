import requests

def descargar_imagen(url, nombre_archivo):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza un error si la solicitud no fue exitosa
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)
        print(f"Imagen descargada y guardada como {nombre_archivo}")
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")

if __name__ == "__main__":
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    nombre_archivo = "imagen_descargada.jpg"
    descargar_imagen(url_imagen, nombre_archivo)
