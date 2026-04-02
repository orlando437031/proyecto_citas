# Lista global para simular una base de datos temporal
from models.paciente import Paciente

lista_pacientes = []

def crear_paciente():
    print("--- Registro de Nuevo Paciente ---")
    id_p = input("ID: ")
    nombre = input("Nombre: ")
    # Creamos el objeto usando la clase que descargaste de GitHub
    nuevo_paciente = Paciente(id_p, nombre) 
    lista_pacientes.append(nuevo_paciente)
    print("✅ Paciente registrado con éxito.")

def listar_pacientes():
    print("--- Lista de Pacientes ---")
    if not lista_pacientes:
        print("No hay pacientes registrados.")
    for p in lista_pacientes:
        print(f"ID: {p.id_p} | Nombre: {p.nombre}")

def actualizar_paciente():
    id_buscar = input("Introduce el ID del paciente a editar: ")
    for p in lista_pacientes:
        if p.id_p == id_buscar:
            # Pedimos el nuevo dato
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            p.nombre = nuevo_nombre
            print("✅ Paciente actualizado con éxito.")
            return # Salimos de la función al terminar
    
    print("⚠️ No se encontró ningún paciente con ese ID.")

def eliminar_paciente():
    id_buscar = input("ID del paciente a eliminar: ")
    global lista_pacientes
    lista_pacientes = [p for p in lista_pacientes if p.id_p != id_buscar]
    print("🗑️ Paciente eliminado (si existía).")