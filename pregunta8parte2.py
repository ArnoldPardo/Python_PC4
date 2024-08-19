import csv
import sqlite3

def obtener_tipo_cambio(fecha):
    try:
        conn = sqlite3.connect('base1.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT venta FROM sunat_info WHERE fecha = ?', (fecha,))
        resultado = cursor.fetchone()
        
        conn.close()
        
        if resultado:
            return resultado[0]
        else:
            print(f"Tipo de cambio no encontrado para la fecha {fecha}.")
            return None
    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")
        return None

def procesar_ventas_csv(ruta_csv):
    productos = {}
    
    try:
        with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                fecha = row['fecha']
                producto = row['producto']
                precio_dolares = float(row['precio_dolares'])
                
                tipo_cambio = obtener_tipo_cambio(fecha)
                
                if tipo_cambio is not None:
                    precio_soles = precio_dolares * tipo_cambio
                else:
                    precio_soles = 0  # Maneja el caso donde no se encuentra el tipo de cambio
                
                if producto not in productos:
                    productos[producto] = {'total_dolares': 0.0, 'total_soles': 0.0}
                
                productos[producto]['total_dolares'] += precio_dolares
                productos[producto]['total_soles'] += precio_soles
        
        return productos
    except FileNotFoundError:
        print("El archivo CSV no se encuentra.")
        return {}
    except Exception as e:
        print(f"Error al procesar el archivo CSV: {e}")
        return {}

def mostrar_resultados(productos):
    if productos:
        for producto, totales in productos.items():
            print(f"Producto: {producto}")
            print(f"  Total en dólares: ${totales['total_dolares']:.2f}")
            print(f"  Total en soles: S/ {totales['total_soles']:.2f}")
            print()
    else:
        print("No se encontraron productos.")

def main():
    ruta_csv = 'ventas.csv'  # Asegúrate de que esta ruta es correcta
    productos = procesar_ventas_csv(ruta_csv)
    mostrar_resultados(productos)

if __name__ == "__main__":
    main()
