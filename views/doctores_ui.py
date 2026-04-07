import tkinter as tk
from tkinter import messagebox
import sqlite3


import sqlite3

def registrar_doctor_db(nombre, especialidad):
    try:
        # Importante: Asegúrate de que la ruta sea correcta
        conn = sqlite3.connect('clinica.db') 
        cursor = conn.cursor()
        cursor.execute("INSERT INTO doctores (nombre, especialidad) VALUES (?, ?)", (nombre, especialidad))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False













def guardar_doctor():
    # Obtener datos de los campos
    nombre = entry_nombre.get()
    especialidad = entry_especialidad.get()
    
    if nombre == "" or especialidad == "":
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    try:
        conexion = sqlite3.connect('clinica.db')
        cursor = conexion.cursor()
        
        # Insertar en la tabla doctores
        cursor.execute("INSERT INTO doctores (nombre, especialidad) VALUES (?, ?)", 
                       (nombre, especialidad))
        
        conexion.commit()
        conexion.close()
        
        messagebox.showinfo("Éxito", f"Doctor {nombre} registrado correctamente")
        
        # Limpiar campos
        entry_nombre.delete(0, tk.END)
        entry_especialidad.delete(0, tk.END)
        
    except Exception as e:
        messagebox.showerror("Error", f"Error en BD: {e}")

# --- DISEÑO DE LA VENTANA (Para que no de error 'not defined') ---
ventana = tk.Tk()
ventana.title("Registro de Doctores")

tk.Label(ventana, text="Nombre del Doctor:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Especialidad:").pack()
entry_especialidad = tk.Entry(ventana)
entry_especialidad.pack()

# VINCULAR EL BOTÓN
btn_registrar = tk.Button(ventana, text="Guardar", command=guardar_doctor)
btn_registrar.pack(pady=10)

ventana.mainloop()