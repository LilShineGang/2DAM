import os

dir = "/var/lib/docker/volumes/datos_uploads/_data"

print("Archivos subidos:")

try:
    archivos = os.listdir(dir)

    if not archivos:
        print("No hay archivos subidos.")
    else:
        print(f"Se han encontrado {len(archivos)} archivos:")
        for f in archivos:
            print(f"  -> {f}")

except FileNotFoundError:
    print(f"Error: El directorio '{dir}' no se ha encontrado.")
    print("Monta bien el volumen")
except Exception as e:
    print(f"ERROR: {e}")
