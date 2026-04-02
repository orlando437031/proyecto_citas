import uuid

class Paciente:
    def _init_(self, nombre, edad, historial_medico=""):
        self.id_p = str(uuid.uuid4())[:8] # Genera un ID corto y único
        self.nombre = nombre
        self.edad = edad
        self.historial_medico = historial_medico