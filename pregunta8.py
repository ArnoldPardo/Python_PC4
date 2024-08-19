import sqlite3

def crear_base_datos():
    conn = sqlite3.connect('base1.db')
    cursor = conn.cursor()

    # Crear la tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT PRIMARY KEY,
            compra REAL,
            venta REAL
        )
    ''')

    # Insertar datos de ejemplo (solo si la tabla está vacía)
    cursor.execute('''
        INSERT OR IGNORE INTO sunat_info (fecha, compra, venta)
        VALUES 
        ('2023-01-01', 3.80, 3.82),
        ('2023-01-02', 3.81, 3.83)
        -- Añade más datos aquí si es necesario
    ''')

    conn.commit()
    conn.close()

# Ejecutar la creación de la base de datos (solo una vez)
crear_base_datos()

