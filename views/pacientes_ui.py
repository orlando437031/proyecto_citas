import tkinter as tk
from tkinter import messagebox
import sqlite3

def guardar_paciente():
    # 1. Obtenemos los datos de los cuadros de texto
    nombre = entry_nombre_paciente.get()
    edad = entry_edad.get()
    historial = entry_historial.get()

    # 2. Validamos que no estén vacíos
    if nombre == "" or edad == "":
        messagebox.showwarning("Error", "Nombre y edad son obligatorios")
        return

    try:
        # 3. Conexión a la base de datos
        conexion = sqlite3.connect('clinica.db')
        cursor = conexion.cursor()
        
        # 4. Insertar datos (asegúrate que la tabla se llame 'pacientes')
        cursor.execute("INSERT INTO pacientes (nombre, edad, historial) VALUES (?, ?, ?)", 
                       (nombre, edad, historial))
        
        conexion.commit()
        conexion.close()
        
        messagebox.showinfo("Éxito", "Paciente registrado con éxito")
        
        # 5. Limpiar los campos después de registrar
        entry_nombre_paciente.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_historial.delete(0, tk.END)
        
    except Exception as e:
        messagebox.showerror("Error", f"Error en BD: {e}")

# --- AQUÍ DEBE ESTAR LA CONFIGURACIÓN DE TU VENTANA ---
ventana = tk.Tk()
ventana.title("Registro de Pacientes")

# IMPORTANTE: Los nombres de estas variables deben coincidir con los de la función arriba
tk.Label(ventana, text="Nombre del Paciente:").pack()
entry_nombre_paciente = tk.Entry(ventana)
entry_nombre_paciente.pack()

tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Historial Clínico:").pack()
entry_historial = tk.Entry(ventana)
entry_historial.pack()

# EL BOTÓN (Ya vinculado a la función)
btn_registrar = tk.Button(ventana, text="Registrar", command=guardar_paciente)
btn_registrar.pack(pady=10)

ventana.mainloop()