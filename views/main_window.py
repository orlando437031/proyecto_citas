import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class ModuloDoctores:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.title("Sistema Médico Elite - Gestión de Especialistas")
        self.ventana.geometry("1100x700")
        self.ventana.configure(bg='#0b0f19') # Negro profundo
        self.ventana.resizable(True, True)

        # Conexión Base de Datos
        self.conexion = sqlite3.connect('clinica.db')
        self.crear_tabla()

        # Datos Config
        self.especialidades = ["Cardiología", "Pediatría", "Dermatología", "Neurología", "Ginecología"]
        self.horarios = ["Matutino (08:00 - 14:00)", "Vespertino (14:00 - 20:00)", "Nocturno (20:00 - 02:00)"]

        self.crear_estilos()
        self.crear_widgets()
        self.cargar_doctores()

    def crear_tabla(self):
        cursor = self.conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS doctores 
                       (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT, 
                        especialidad TEXT, telefono TEXT, horario TEXT)''')
        self.conexion.commit()

    def crear_estilos(self):
        style = ttk.Style()
        style.theme_use("clam") # Cambiado a 'clam' para mejor control
        
        # Estilo de la Tabla (Treeview)
        style.configure("Treeview",
                        background="#161b22",
                        foreground="#e6edf3",
                        fieldbackground="#161b22",
                        bordercolor="#30363d",
                        rowheight=35,
                        font=("Segoe UI", 10))
        
        style.configure("Treeview.Heading",
                        background="#21262d",
                        foreground="#ffb703", # Dorado para encabezados
                        font=("Segoe UI", 11, "bold"))

        style.map("Treeview", background=[("selected", "#d4a017")], foreground=[("selected", "black")])

    def crear_widgets(self):
        # 🟡 SIDEBAR IZQUIERDO (Navegación Vertical)
        self.sidebar = tk.Frame(self.ventana, bg="#161b22", width=200)
        self.sidebar.pack(side="left", fill="y")

        tk.Label(self.sidebar, text="MODULO\nDOCTORES", font=("Impact", 20), 
                 bg="#161b22", fg="#ffb703", pady=30).pack()

        def btn_nav(texto, cmd, color="#ffb703"):
            return tk.Button(self.sidebar, text=texto, font=("Segoe UI", 10, "bold"),
                             bg="#161b22", fg=color, activebackground="#30363d",
                             activeforeground="white", bd=0, pady=15, cursor="hand2", command=cmd)

        btn_nav("🏠 INICIO", self.ir_inicio).pack(fill="x")
        btn_nav("🔄 RECARGAR", self.cargar_doctores).pack(fill="x")
        btn_nav("❌ SALIR", self.cerrar, "#ff4d4d").pack(side="bottom", fill="x")

        # ⚪ CONTENEDOR PRINCIPAL
        main_container = tk.Frame(self.ventana, bg="#0b0f19", padx=30, pady=20)
        main_container.pack(side="right", fill="both", expand=True)

        # --- SECCIÓN FORMULARIO (Diseño en Tarjeta) ---
        card_form = tk.Frame(main_container, bg="#161b22", padx=20, pady=20, 
                             highlightthickness=1, highlightbackground="#30363d")
        card_form.pack(fill="x", pady=(0, 20))

        tk.Label(card_form, text="REGISTRO DE PERSONAL MÉDICO", font=("Segoe UI", 14, "bold"), 
                 bg="#161b22", fg="white").grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 20))

        def input_field(txt, r, c):
            tk.Label(card_form, text=txt, bg="#161b22", fg="#8b949e", font=("Segoe UI", 9)).grid(row=r, column=c, sticky="w", padx=10)
            entry = tk.Entry(card_form, bg="#0d1117", fg="white", insertbackground="white", 
                             relief="flat", font=("Segoe UI", 11))
            entry.grid(row=r+1, column=c, padx=10, pady=(5, 15), sticky="ew")
            return entry

        card_form.columnconfigure((0,1,2,3), weight=1)
        
        self.entry_nombre = input_field("NOMBRE", 1, 0)
        self.entry_apellido = input_field("APELLIDO", 1, 1)
        self.entry_telefono = input_field("TELÉFONO", 1, 2)
        
        # Combos con estilo
        tk.Label(card_form, text="ESPECIALIDAD", bg="#161b22", fg="#8b949e").grid(row=3, column=0, sticky="w", padx=10)
        self.combo_esp = ttk.Combobox(card_form, values=self.especialidades, state="readonly")
        self.combo_esp.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        tk.Label(card_form, text="TURNO", bg="#161b22", fg="#8b949e").grid(row=3, column=1, sticky="w", padx=10)
        self.combo_hor = ttk.Combobox(card_form, values=self.horarios, state="readonly")
        self.combo_hor.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        # --- BOTONERA DE ACCIÓN ---
        action_frame = tk.Frame(card_form, bg="#161b22")
        action_frame.grid(row=4, column=2, columnspan=2, sticky="e", padx=10)

        def btn_act(txt, bg, cmd):
            return tk.Button(action_frame, text=txt, bg=bg, fg="white", font=("Segoe UI", 9, "bold"),
                             relief="flat", padx=20, pady=8, cursor="hand2", command=cmd)

        btn_act("＋ AGREGAR", "#238636", self.agregar_doctor).pack(side="left", padx=5)
        btn_act("🗑 ELIMINAR", "#da3633", self.eliminar_doctor).pack(side="left", padx=5)
        btn_act("🧹 LIMPIAR", "#484f58", self.limpiar_formulario).pack(side="left", padx=5)

        # --- TABLA DE RESULTADOS ---
        self.tabla = ttk.Treeview(main_container, columns=("ID", "NOMBRE", "APELLIDO", "ESPECIALIDAD", "TEL", "TURNO"), show="headings")
        
        columnas = [("ID", 50), ("NOMBRE", 150), ("APELLIDO", 150), ("ESPECIALIDAD", 150), ("TEL", 120), ("TURNO", 180)]
        for col, ancho in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=ancho, anchor="center")

        self.tabla.pack(fill="both", expand=True)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

    # Lógica mejorada
    def agregar_doctor(self):
        datos = (self.entry_nombre.get(), self.entry_apellido.get(), self.combo_esp.get(), 
                 self.entry_telefono.get(), self.combo_hor.get())
        
        if all(datos):
            cursor = self.conexion.cursor()
            cursor.execute("INSERT INTO doctores VALUES (NULL, ?, ?, ?, ?, ?)", datos)
            self.conexion.commit()
            messagebox.showinfo("Éxito", "Doctor registrado en el sistema elite.")
            self.cargar_doctores()
            self.limpiar_formulario()
        else:
            messagebox.showwarning("Incompleto", "Por favor llene todos los campos de registro.")

    def eliminar_doctor(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un doctor de la lista.")
            return
        
        if messagebox.askyesno("Confirmar", "¿Desea eliminar permanentemente este registro?"):
            item = self.tabla.item(seleccion)
            id_doc = item['values'][0]
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM doctores WHERE id=?", (id_doc,))
            self.conexion.commit()
            self.cargar_doctores()

    def cargar_doctores(self):
        for i in self.tabla.get_children(): self.tabla.delete(i)
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM doctores")
        for row in cursor.fetchall(): self.tabla.insert("", "end", values=row)

    def seleccionar(self, event):
        item = self.tabla.item(self.tabla.selection())
        v = item["values"]
        if v:
            self.limpiar_formulario()
            self.entry_nombre.insert(0, v[1])
            self.entry_apellido.insert(0, v[2])
            self.entry_telefono.insert(0, v[4])
            self.combo_esp.set(v[3])
            self.combo_hor.set(v[5])

    def limpiar_formulario(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.combo_esp.set('')
        self.combo_hor.set('')

    def cerrar(self): self.ventana.destroy()
    def ir_inicio(self): self.ventana.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = ModuloDoctores(root)
    root.mainloop()