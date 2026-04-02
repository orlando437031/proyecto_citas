
import tkinter as tk
from PIL import Image, ImageTk
import os

class PortadaUI:
    def __init__(self, root, al_terminar):
        self.root = root
        self.al_terminar = al_terminar
        self.root.title("Bienvenido - Sistema de Citas")
        self.root.geometry("600x600") # La hice un poco más grande
        self.root.configure(bg="#f2a9ff")

        # --- CARGAR TU IMAGEN ---
        try:
            ruta_actual = os.path.dirname(__file__)
            
            # CAMBIA "mifoto.png" por el nombre exacto de tu archivo (ejemplo: "logo.jpg")
            nombre_archivo = "mifoto.png" 
            
            ruta_final = os.path.join(ruta_actual, nombre_archivo)
            
            img_original = Image.open(ruta_final)
            # Aquí ajustas el tamaño (Ancho, Alto)
            img_redimensionada = img_original.resize((350, 350)) 
            self.foto = ImageTk.PhotoImage(img_redimensionada)
            
            self.lbl_img = tk.Label(self.root, image=self.foto, bg="#f2a9ff")
            self.lbl_img.pack(pady=20)
            
        except Exception as e:
            print(f"Error: No encontré la imagen '{nombre_archivo}'. Revisa el nombre.")
            tk.Label(self.root, text=f"[Falta el archivo {nombre_archivo}]", bg="#f2a9ff", fg="red").pack()

        # Título y Botón
        tk.Label(self.root, text="SISTEMA MÉDICO", font=("Arial", 22, "bold"), 
                 bg="#f2a9ff", fg="#1f2933").pack(pady=10)
        
        self.btn = tk.Button(self.root, text="COMENZAR", command=self.entrar,
                            bg="#8b82f6", fg="white", font=("Arial", 14, "bold"),
                            width=18, height=2, cursor="hand2")
        self.btn.pack(pady=20)

    def entrar(self):
        self.root.destroy()
        self.al_terminar()

if __name__ == "__main__":
    root = tk.Tk()
    app = PortadaUI(root, lambda: print("Iniciando..."))
    root.mainloop()
    
    