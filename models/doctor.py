import uuid

class Doctor:
    def _init_(self, nombre, especialidad):
        self.id_d = str(uuid.uuid4())[:8] # ID único para el doctor
        self.nombre = nombre
        self.especialidad = especialidad