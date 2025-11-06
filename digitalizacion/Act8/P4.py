# Programa 4: Computación en la nube - Gestión de usuarios
import json

usuarios = [
    {"usuario": "admin1", "clave": "abc123"},
    {"usuario": "tecnico2", "clave": "xyz789"},
]

# Guardar usuarios
with open("usuarios_nube.json", "w", encoding="utf-8") as f:
    json.dump(usuarios, f, indent=4, ensure_ascii=False)
    # dump convierte un objeto de Python a json y lo escribe directamente en un archivo
    # ensure_ascii = False. Este parámetro en False mantiene las tildes y caracteres latinos

# Leer usuarios
with open("usuarios_nube.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print("=== Usuarios registrados ===")
    for u in data:
        print(f"Usuario: {u['usuario']}, Clave cifrada: {u['clave']}")
