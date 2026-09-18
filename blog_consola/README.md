# Sistema de Gestión de Blog de Posts 

Este proyecto es un sistema interactivo por consola refactorizado en una arquitectura modular orientada a paquetes y módulos en Python.

## Estructura del Proyecto

```text
blog_consola/
│
├── main.py              # Archivo principal y orquestador del flujo
├── README.md            # Documentación del proyecto
│
└── blog/                # Paquete principal del sistema
    ├── __init__.py      # Inicializador del paquete
    ├── datos.py         # Estructuras de datos base (posts, autor, tags, estados)
    ├── menu.py          # Presentación del menú y captura de entradas
    ├── operaciones.py   # Lógica de listado, búsqueda y filtrado
    └── validaciones.py  # Reglas de negocio e integridad de los datos