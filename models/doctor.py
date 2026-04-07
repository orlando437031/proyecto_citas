import uuid

class Doctor:
    def __init__(self, nombre, especialidad):
        self.id_d = str(uuid.uuid4())[:8] # ID único para el doctor
        self.nombre = nombre
        self.especialidad = especialidad