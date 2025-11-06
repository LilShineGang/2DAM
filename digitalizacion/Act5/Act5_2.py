# Importar módulo adecuado
import re

# Diccionario con códigos y conceptos
codigos = {
    "!AA&5-1": "Acceso general",
    "!AA&5-2": "Acceso restringido",
    "!AA&5-3": "Permiso temporal",
    "!AA&5-4": "Administrador"
}


# Expresión regular general para el formato !AA&5-N, donde N puede ser cualquier dígito
patron_general = r"^![A-Z]{2}&5-\d$"

# Solicitar código al usuario
print("El formato del código debe ser el siguiente '!AA&5-N'")
codigo_usuario = input("Introduce tu código: ")

# Validar formato con la expresión regular
if re.match(patron_general, codigo_usuario):
    if codigo_usuario in codigos:
        print(f"\033[92mCódigo válido: corresponde a '{codigos[codigo_usuario]}'\033[0m")
    else:
        print("\033[93mEl formato es correcto, pero el código no está registrado en el sistema.\033[0m")
else:
    print("\033[91mEl código no cumple el formato esperado '!AA&5-N'.\033[0m")
    