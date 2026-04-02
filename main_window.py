import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class ModuloDoctores:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.title("Gestión de Doctores")
        self.ventana.geometry("1000x650")
        self.ventana.configure(bg='#0f172a')
        self.ventana.resizable(True, True)

        # Base de datos
        self.conexion = sqlite3.connect('clinica.db')
        self.crear_tabla()

        # Datos
        self.especialidades = ["Cardiología", "Pediatría", "Dermatología", "Neurología"]
        self.horarios = ["08:00 - 12:00", "12:00 - 16:00", "16:00 - 20:00"]

        self.crear_estilos()
        self.crear_widgets()
        self.cargar_doctores()

    def crear_tabla(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS doctores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                apellido TEXT,
                especialidad TEXT,
                telefono TEXT,
                horario TEXT
            )
        ''')
        self.conexion.commit()

    # 🎨 ESTILOS MODERNOS
    def crear_estilos(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
                        background="#1f2937",
                        foreground="white",
                        fieldbackground="#1f2937",
                        rowheight=28)

        style.map("Treeview",
                  background=[("selected", "#2563eb")])

    def crear_widgets(self):

        # 🔷 NAVBAR
        navbar = tk.Frame(self.ventana, bg="#020617", height=50)
        navbar.pack(fill="x")

        def crear_boton(texto, comando):
            return tk.Button(navbar, text=texto,
                             font=("Segoe UI", 11, "bold"),
                             bg="#2563eb", fg="white",
                             activebackground="#1e40af",
                             bd=0, padx=15, pady=5,
                             cursor="hand2",
                             command=comando)

        crear_boton("Inicio", self.ir_inicio).pack(side="left", padx=10, pady=10)
        crear_boton("Doctores", lambda: None).pack(side="left", padx=10)
        crear_boton("Salir", self.cerrar).pack(side="right", padx=10)

        # 📦 CONTENEDOR
        container = tk.Frame(self.ventana, bg="#0f172a")
        container.pack(fill="both", expand=True, padx=15, pady=15)

        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # 🧾 FORMULARIO
        form = tk.Frame(container, bg="#111827")
        form.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        def crear_label(texto, row, col):
            tk.Label(form, text=texto,
                     bg="#111827", fg="white",
                     font=("Segoe UI", 10, "bold")
                     ).grid(row=row, column=col, padx=10, pady=10, sticky="w")

        def crear_entry(row, col):
            entry = tk.Entry(form,
                             bg="#1f2937",
                             fg="white",
                             insertbackground="white",
                             relief="flat",
                             font=("Segoe UI", 10))
            entry.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
            return entry

        form.grid_columnconfigure(1, weight=1)
        form.grid_columnconfigure(3, weight=1)

        crear_label("Nombre", 0, 0)
        self.entry_nombre = crear_entry(0, 1)

        crear_label("Apellido", 0, 2)
        self.entry_apellido = crear_entry(0, 3)

        crear_label("Especialidad", 1, 0)
        self.combo_especialidad = ttk.Combobox(form, values=self.especialidades)
        self.combo_especialidad.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        crear_label("Teléfono", 1, 2)
        self.entry_telefono = crear_entry(1, 3)

        crear_label("Horario", 2, 0)
        self.combo_horario = ttk.Combobox(form, values=self.horarios)
        self.combo_horario.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # 🔘 BOTONES
        btn_frame = tk.Frame(form, bg="#111827")
        btn_frame.grid(row=3, column=0, columnspan=4, pady=10)

        def btn(texto, color, cmd):
            return tk.Button(btn_frame, text=texto,
                             bg=color, fg="white",
                             font=("Segoe UI", 10, "bold"),
                             bd=0, padx=10, pady=5,
                             cursor="hand2",
                             command=cmd)

        btn("Agregar", "#22c55e", self.agregar_doctor).pack(side="left", padx=5)
        btn("Actualizar", "#3b82f6", self.actualizar_doctor).pack(side="left", padx=5)
        btn("Eliminar", "#ef4444", self.eliminar_doctor).pack(side="left", padx=5)
        btn("Limpiar", "#f59e0b", self.limpiar_formulario).pack(side="left", padx=5)

        # 📊 TABLA
        tabla_frame = tk.Frame(container, bg="#111827")
        tabla_frame.grid(row=1, column=0, sticky="nsew")

        self.tabla = ttk.Treeview(tabla_frame,
                                 columns=("ID", "Nombre", "Apellido", "Especialidad", "Telefono", "Horario"),
                                 show="headings")

        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center")

        self.tabla.pack(fill="both", expand=True)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

    # 🔧 FUNCIONES
    def agregar_doctor(self):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO doctores VALUES (NULL, ?, ?, ?, ?, ?)",
                       (self.entry_nombre.get(),
                        self.entry_apellido.get(),
                        self.combo_especialidad.get(),
                        self.entry_telefono.get(),
                        self.combo_horario.get()))
        self.conexion.commit()
        self.cargar_doctores()

    def cargar_doctores(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)

        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM doctores")
        for row in cursor.fetchall():
            self.tabla.insert("", "end", values=row)

    def seleccionar(self, event):
        item = self.tabla.item(self.tabla.selection())
        valores = item["values"]
        if valores:
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, valores[1])

    def actualizar_doctor(self):
        pass  # puedes completar luego

    def eliminar_doctor(self):
        pass

    def limpiar_formulario(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)

    def cerrar(self):
        self.ventana.destroy()

    def ir_inicio(self):
        self.ventana.destroy()


# ▶️ EJECUCIÓN
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = ModuloDoctores(root)
    root.mainloop()