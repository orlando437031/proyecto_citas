import tkinter as tk
from tkinter import ttk, messagebox

class VentanaDoctores:
    def _init_(self, root):
        self.root = root
        self.root.title("Registro de Doctores")
        self.root.geometry("400x400")
        self.root.config(bg="#e3f2fd") # Un azul claro médico

        tk.Label(self.root, text="REGISTRO DE DOCTORES", font=("Arial", 14, "bold"), bg="#e3f2fd").pack(pady=20)

        # Campos de entrada
        tk.Label(self.root, text="Nombre del Doctor:", bg="#e3f2fd").pack()
        self.ent_nombre = tk.Entry(self.root, width=30)
        self.ent_nombre.pack(pady=5)

        tk.Label(self.root, text="Especialidad:", bg="#e3f2fd").pack()
        self.ent_especialidad = tk.Entry(self.root, width=30)
        self.ent_especialidad.pack(pady=5)

        # Botón para guardar
        tk.Button(self.root, text="Guardar Doctor", command=self.guardar, bg="#4caf50", fg="white").pack(pady=20)

    def guardar(self):
        nombre = self.ent_nombre.get()
        especialidad = self.ent_especialidad.get()
        if nombre and especialidad:
            messagebox.showinfo("Éxito", f"Doctor {nombre} registrado correctamente.")
            self.root.destroy() # Cierra la ventana al terminar
        else:
            messagebox.showwarning("Error", "Por favor llena todos los campos.")

class VentanaPacientes:
    def _init_(self, root):
        self.root = root
        self.root.title("Registro de Pacientes")
        self.root.geometry("400x400")
        self.root.config(bg="#f1f8e9") # Un verde claro médico

        tk.Label(self.root, text="REGISTRO DE PACIENTES", font=("Arial", 14, "bold"), bg="#f1f8e9").pack(pady=20)
        
        # Aquí puedes añadir campos similares para pacientes (Nombre, Edad, etc.)
        tk.Label(self.root, text="Nombre del Paciente:", bg="#f1f8e9").pack()
        self.ent_paciente = tk.Entry(self.root, width=30)
        self.ent_paciente.pack(pady=5)
        
        tk.Button(self.root, text="Guardar Paciente", command=lambda: messagebox.showinfo("Éxito", "Paciente guardado"), bg="#4caf50", fg="white").pack(pady=20)
