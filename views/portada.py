import tkinter as tk
from PIL import Image, ImageTk
# Importamos las ventanas vecinas (están en la misma carpeta views)
from doctores_ui import VentanaDoctores
from pacientes_ui import VentanaPacientes
from citas_ui import VentanaCitas 

class Portada:
    def _init_(self, root):
        self.root = root
        self.root.title("Sistema Médico - Menu")
        self.root.geometry("400x550")
        self.root.config(bg="#f0f0f0")

        # --- TÍTULO ---
        self.label = tk.Label(self.root, text="MENÚ PRINCIPAL", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.label.pack(pady=30)

        # --- BOTONES ---
        # Estilo común para botones
        estilo_btn = {"width": 20, "height": 2, "font": ("Arial", 10, "bold"), "fg": "white"}

        # Botón Doctores
        self.btn_doctores = tk.Button(self.root, text="DOCTORES", bg="#4CAF50", 
                                      command=self.abrir_doctores, **estilo_btn)
        self.btn_doctores.pack(pady=10)

        # Botón Pacientes
        self.btn_pacientes = tk.Button(self.root, text="PACIENTES", bg="#2196F3", 
                                       command=self.abrir_pacientes, **estilo_btn)
        self.btn_pacientes.pack(pady=10)

        # Botón Citas
        self.btn_citas = tk.Button(self.root, text="CITAS", bg="#FF9800", 
                                   command=self.abrir_citas, **estilo_btn)
        self.btn_citas.pack(pady=10)

    # --- FUNCIONES PARA ABRIR LAS VENTANAS ---
    def abrir_doctores(self):
        nueva_ventana = tk.Toplevel(self.root)
        VentanaDoctores(nueva_ventana)

    def abrir_pacientes(self):
        nueva_ventana = tk.Toplevel(self.root)
        VentanaPacientes(nueva_ventana)

    def abrir_citas(self):
        nueva_ventana = tk.Toplevel(self.root)
        VentanaCitas(nueva_ventana)

# Para ejecutar esta pantalla sola si quieres probarla
if __name__ == "__main__":
    root = tk.Tk()
    app = Portada(root)
    root.mainloop()