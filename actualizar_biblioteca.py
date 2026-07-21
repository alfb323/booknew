import os
import json

# Ruta de tu carpeta de libros
carpeta_libros = "libros"
archivo_json = "libros.json"

# Crear la carpeta si no existe para que no de error
if not os.path.exists(carpeta_libros):
    os.makedirs(carpeta_libros)
    print(f"He creado la carpeta '{carpeta_libros}'. Mete ahí todos tus PDFs y vuelve a ejecutar el script.")
    exit()

nuevos_libros = []

print("Escaneando biblioteca... Esto puede tardar unos segundos.")

# Lee de golpe todos los archivos que metiste en la carpeta
for nombre_archivo in os.listdir(carpeta_libros):
    if nombre_archivo.lower().endswith('.pdf'):
        # Quita el ".pdf" del final para usarlo como título limpio
        titulo_limpio = nombre_archivo.rsplit('.', 1)[0]
        
        # Reemplaza guiones bajos o medios por espacios para que se vea bien en el buscador
        titulo_legible = titulo_limpio.replace('_', ' ').replace('-', ' ').title()
        
        # Arma la estructura del libro de forma automática
        libro = {
            "titulo": titulo_legible,
            "autor": "Autor Desconocido", # Al ser masivo, se deja así, o el usuario busca por el nombre del archivo
            "archivo_pdf": f"{carpeta_libros}/{nombre_archivo}",
            "portada": "https://openlibrary.org/images/icons/avatar_book-sm.png" # Portada genérica por defecto para no saturar
        }
        nuevos_libros.append(libro)

# Guarda los 6,000+ libros de una sola vez en tu JSON
with open(archivo_json, "w", encoding="utf-8") as f:
    json.dump(nuevos_libros, f, ensure_ascii=False, indent=2)

print(f"¡Listo! Se escanearon y agregaron {len(nuevos_libros)} libros al archivo '{archivo_json}' automáticamente.")