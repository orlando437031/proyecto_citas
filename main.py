import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageSequence
import sqlite3

class MediControlPro:
    def __init__(self, root):
        self.root = root
        self.root.title("MediControl Pro v3.0 - Sistema Médico Integral")
        self.root.geometry("1100x700")
        self.root.configure(bg="#0a192f") # Fondo Azul Oscuro Navy
        
        # Base de Datos (Conexión inicial)
        self.conn = sqlite3.connect("clinica.db")
        self.crear_tablas_iniciales()

        # --- 1. PANTALLA DE CARGA (SPLASH) ---
        self.mostrar_pantalla_carga()

    def crear_tablas_iniciales(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS doctores 
                       (id INTEGER PRIMARY KEY, nombre TEXT, especialidad TEXT, tel TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes 
                       (id INTEGER PRIMARY KEY, nombre TEXT, edad TEXT, tel TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS citas 
                       (id INTEGER PRIMARY KEY, fecha TEXT, doctor TEXT, paciente TEXT)''')
        self.conn.commit()

    def mostrar_pantalla_carga(self):
        # Fondo
        try:
            self.img_fondo = Image.open("imagen 2.webp").resize((1100, 700))
            self.bg_render = ImageTk.PhotoImage(self.img_fondo)
            self.lbl_bg = tk.Label(self.root, image=self.bg_render)
            self.lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            tk.Label(self.root, bg="#0a192f").place(x=0, y=0, relwidth=1, relheight=1)

        # Capa de texto
        self.txt_splash = tk.Label(self.root, text="MEDICONTROL PRO", font=("Century Gothic", 40, "bold"), 
                                   fg="#00e5ff", bg="#0a192f")
        self.txt_splash.place(relx=0.5, rely=0.4, anchor="center")

        # Barra de progreso
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("Cyan.Horizontal.TProgressbar", thickness=15, troughcolor='#0a192f', background='#00e5ff')
        
        self.bar = ttk.Progressbar(self.root, length=500, mode="determinate", style="Cyan.Horizontal.TProgressbar")
        self.bar.place(relx=0.5, rely=0.6, anchor="center")
        
        self.lbl_status = tk.Label(self.root, text="Cargando base de datos...", font=("Arial", 10), fg="white", bg="#0a192f")
        self.lbl_status.place(relx=0.5, rely=0.65, anchor="center")

        self.animar_carga(0)

    def animar_carga(self, n):
        if n <= 100:
            self.bar['value'] = n
            # Mensajes dinámicos de carga
            if n == 30: self.lbl_status.config(text="Cargando módulos de interfaz...")
            if n == 60: self.lbl_status.config(text="Sincronizando expedientes...")
            if n == 90: self.lbl_status.config(text="Sistema Listo.")
            self.root.after(30, self.animar_carga, n + 1)
        else:
            self.mostrar_login_final()

    def mostrar_login_final(self):
        # Botón para entrar al Dashboard
        self.btn_entrar = tk.Button(self.root, text="INGRESAR AL PANEL", font=("Helvetica", 14, "bold"), 
                                    bg="#00e5ff", fg="#0a192f", bd=0, padx=40, pady=15, 
                                    cursor="hand2", command=self.cargar_dashboard)
        self.btn_entrar.place(relx=0.5, rely=0.75, anchor="center")

    # --- 2. DASHBOARD PRINCIPAL ---
    def cargar_dashboard(self):
        # Limpiar pantalla de carga
        for widget in self.root.winfo_children():
            widget.destroy()

        # BARRA LATERAL
        self.sidebar = tk.Frame(self.root, bg="#112240", width=250)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="🏥 MENU", font=("Arial", 20, "bold"), bg="#112240", fg="#00e5ff", pady=30).pack()

        def crear_btn_nav(texto, emoji, cmd):
            return tk.Button(self.sidebar, text=f"{emoji} {texto}", font=("Segoe UI", 12),
                             bg="#112240", fg="white", relief="flat", anchor="w", padx=25,
                             activebackground="#1d2d50", activeforeground="#00e5ff",
                             cursor="hand2", command=cmd).pack(fill="x", pady=5)

        crear_btn_nav("DOCTORES", "👨‍⚕️", self.ventana_doctores)
        crear_btn_nav("PACIENTES", "👥", self.ventana_pacientes)
        crear_btn_nav("CITAS", "📅", self.ventana_citas)
        
        tk.Button(self.sidebar, text="🚪 CERRAR SESIÓN", bg="#112240", fg="#ff5555", relief="flat", 
                  command=self.root.quit).pack(side="bottom", fill="x", pady=20)

        # ÁREA CENTRAL
        self.main_frame = tk.Frame(self.root, bg="#0a192f")
        self.main_area_init()

    def main_area_init(self):
        self.main_frame.pack(side="right", expand=True, fill="both")
        tk.Label(self.main_frame, text="BIENVENIDO A MEDICONTROL PRO", font=("Century Gothic", 25, "bold"), 
                 bg="#0a192f", fg="white").pack(pady=50)
        
        # Tarjetas de estado rápidas
        card_frame = tk.Frame(self.main_frame, bg="#0a192f")
        card_frame.pack(pady=20)

        self.crear_card(card_frame, "CITAS HOY", "12", "#00e5ff")
        self.crear_card(card_frame, "URGENCIAS", "3", "#ff5555")

    def crear_card(self, parent, titulo, valor, color):
        f = tk.Frame(parent, bg="#112240", padx=30, pady=20, highlightthickness=1, highlightbackground=color)
        f.pack(side="left", padx=20)
        tk.Label(f, text=titulo, bg="#112240", fg="#8892b0").pack()
        tk.Label(f, text=valor, font=("Arial", 24, "bold"), bg="#112240", fg="white").pack()

    # --- 3. MÓDULOS (VENTANAS) ---
    def ventana_doctores(self):
        top = tk.Toplevel(self.root)
        top.title("Gestión de Doctores")
        top.geometry("600x400")
        top.configure(bg="#112240")
        tk.Label(top, text="REGISTRO DE DOCTORES", font=("Arial", 18, "bold"), bg="#112240", fg="#00e5ff").pack(pady=20)
        # Aquí va tu código de ModuloDoctores anterior...
        tk.Label(top, text="Módulo en funcionamiento...", bg="#112240", fg="white").pack()

    def ventana_pacientes(self):
        top = tk.Toplevel(self.root)
        top.title("Gestión de Pacientes")
        top.geometry("600x400")
        top.configure(bg="#112240")
        tk.Label(top, text="GESTIÓN DE PACIENTES", font=("Arial", 18, "bold"), bg="#112240", fg="#00e5ff").pack(pady=20)
        tk.Button(top, text="Registrar Nuevo", bg="#00e5ff", fg="#0a192f").pack(pady=10)

    def ventana_citas(self):
        top = tk.Toplevel(self.root)
        top.title("Calendario de Citas")
        top.geometry("700x500")
        top.configure(bg="#0a192f")
        tk.Label(top, text="AGENDA MÉDICA", font=("Arial", 18, "bold"), bg="#0a192f", fg="#00e5ff").pack(pady=20)
        # Ejemplo de tabla rápida
        tabla = ttk.Treeview(top, columns=("Hora", "Paciente"), show="headings")
        tabla.heading("Hora", text="HORA")
        tabla.heading("Paciente", text="PACIENTE")
        tabla.pack(fill="both", expand=True, padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = MediControlPro(root)
    root.mainloop()

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
    
