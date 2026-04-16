import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime

# Las citas de hoy
query_citas = "SELECT hora, paciente FROM citas WHERE fecha = date('now')"

# Emergencias (asegurándote de que los campos existan en tu DB)
query_emergencias = "SELECT paciente, motivo FROM citas WHERE tipo = 'Emergencia' AND estado = 'Pendiente'"



class MediControlPro:

    def __init__(self, root):

        self.root = root
        self.root.title("MediControl Pro v3.0 - Sistema Médico Integral")
        self.root.geometry("1100x700")
        self.root.configure(bg="#0a192f")

        self.conn = sqlite3.connect("./data/clinica.db")
        self.crear_tablas()

        self.mostrar_splash()

# ---------------- BASE DE DATOS ----------------

    def crear_tablas(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        identidad TEXT,
        edad TEXT,
        sexo TEXT,
        telefono TEXT)
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        especialidad TEXT,
        telefono TEXT)
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS citas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        paciente TEXT,
        identidad TEXT,
        doctor TEXT)
        """)

        self.conn.commit()

# ---------------- SPLASH ----------------

    def mostrar_splash(self):

        try:
            img = Image.open("imagen 2.webp").resize((1100,700))
            self.bg = ImageTk.PhotoImage(img)

            lbl = tk.Label(self.root,image=self.bg)
            lbl.place(x=0,y=0,relwidth=1,relheight=1)

        except:
            self.root.configure(bg="#0a192f")

        titulo = tk.Label(
            self.root,
            text="MEDICONTROL PRO",
            font=("Century Gothic",40,"bold"),
            fg="#00e5ff",
            bg="#0a192f"
        )

        titulo.place(relx=0.5,rely=0.4,anchor="center")

        self.barra = ttk.Progressbar(self.root,length=500,mode="determinate")
        self.barra.place(relx=0.5,rely=0.6,anchor="center")

        self.cargar(0)

    def cargar(self,n):

        if n<=100:
            self.barra["value"]=n
            self.root.after(20,self.cargar,n+1)

        else:

            btn=tk.Button(
                self.root,
                text="INGRESAR AL PANEL",
                font=("Arial",14,"bold"),
                bg="#00e5ff",
                fg="#0a192f",
                command=self.dashboard
            )

            btn.place(relx=0.5,rely=0.75,anchor="center")

# ---------------- DASHBOARD ----------------

    def dashboard(self):

        for w in self.root.winfo_children():
            w.destroy()

        sidebar = tk.Frame(self.root,bg="#112240",width=250)
        sidebar.pack(side="left",fill="y")

        tk.Label(
            sidebar,
            text="🏥 MENU",
            font=("Arial",20,"bold"),
            bg="#112240",
            fg="#00e5ff"
        ).pack(pady=30)

        tk.Button(sidebar,text="👥 PACIENTES",bg="#112240",fg="white",
                  command=self.modulo_pacientes).pack(fill="x",pady=5)

        tk.Button(sidebar,text="👨‍⚕️ DOCTORES",bg="#112240",fg="white",
                  command=self.modulo_doctores).pack(fill="x",pady=5)

        tk.Button(sidebar,text="📅 CITAS",bg="#112240",fg="white",
                  command=self.modulo_citas).pack(fill="x",pady=5)

        main=tk.Frame(self.root,bg="#0a192f")
        main.pack(expand=True,fill="both")

        tk.Label(
            main,
            text="BIENVENIDO A MEDICONTROL PRO",
            font=("Century Gothic",25,"bold"),
            fg="white",
            bg="#0a192f"
        ).pack(pady=50)

# ---------------- PACIENTES ----------------

    def modulo_pacientes(self):

        top=tk.Toplevel(self.root)
        top.title("Pacientes")
        top.geometry("500x500")

        tk.Label(top,text="Nombre").pack()
        nombre=tk.Entry(top)
        nombre.pack()

        tk.Label(top,text="Identidad").pack()
        identidad=tk.Entry(top)
        identidad.pack()

        tk.Label(top,text="Edad").pack()
        edad=tk.Entry(top)
        edad.pack()

        tk.Label(top,text="Sexo").pack()
        sexo=tk.Entry(top)
        sexo.pack()

        tk.Label(top,text="Telefono").pack()
        telefono=tk.Entry(top)
        telefono.pack()

        def guardar():

            cursor=self.conn.cursor()

            cursor.execute(
            "INSERT INTO pacientes(nombre,identidad,edad,sexo,telefono) VALUES(?,?,?,?,?)",
            (nombre.get(),identidad.get(),edad.get(),sexo.get(),telefono.get())
            )

            self.conn.commit()

            messagebox.showinfo("Guardado","Paciente guardado exitosamente")

        def buscar():

            cursor=self.conn.cursor()

            cursor.execute("""
            SELECT nombre,identidad,edad,sexo,telefono
            FROM pacientes
            WHERE nombre LIKE ? OR identidad LIKE ? OR telefono LIKE ?
            """,(
                "%"+nombre.get()+"%",
                "%"+identidad.get()+"%",
                "%"+telefono.get()+"%"
            ))

            r=cursor.fetchone()

            if r:

                nombre.delete(0,tk.END)
                identidad.delete(0,tk.END)
                edad.delete(0,tk.END)
                sexo.delete(0,tk.END)
                telefono.delete(0,tk.END)

                nombre.insert(0,r[0])
                identidad.insert(0,r[1])
                edad.insert(0,r[2])
                sexo.insert(0,r[3])
                telefono.insert(0,r[4])

            else:

                messagebox.showinfo("Buscar","Paciente no encontrado")

        tk.Button(top,text="Guardar",command=guardar).pack(pady=10)
        tk.Button(top,text="Buscar Paciente",command=buscar).pack()

# ---------------- DOCTORES ----------------

    def modulo_doctores(self):

        top=tk.Toplevel(self.root)
        top.title("Doctores")
        top.geometry("400x300")

        tk.Label(top,text="Nombre").pack()
        nombre=tk.Entry(top)
        nombre.pack()

        tk.Label(top,text="Especialidad").pack()
        esp=tk.Entry(top)
        esp.pack()

        tk.Label(top,text="Telefono").pack()
        tel=tk.Entry(top)
        tel.pack()

        def guardar():

            cursor=self.conn.cursor()

            cursor.execute(
            "INSERT INTO doctores(nombre,especialidad,telefono) VALUES(?,?,?)",
            (nombre.get(),esp.get(),tel.get())
            )

            self.conn.commit()

            messagebox.showinfo("Guardado","Doctor guardado exitosamente")

        tk.Button(top,text="Guardar",command=guardar).pack(pady=20)

# ---------------- CITAS ----------------

    def modulo_citas(self):

        top=tk.Toplevel(self.root)
        top.title("Citas")
        top.geometry("750x550")

        tk.Label(top,text="Nombre Paciente").pack()
        nombre=tk.Entry(top)
        nombre.pack()

        tk.Label(top,text="Identidad").pack()
        identidad=tk.Entry(top)
        identidad.pack()

        tk.Label(top,text="Doctor").pack()
        doctor=tk.Entry(top)
        doctor.pack()

        tk.Label(top,text="Fecha (YYYY-MM-DD)").pack()
        fecha=tk.Entry(top)
        fecha.pack()

        tabla=ttk.Treeview(top,columns=("Fecha","Paciente","Doctor"),show="headings")
        tabla.heading("Fecha",text="Fecha")
        tabla.heading("Paciente",text="Paciente")
        tabla.heading("Doctor",text="Doctor")
        tabla.pack(fill="both",expand=True)

        def limpiar_tabla():
            for item in tabla.get_children():
                tabla.delete(item)

        def ver_todas():

            limpiar_tabla()

            cursor=self.conn.cursor()
            cursor.execute("SELECT fecha,paciente,doctor FROM citas")

            for r in cursor.fetchall():
                tabla.insert("",tk.END,values=r)

        def citas_hoy():

            limpiar_tabla()

            hoy=datetime.now().strftime("%Y-%m-%d")

            cursor=self.conn.cursor()
            cursor.execute(
                "SELECT fecha,paciente,doctor FROM citas WHERE fecha=?",
                (hoy,)
            )

            for r in cursor.fetchall():
                tabla.insert("",tk.END,values=r)

        def crear():

            cursor=self.conn.cursor()

            cursor.execute(
                "INSERT INTO citas(fecha,paciente,identidad,doctor) VALUES(?,?,?,?)",
                (fecha.get(),nombre.get(),identidad.get(),doctor.get())
            )

            self.conn.commit()

            messagebox.showinfo("Guardado","Cita registrada")

            ver_todas()

        def eliminar():

            item=tabla.selection()

            if not item:
                messagebox.showwarning("Eliminar","Seleccione una cita")
                return

            datos=tabla.item(item[0])["values"]

            cursor=self.conn.cursor()

            cursor.execute(
            "DELETE FROM citas WHERE fecha=? AND paciente=? AND doctor=?",
            (datos[0],datos[1],datos[2])
            )

            self.conn.commit()

            ver_todas()

        tk.Button(top,text="Crear Cita",command=crear).pack(pady=5)
        tk.Button(top,text="Eliminar Cita",command=eliminar).pack(pady=5)
        tk.Button(top,text="Citas del Día",command=citas_hoy).pack(pady=5)
        tk.Button(top,text="Ver Todas las Citas",command=ver_todas).pack(pady=5)

        ver_todas()

# ---------------- INICIO ----------------

if __name__=="__main__":

    root=tk.Tk()

    app=MediControlPro(root)

    root.mainloop()