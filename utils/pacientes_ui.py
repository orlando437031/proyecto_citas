import tkinter as tk
from tkinter import ttk, messagebox
import uuid

#  Colores
COLOR_FONDO = "#f2e9ff"
COLOR_TITULO = "#3b82f6"
COLOR_BOTON = "#ec4899"
COLOR_TABLA = "#ede9fe"
COLOR_TEXTO = "#1f2933"

class PacientesUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Pacientes")
        self.root.configure(bg=COLOR_FONDO)
        self.root.geometry("600x400")

        # Título
        titulo = tk.Label(
            root,
            text="Registro de Pacientes",
            bg=COLOR_FONDO,
            fg=COLOR_TITULO,
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=10)

        frame = tk.Frame(root, bg=COLOR_FONDO)
        frame.pack()

        # Etiquetas
        tk.Label(frame, text="Nombre:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=0, pady=5)
        tk.Label(frame, text="Cédula:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=1, column=0, pady=5)
        tk.Label(frame, text="Teléfono:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=2, column=0, pady=5)

        self.nombre = tk.Entry(frame)
        self.cedula = tk.Entry(frame)
        self.telefono = tk.Entry(frame)

        self.nombre.grid(row=0, column=1)
        self.cedula.grid(row=1, column=1)
        self.telefono.grid(row=2, column=1)

        # Botón
        boton = tk.Button(
            frame,
            text="Agregar Paciente",
            bg=COLOR_BOTON,
            fg="white",
            command=self.agregar
        )
        boton.grid(row=3, columnspan=2, pady=10)

        # Tabla
        style = ttk.Style()
        style.configure("Treeview", background=COLOR_TABLA, foreground=COLOR_TEXTO)
        style.configure("Treeview.Heading", background="#8b5cf6", foreground="white")

        self.tabla = ttk.Treeview(
            root,
            columns=("ID", "Nombre", "Cédula", "Teléfono"),
            show="headings"
        )

        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)

        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

    def agregar(self):
        if not self.nombre.get() or not self.cedula.get() or not self.telefono.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        self.tabla.insert("", "end", values=(
            str(uuid.uuid4())[:8],
            self.nombre.get(),
            self.cedula.get(),
            self.telefono.get()
        ))

        self.nombre.delete(0, tk.END)
        self.cedula.delete(0, tk.END)
        self.telefono.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PacientesUI(root)
    root.mainloop()