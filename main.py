from services.cita_service import *

#Crear citas
print(crear_cita("1", "1", "2026-03-07", "10:30"))
print(crear_cita("2", "1", "2026-03-07", "10:30"))

# Listar citas
print(listar_citas())

# Actualizar cita
print(actualizar_cita("1", "2026-03-07", "10:30", "2026-03-08", "11:00"))


# Eliminar cita
print(eliminar_cita("1", "2026-03-28", "11:00"))


# Ver resultado final
print(listar_citas())

