import uuid
from datetime import datetime

class Cita:
    def _init_(self, paciente_id, doctor_id, fecha, motivo):
        self.id_c = str(uuid.uuid4())[:8] # ID único de la cita
        self.paciente_id = paciente_id
        self.doctor_id = doctor_id
        self.fecha = fecha
        self.motivo = motivo