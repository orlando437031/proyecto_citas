import tkinter as tk
from tkinter import messagebox
import sqlite3

def guardar_datos():
    # 1. Obtener datos de los cuadros de texto
    paciente = entry_paciente.get()
    doctor = entry_doctor.get()
    hora = entry_hora.get()
    es_urgencia = var_urgencia.get() # 1 si está marcado, 0 si no

    if paciente == "" or doctor == "" or hora == "":
        messagebox.showwarning("Atención", "Por favor, llena todos los campos")
        return

    # 2. Conectar y guardar en clinica.db
    try:
        conexion = sqlite3.connect('clinica.db')
        cursor = conexion.cursor()
        
        # Insertar los datos en la tabla (asegúrate de que las columnas coincidan)
        cursor.execute("INSERT INTO citas (paciente, doctor, hora, urgencia) VALUES (?, ?, ?, ?)", 
                       (paciente, doctor, hora, es_urgencia))
        
        conexion.commit()
        conexion.close()
        
        messagebox.showinfo("Éxito", f"Cita registrada para {paciente}")
        
        # Limpiar campos después de guardar
        entry_paciente.delete(0, tk.END)
        entry_doctor.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        var_urgencia.set(0)
        
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")

# --- Configuración de la Ventana Visual ---
ventana = tk.Tk()
ventana.title("Registro de Citas - MediControl")
ventana.geometry("400x450")
ventana.config(bg="#1e1e1e") # Color oscuro como tu VS Code

# Título
tk.Label(ventana, text="NUEVO REGISTRO", fg="white", bg="#1e1e1e", font=("Arial", 14, "bold")).pack(pady=20)

# Campos de entrada
tk.Label(ventana, text="Nombre del Paciente:", fg="white", bg="#1e1e1e").pack()
entry_paciente = tk.Entry(ventana, width=30)
entry_paciente.pack(pady=5)

tk.Label(ventana, text="Nombre del Doctor:", fg="white", bg="#1e1e1e").pack()
entry_doctor = tk.Entry(ventana, width=30)
entry_doctor.pack(pady=5)

tk.Label(ventana, text="Hora (Ej: 14:30):", fg="white", bg="#1e1e1e").pack()
entry_hora = tk.Entry(ventana, width=30)
entry_hora.pack(pady=5)

# Checkbox para Urgencia
var_urgencia = tk.IntVar()
tk.Checkbutton(ventana, text="¿Es una Urgencia?", variable=var_urgencia, 
               bg="#1e1e1e", fg="white", selectcolor="#333333").pack(pady=15)

# Botón Guardar (Azul como tu interfaz)
btn_guardar = tk.Button(ventana, text="REGISTRAR CITA", command=guardar_datos, 
                        bg="#007acc", fg="white", font=("Arial", 10, "bold"), width=20)
btn_guardar.pack(pady=20)

ventana.mainloop()