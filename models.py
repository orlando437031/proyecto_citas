import uuid

# Clase Paciente
class Paciente:
    def __init__(self, nombre, edad):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Paciente: {self.nombre} (ID: {self.id})"


# Clase Doctor
class Doctor:
    def __init__(self, nombre, especialidad):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Doctor: {self.nombre} - {self.especialidad} (ID: {self.id})"


# Clase Cita
class Cita:
    def __init__(self, paciente, doctor, fecha, hora):
        self.id = str(uuid.uuid4())
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"Cita: {self.paciente.nombre} con {self.doctor.nombre} el {self.fecha} a las {self.hora}"
