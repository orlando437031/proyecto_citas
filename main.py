def menu_principal():
gestion = GestionMedica()
    
    while True:
        print("\n=== SISTEMA MÉDICO - MÓDULO GEORDANY ===")
        print("1. Agregar Paciente")
        print("2. Listar Pacientes")
        print("3. Agregar Doctor")
        print("4. Listar Doctores")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_p = input("ID: ")
            nom = input("Nombre: ")
            edad = input("Edad: ")
            gestion.crear_paciente(nom, edad, id_p)
        elif opcion == "2":
            gestion.listar_pacientes()
        elif opcion == "3":
            id_d = input("ID: ")
            nom = input("Nombre: ")
            esp = input("Especialidad: ")
            gestion.crear_doctor(nom, esp, id_d)
        elif opcion == "4":
            gestion.listar_doctores()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()
