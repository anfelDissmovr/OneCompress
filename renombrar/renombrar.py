#Cambia el nombre desde 001
import os
import re

def listar_archivos(carpeta):
    """Devuelve una lista de archivos ordenados numéricamente en la carpeta o None si no existe."""
    try:
        archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
        
        # Ordenar extrayendo el número de cada archivo
        archivos.sort(key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else float('inf'))
        
        return archivos
    except FileNotFoundError:
        return None

# Definir la carpeta
carpeta = r"C:/Users/anfel/Downloads/DissmoVr/Arista/Arista/IMAGENES/SLIDER-ARISTA-FULL/100K @ 20"
archivos = listar_archivos(carpeta)

if archivos is None:
    print(f"La carpeta '{carpeta}' no existe.")
else:
    print("Archivos antes del renombrado:", archivos)

    nuevo_numero = 4001  # Inicia desde 1
    for archivo in archivos:
        ruta_vieja = os.path.join(carpeta, archivo)
        extension = os.path.splitext(archivo)[1]
        # Rellenar con ceros a la izquierda para lograr 3 dígitos
        nuevo_nombre = f"{str(nuevo_numero).zfill(3)}{extension}"
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)

        try:
            os.rename(ruta_vieja, ruta_nueva)
            nuevo_numero += 1  
        except Exception as e:
            print(f"Error renombrando '{archivo}': {e}")

    # Verificar los cambios
    archivos_renombrados = listar_archivos(carpeta)
    print("Archivos después del renombrado:", archivos_renombrados)


# import os
# import re

# def listar_archivos(carpeta):
#     """Devuelve una lista de archivos ordenados numéricamente en la carpeta o None si no existe."""
#     try:
#         archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
        
#         # Ordenar extrayendo el número de cada archivo
#         archivos.sort(key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else float('inf'))
        
#         return archivos
#     except FileNotFoundError:
#         return None

# # Definir la carpeta
# carpeta = "C:/Users/anfel/Downloads/DissmoVr/COCUY/curubal-2025/SLIDER/100K"
# archivos = listar_archivos(carpeta)

# if archivos is None:
#     print(f"La carpeta '{carpeta}' no existe.")
# else:
#     print("Archivos antes del renombrado:", archivos)

#     nuevo_numero = 280  # Número inicial
#     for archivo in archivos:
#         ruta_vieja = os.path.join(carpeta, archivo)
#         extension = os.path.splitext(archivo)[1]
#         nuevo_nombre = f"{nuevo_numero}{extension}"
#         ruta_nueva = os.path.join(carpeta, nuevo_nombre)

#         try:
#             os.rename(ruta_vieja, ruta_nueva)
#             nuevo_numero += 2  # Incremento de dos en dos
#         except Exception as e:
#             print(f"Error renombrando '{archivo}': {e}")

#     # Verificar los cambios
#     archivos_renombrados = listar_archivos(carpeta)
#     print("Archivos después del renombrado:", archivos_renombrados)

# import os
# import re

# def listar_archivos(carpeta):
#     """Devuelve una lista de archivos ordenados numéricamente en la carpeta o None si no existe."""
#     try:
#         archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
#         archivos = [f for f in archivos if re.search(r'\d+', f)]  # Filtrar archivos con números

#         # Extraer y ordenar los archivos por número
#         archivos.sort(key=lambda x: int(re.search(r'\d+', x).group()))
        
#         return archivos
#     except FileNotFoundError:
#         return None

# def invertir_nombres(carpeta):
#     archivos = listar_archivos(carpeta)

#     if archivos is None:
#         print(f"La carpeta '{carpeta}' no existe.")
#         return

#     # Filtrar solo archivos en el rango 0360 a 0720
#     archivos_en_rango = [f for f in archivos if 360 <= int(re.search(r'\d+', f).group()) <= 720]

#     if not archivos_en_rango:
#         print("No se encontraron archivos en el rango.")
#         return
    
#     # Extraer los números y ordenarlos
#     numeros = sorted([int(re.search(r'\d+', f).group()) for f in archivos_en_rango])

#     # Generar el mapeo inverso (Ej: 0360 -> 0720, 0361 -> 0719, ..., 0720 -> 0360)
#     nuevos_nombres = {num: numeros[::-1][i] for i, num in enumerate(numeros)}

#     # Renombrar usando nombres temporales
#     temp_names = {}
#     for archivo in archivos_en_rango:
#         num_actual = int(re.search(r'\d+', archivo).group())
#         num_nuevo = nuevos_nombres[num_actual]
#         extension = os.path.splitext(archivo)[1]
#         temp_name = f"temp_{num_nuevo}{extension}"  # Evitar conflicto al renombrar
#         os.rename(os.path.join(carpeta, archivo), os.path.join(carpeta, temp_name))
#         temp_names[temp_name] = num_nuevo  # Guardar el mapeo temporal
    
#     # Aplicar los nombres finales
#     for temp_name, num_nuevo in temp_names.items():
#         extension = os.path.splitext(temp_name)[1]
#         nombre_final = f"{num_nuevo:04d}{extension}"
#         os.rename(os.path.join(carpeta, temp_name), os.path.join(carpeta, nombre_final))

#     print("Renombrado completado.")

# # Definir la carpeta donde están las imágenes
# carpeta = "C:/Users/anfel/Downloads/DissmoVr/curubal-2025/SLIDER/600K"
# invertir_nombres(carpeta)

# import os
# import re

# def listar_archivos(carpeta):
#     """Devuelve una lista de archivos ordenados numéricamente en la carpeta o None si no existe."""
#     try:
#         archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
#         archivos = [f for f in archivos if re.search(r'\d+', f)]  # Filtrar archivos con números
#         archivos.sort(key=lambda x: int(re.search(r'\d+', x).group()))  # Ordenar por número
#         return archivos
#     except FileNotFoundError:
#         return None

# def renombrar_archivos(carpeta):
#     archivos = listar_archivos(carpeta)

#     if archivos is None:
#         print(f"La carpeta '{carpeta}' no existe.")
#         return

#     if not archivos:
#         print("No hay archivos para renombrar.")
#         return

#     nuevo_numero = 280  # Número inicial en la secuencia
#     incremento = 2  # Aumenta de dos en dos

#     for archivo in archivos:
#         ruta_vieja = os.path.join(carpeta, archivo)
#         extension = os.path.splitext(archivo)[1]

#         nuevo_nombre = f"{nuevo_numero}{extension}"
#         ruta_nueva = os.path.join(carpeta, nuevo_nombre)

#         try:
#             os.rename(ruta_vieja, ruta_nueva)
#             nuevo_numero += incremento  # Siguiente número par
#         except Exception as e:
#             print(f"Error renombrando '{archivo}': {e}")

#     # Verificar los cambios
#     archivos_renombrados = listar_archivos(carpeta)
#     print("Archivos después del renombrado:", archivos_renombrados)

# # Definir la carpeta donde están los archivos
# carpeta = "C:/Users/anfel/Downloads/DissmoVr/curubal-2025/SLIDER/100K"
# renombrar_archivos(carpeta)
