# Ejecutar la Aplicación Python

Este documento explica los pasos necesarios para ejecutar la aplicación correctamente.

## Requisitos Previos

- Tener instalado [Python](https://www.python.org/) (versión 3.7 o superior recomendada).
- Tener instalado `pip` para la gestión de paquetes de Python.
- (Opcional pero recomendado) Tener instalado [Visual Studio Code](https://code.visualstudio.com/) u otro editor de código con soporte para Python.

## Configuración del Entorno Virtual

Se recomienda crear un entorno virtual para gestionar las dependencias del proyecto de forma aislada.

### Opción 1: Usando Visual Studio Code
1. Abrir el proyecto en Visual Studio Code.
2. Abrir la terminal integrada (``Ctrl + ` `` en Windows o `Cmd + `` en macOS).
3. Ejecutar el siguiente comando para crear el entorno virtual:
   ```sh
   python -m venv venv
   ```
4. Activar el entorno virtual:
   - En Windows:
     ```sh
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

### Opción 2: Usando la Terminal

1. Navegar a la carpeta del proyecto y ejecutar:
   ```sh
   python -m venv venv
   ```
2. Activar el entorno virtual:
   - En Windows:
     ```sh
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

## Instalación de Dependencias

Una vez activado el entorno virtual, instalar las dependencias necesarias con:
```sh
pip install -r requirements.txt
```

## Creación de la Base de Datos

Para inicializar la base de datos, ejecutar el siguiente comando:
```sh
python db_instance.py
```

## Ejecutar la Aplicación

Para iniciar la aplicación, ejecutar el siguiente comando:
```sh
python api.py
```

## Notas

- Asegúrate de activar el entorno virtual antes de ejecutar los comandos de instalación y ejecución.
- Si se presentan problemas con permisos, usar `python -m pip install --user -r requirements.txt` para instalar las dependencias.
- Para salir del entorno virtual, ejecutar `deactivate` en la terminal.

