class DoctorServicios:
    def _init_(self):
        # Simulamos una base de datos con listas
        self.pacientes = []
        self.doctores = []

    # --- CRUD PACIENTES ---
    def crear_paciente(self, nombre, edad, id_paciente):
        paciente = {"id": id_paciente, "nombre": nombre, "edad": edad}
        self.pacientes.append(paciente)
        print(f"Paciente {nombre} creado con éxito.")

    def listar_pacientes(self):
        print("\n--- Lista de Pacientes ---")
        for p in self.pacientes:
            print(f"ID: {p['id']} | Nombre: {p['nombre']} | Edad: {p['edad']}")

    def actualizar_paciente(self, id_paciente, nuevo_nombre):
        for p in self.pacientes:
            if p['id'] == id_paciente:
                p['nombre'] = nuevo_nombre
                print("Paciente actualizado.")
                return
        print("Paciente no encontrado.")

    def eliminar_paciente(self, id_paciente):
        self.pacientes = [p for p in self.pacientes if p['id'] != id_paciente]
        print(f"Paciente con ID {id_paciente} eliminado.")

    # --- CRUD DOCTORES (Estructura similar) ---
    def crear_doctor(self, nombre, especialidad, id_doctor):
        doctor = {"id": id_doctor, "nombre": nombre, "especialidad": especialidad}
        self.doctores.append(doctor)
        print(f"Dr. {nombre} creado con éxito.")

    def listar_doctores(self):
        print("\n--- Lista de Doctores ---")
        for d in self.doctores:
            print(f"ID: {d['id']} | Dr. {d['nombre']} | Especialidad: {d['especialidad']}")