# 🏥 MediControl Pro v3.0 - Sistema Médico Integral

*MediControl Pro* es una aplicación de escritorio desarrollada en Python para la gestión eficiente de clínicas y centros médicos. Permite la administración de pacientes, doctores y el control detallado de citas médicas y emergencias en tiempo real.

---

## 🚀 Características Principales

*   *Panel de Control (Dashboard):* Visualización inmediata de citas del día y emergencias.
*   *Gestión de Pacientes:* Registro, actualización y consulta de historial clínico.
*   *Control de Doctores:* Administración de especialidades y disponibilidad.
*   *Módulo de Citas:* Sistema de agendamiento con estados (Pendiente, Completada, Emergencia).
*   *Base de Datos Robusta:* Implementación con SQLite para persistencia de datos local.

---

## 🛠️ Estructura del Proyecto

El proyecto sigue una arquitectura organizada por módulos:

*   main.py: Punto de entrada principal de la aplicación.
*   views/: Contiene los archivos de la interfaz gráfica (UI).
*   services/: Lógica de negocio y manejo de datos de pacientes y doctores.
*   utils/: Funciones auxiliares como generadores de UUID.
*   data/: Almacena la base de datos clinica.db.

---

## 📋 Requisitos del Sistema

Antes de iniciar, asegúrate de tener instalado:
*   [Python 3.10+](https://python.org)
*   Librería Pillow (para el manejo de imágenes).
*   Librería Tkinter (incluida habitualmente en Python).

---

## 💻 Instalación y Configuración

1. *Clonar el repositorio:*
   ```bash
   git clone https://github.com/orlando437031/proyecto_citas
   cd proyecto_citas-main