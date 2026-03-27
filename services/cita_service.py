# Función para obtener todas las citas registradas
citas =[]
# Función para crear una nueva cita
def listar_citas():
    return citas

# Función para validar si ya existe una cita con el mismo doctor, fecha y hora
def validar_cita(doctor_id, fecha, hora):
    for cita in citas:
        if (
            cita["doctor_id"] == doctor_id and
            cita["fecha"] == fecha and
            cita["hora"] == hora
        ):
            return False  # Ya existe → NO permitir
    return True  # No existe → SÍ permitir


 #diccionario con los datos de la cita
def crear_cita(paciente_id, doctor_id, fecha, hora):
    
     # Validamos antes de crear la cita
    if not validar_cita(doctor_id, fecha, hora):
        return "Error: Ya existe una cita con ese doctor en esa fecha y hora"
    
    nueva_cita =  {
        "paciente_id": paciente_id,
        "doctor_id": doctor_id,
        "fecha": fecha,
        "hora": hora, 
          }
    
    # Retornamos la cita creada (confirmación)
    citas.append(nueva_cita)
    return nueva_cita

#Espacio de fucniones de confirmar y validar nuevas citas
def eliminar_cita(doctor_id, fecha, hora):
    for cita in citas:
        if(
            cita["doctor_id"] == doctor_id and
            cita["fecha"] == fecha and
            cita["hora"] == hora
        ):
        
             citas.remove (cita)
        return("Cita eliminada correctamente")
    
    return "Error: Cita no encontrada"

def actualizar_cita(doctor_id, fecha, hora, nueva_fecha, nueva_hora):
    
    for cita in citas:
        if(cita["doctor_id"] == doctor_id and
            cita["fecha"] == fecha and
            cita["hora"] == hora
            
            
        ):
        
            if not validar_cita(doctor_id, nueva_fecha, nueva_hora):
              return "Error: La nueva fecha y hora ya están ocupadas"
        cita["fecha"] =nueva_fecha
        cita["hora"] = nueva_hora
        
        return "cita actualizada correctamente"
    return "Error:  Cita no encontrada"
    
    