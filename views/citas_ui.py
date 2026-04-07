import sqlite3

def guardar_cita(paciente, doctor, hora, es_urgencia):
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    
    # 1 representa urgencia, 0 cita normal
    valor_urgencia = 1 if es_urgencia else 0
    
    cursor.execute("INSERT INTO citas (paciente, doctor, hora, urgencia) VALUES (?, ?, ?, ?)", 
                   (paciente, doctor, hora, valor_urgencia))
    
    conn.commit()
    conn.close()