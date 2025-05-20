import os
from subprocess import run

def start_server():
    # Instalar dependencias desde requirements.txt
    run(["pip", "install", "-r", "requirements.txt"], check=True)

    # Activar el entorno virtual (si estás en Windows)
    os.system("venv\\Scripts\\activate")

    # Configurar variables de entorno
    os.environ["FLASK_APP"] = "main.py"
    os.environ["FLASK_DEBUG"] = "1"

    # Ejecutar el servidor Flask
    run(["flask", "run"])

# Función para iniciar el servidor
start_server()