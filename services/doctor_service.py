import sqlite3
import os

# Buscamos la base de datos en la carpeta principal
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "clinica.db"))

def guardar_doctor(nombre, especialidad):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Asegúrate de que los nombres de las columnas coincidan con tu base de datos
    cursor.execute("INSERT INTO doctores (nombre, especialidad) VALUES (?, ?)", (nombre, especialidad))
    conn.commit() 
    conn.close()
    print("¡Doctor registrado con éxito!")