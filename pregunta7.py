import requests
import sqlite3
from pymongo import MongoClient
import json

# Paso 1: Obtener datos de la API de SUNAT

def obtener_precio_dolar():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    params = {
        "fecha_inicio": "2023-01-01",
        "fecha_fin": "2023-12-31"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Verifica si hubo algún error en la solicitud
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error al obtener datos: {e}")
        return None

# Paso 2: Almacenar en SQLite

def almacenar_en_sqlite(data):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    # Crear tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT PRIMARY KEY,
            compra REAL,
            venta REAL
        )
    ''')
    
    # Insertar datos
    for item in data:
        cursor.execute('''
            INSERT OR REPLACE INTO sunat_info (fecha, compra, venta)
            VALUES (?, ?, ?)
        ''', (item['fecha'], item['compra'], item['venta']))
    
    conn.commit()
    conn.close()

# Paso 3: Almacenar en MongoDB

def almacenar_en_mongodb(data):
    client = MongoClient('mongodb+srv://arnolmcgiberth0:Mcgiberth1@cluster0.pwaie.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['tipo_cambio']
    collection = db['sunat_info']
    
    # Limpiar colección antes de insertar datos
    collection.delete_many({})
    
    # Insertar datos
    collection.insert_many(data)
    
    client.close()

# Mostrar contenido de la tabla

def mostrar_contenido_sqlite():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM sunat_info')
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    conn.close()


