import sqlite3

def preparar_sistema():
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    
    # Tabla Doctores
    cursor.execute('''CREATE TABLE IF NOT EXISTS doctores 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, especialidad TEXT)''')
    
    # Tabla Pacientes
    cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, edad INTEGER, telefono TEXT)''')
    
    conn.commit()
    conn.close()
    print("✅ Tablas de Doctores y Pacientes listas.")

preparar_sistema()