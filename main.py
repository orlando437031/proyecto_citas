import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence

class PortadaSoftware:
    def __init__(self, root): # <--- Asegúrate de que sean DOS guiones bajos
        self.root = root
        self.root.title("MediControl Pro - Innovación Médica")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        # 1. CARGA DEL FONDO (GIF o Imagen)
        try:
            # Intentamos cargar un GIF animado para el efecto "video"
            self.gif = Image.open("imagen 2.webp") # Puedes usar .gif o .webp animado
            self.frames = [ImageTk.PhotoImage(img.resize((900, 600))) 
                           for img in ImageSequence.Iterator(self.gif)]
        except:
            self.frames = None
            self.root.configure(bg="#001F3F") # Azul oscuro profundo si falla

        self.label_fondo = tk.Label(self.root)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # 2. CAPA DE DISEÑO (Colores y Títulos)
        self.titulo = tk.Label(self.root, text="SISTEMA MÉDICO INTEGRAL", 
                               font=("Century Gothic", 32, "bold"), 
                               fg="#00E5FF", bg="#001F3F", pady=10)
        self.titulo.place(relx=0.5, rely=0.2, anchor="center")

        # 3. BARRA DE CARGA (Para que se vea más profesional)
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("TProgressbar", thickness=10, troughcolor='#001F3F', background='#00E5FF')
        
        self.progreso = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate", style="TProgressbar")
        self.progreso.place(relx=0.5, rely=0.7, anchor="center")
        
        self.lbl_carga = tk.Label(self.root, text="Iniciando módulos...", font=("Arial", 10), fg="white", bg="#001F3F")
        self.lbl_carga.place(relx=0.5, rely=0.75, anchor="center")

        # 4. BOTÓN DE ENTRADA (Oculto al inicio)
        self.btn_entrar = tk.Button(self.root, text="INGRESAR AHORA", 
                                    command=self.acceder,
                                    font=("Helvetica", 14, "bold"), 
                                    bg="#00E5FF", fg="#001F3F", 
                                    padx=30, pady=10, cursor="hand2", bd=0)

        # Iniciar procesos
        if self.frames:
            self.animar_fondo(0)
        self.simular_carga(0)

    def animar_fondo(self, contador):
        frame = self.frames[contador]
        self.label_fondo.config(image=frame)
        contador = (contador + 1) % len(self.frames)
        self.root.after(50, self.animar_fondo, contador)

    def simular_carga(self, n):
        if n <= 100:
            self.progreso['value'] = n
            self.root.after(30, self.simular_carga, n + 1)
        else:
            self.lbl_carga.config(text="¡Sistema Listo!")
            self.btn_entrar.place(relx=0.5, rely=0.85, anchor="center")

    def acceder(self):
        print("Acceso concedido")
        # self.root.destroy() # Aquí abres tu otra ventana

if __name__ == "__main__":
    root = tk.Tk()
    app = PortadaSoftware(root) # <--- Aquí ya no te dará error
    root.mainloop()
    
