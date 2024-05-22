import os
import shutil

def combinar_archivos(directorio_origen, directorio_destino):
    """
    Combina archivos de respaldo de Google Takeout en un solo directorio.

    Args:
        directorio_origen: La ruta al directorio que contiene los archivos de respaldo.
        directorio_destino: La ruta al directorio donde se guardarán los archivos combinados.
    """

    # Crea el directorio de destino si no existe
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)

    # Recorre cada archivo en el directorio de origen
    for archivo in os.listdir(directorio_origen):
        ruta_archivo = os.path.join(directorio_origen, archivo)

        # Si el archivo es una carpeta
        if os.path.isdir(ruta_archivo):
            # Combina los archivos dentro de la carpeta
            combinar_archivos(ruta_archivo, os.path.join(directorio_destino, archivo))

        # Si el archivo es un archivo regular (no una carpeta)
        else:
            try:
                ruta_destino_archivo = os.path.join(directorio_destino, archivo)
                
                # Evita sobreescribir archivos existentes
                if os.path.exists(ruta_destino_archivo):
                    print(f"El archivo {ruta_destino_archivo} ya existe. Se omitirá.")
                else:
                    shutil.copyfile(ruta_archivo, ruta_destino_archivo)
                    print(f"Copiado: {ruta_archivo} a {ruta_destino_archivo}")
            
            except Exception as e:
                print(f"Error al copiar {ruta_archivo} a {ruta_destino_archivo}: {e}")

# Especifica los directorios de origen y destino
directorio_origen = "/Users/gabrielsosa/Documents/RespaldoGoogleFotos/Takeout 8/Google Fotos"
directorio_destino = "/Users/gabrielsosa/Documents/CarpetaGoogleFotos"

# Ejecuta la función para combinar los archivos
combinar_archivos(directorio_origen, directorio_destino)
