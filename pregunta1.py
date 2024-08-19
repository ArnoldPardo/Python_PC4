import requests

def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza un error si la solicitud no fue exitosa
        datos = respuesta.json()
        precio_usd = datos['bpi']['USD']['rate'].replace(',', '')  # Eliminamos la coma del precio para convertir a float
        return float(precio_usd)
    except requests.RequestException as e:
        print(f"Error al consultar la API: {e}")
        return None

def calcular_costo_total(bitcoins, precio_bitcoin):
    return bitcoins * precio_bitcoin

def main():
    try:
        n = float(input("Ingrese la cantidad de bitcoins que posee: "))
        if n < 0:
            raise ValueError("La cantidad de bitcoins no puede ser negativa.")
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return
    
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is None:
        return
    
    costo_total = calcular_costo_total(n, precio_bitcoin)
    print(f"El costo actual de {n} Bitcoins en USD es: ${costo_total:,.4f}")

if __name__ == "__main__":
    main()
