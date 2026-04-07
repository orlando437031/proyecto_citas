import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageSequence
from datetime import datetime

# ===============================
# BASE DE DATOS TEMPORAL
# ===============================

pacientes = []
doctores = []
citas = []

# ===============================
# PORTADA
# ===============================

class PortadaSoftware:
    def __init__(self, root):
        self.root = root
        self.root.title("MediControl Pro - Innovación Médica")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        try:
            self.gif = Image.open("imagen 2.webp")
            self.frames = [
                ImageTk.PhotoImage(img.resize((900, 600)))
                for img in ImageSequence.Iterator(self.gif)
            ]
        except:
            self.frames = None
            self.root.configure(bg="#001F3F")

        self.label_fondo = tk.Label(self.root)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.titulo = tk.Label(
            self.root,
            text="SISTEMA MÉDICO INTEGRAL",
            font=("Century Gothic", 32, "bold"),
            fg="#00E5FF",
            bg="#001F3F",
            pady=10,
        )
        self.titulo.place(relx=0.5, rely=0.2, anchor="center")

        self.style = ttk.Style()
        self.style.theme_use("default")

        self.progreso = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=400,
            mode="determinate",
        )
        self.progreso.place(relx=0.5, rely=0.7, anchor="center")

        self.lbl_carga = tk.Label(
            self.root,
            text="Iniciando módulos...",
            font=("Arial", 10),
            fg="white",
            bg="#001F3F",
        )
        self.lbl_carga.place(relx=0.5, rely=0.75, anchor="center")

        self.btn_entrar = tk.Button(
            self.root,
            text="INGRESAR AHORA",
            command=self.acceder,
            font=("Helvetica", 14, "bold"),
            bg="#00E5FF",
            fg="#001F3F",
            padx=30,
            pady=10,
            cursor="hand2",
            bd=0,
        )

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
            self.progreso["value"] = n
            self.root.after(30, self.simular_carga, n + 1)
        else:
            self.lbl_carga.config(text="¡Sistema Listo!")
            self.btn_entrar.place(relx=0.5, rely=0.85, anchor="center")

    def acceder(self):
        self.root.destroy()
        iniciar_sistema()


# ===============================
# FUNCIONES PACIENTES
# ===============================

def registrar_paciente():

    ventana = tk.Toplevel()
    ventana.title("Registrar Paciente")
    ventana.geometry("300x200")

    tk.Label(ventana, text="Nombre del Paciente").pack(pady=10)

    entrada = tk.Entry(ventana)
    entrada.pack()

    def guardar():
        nombre = entrada.get()

        if nombre == "":
            messagebox.showerror("Error", "Debe escribir un nombre")
            return

        pacientes.append(nombre)

        messagebox.showinfo("Éxito", "Paciente registrado")

        entrada.delete(0, tk.END)

    tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)


def ver_pacientes():

    ventana = tk.Toplevel()
    ventana.title("Pacientes")
    ventana.geometry("300x300")

    tk.Label(
        ventana,
        text="Pacientes Registrados",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    if len(pacientes) == 0:
        tk.Label(ventana, text="No hay pacientes").pack()

    for p in pacientes:
        tk.Label(ventana, text=p).pack()


# ===============================
# FUNCIONES DOCTORES
# ===============================

def registrar_doctor():

    ventana = tk.Toplevel()
    ventana.title("Registrar Doctor")
    ventana.geometry("300x200")

    tk.Label(ventana, text="Nombre del Doctor").pack(pady=10)

    entrada = tk.Entry(ventana)
    entrada.pack()

    def guardar():
        nombre = entrada.get()

        if nombre == "":
            messagebox.showerror("Error", "Debe escribir un nombre")
            return

        doctores.append(nombre)

        messagebox.showinfo("Éxito", "Doctor registrado")

        entrada.delete(0, tk.END)

    tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)


# ===============================
# FUNCIONES CITAS
# ===============================

def crear_cita():

    ventana = tk.Toplevel()
    ventana.title("Crear Cita")
    ventana.geometry("350x250")

    tk.Label(ventana, text="Paciente").pack()
    paciente_entry = tk.Entry(ventana)
    paciente_entry.pack()

    tk.Label(ventana, text="Doctor").pack()
    doctor_entry = tk.Entry(ventana)
    doctor_entry.pack()

    tk.Label(ventana, text="Fecha (YYYY-MM-DD)").pack()
    fecha_entry = tk.Entry(ventana)
    fecha_entry.pack()

    def guardar():

        paciente = paciente_entry.get()
        doctor = doctor_entry.get()
        fecha = fecha_entry.get()

        if paciente == "" or doctor == "" or fecha == "":
            messagebox.showerror("Error", "Debe completar todos los campos")
            return

        cita = {
            "paciente": paciente,
            "doctor": doctor,
            "fecha": fecha
        }

        citas.append(cita)

        messagebox.showinfo("Éxito", "Cita creada")

        ventana.destroy()

    tk.Button(ventana, text="Guardar Cita", command=guardar).pack(pady=10)


def ver_citas_hoy():

    ventana = tk.Toplevel()
    ventana.title("Citas de Hoy")
    ventana.geometry("350x300")

    hoy = datetime.now().strftime("%Y-%m-%d")

    tk.Label(
        ventana,
        text="Citas del Día",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    hay = False

    for c in citas:
        if c["fecha"] == hoy:
            texto = f"{c['paciente']} con Dr. {c['doctor']}"
            tk.Label(ventana, text=texto).pack()
            hay = True

    if not hay:
        tk.Label(ventana, text="No hay citas hoy").pack()


# ===============================
# MENÚ PRINCIPAL
# ===============================

def iniciar_sistema():
    ventana = tk.Tk()
    ventana.title("Sistema Médico")
    ventana.geometry("500x450")

    titulo = tk.Label(
        ventana,
        text="Sistema de Gestión Médica",
        font=("Arial", 18, "bold")
    )
    titulo.pack(pady=20)

    tk.Button(
        ventana,
        text="Registrar Paciente",
        width=25,
        height=2,
        command=registrar_paciente
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Ver Pacientes",
        width=25,
        height=2,
        command=ver_pacientes
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Registrar Doctor",
        width=25,
        height=2,
        command=registrar_doctor
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Crear Cita",
        width=25,
        height=2,
        command=crear_cita
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Ver Citas del Día",
        width=25,
        height=2,
        command=ver_citas_hoy
    ).pack(pady=10)

    ventana.mainloop()


# ===============================
# INICIO DEL PROGRAMA
# ===============================

if __name__ == "__main__":
    root = tk.Tk()
    app = PortadaSoftware(root)
    root.mainloop()