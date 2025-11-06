import re

# Credenciales válidas predefinidas
USUARIO_VALIDO = "dan"       
CONTRASENA_VALIDA = "123456789"  

# Códigos ANSI para colores
ANSI_RESET = "\033[0m"
ANSI_RED = "\033[31m"
ANSI_GREEN = "\033[32m"

# Solicitar credenciales al usuario
usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

# Validación del usuario
# -----------------------
# Patrón: '^[a-zA-Z0-9]+$'
# ^          - indica el inicio de la cadena
# [a-zA-Z0-9] - cualquier letra mayúscula, minúscula o número
# +          - uno o más caracteres del conjunto anterior
# $          - indica el final de la cadena
if re.match(r"^[a-z]{1,10}$", usuario):   
    # Validación de la contraseña
    # ----------------------------
    # Patrón: '^[a-zA-Z0-9]{6,}$'
    # ^          - inicio de la cadena
    # [a-zA-Z0-9] - cualquier letra o número
    # {6,}       - al menos 6 caracteres
    # $          - final de la cadena
    if re.match(r"^[0-9\*]{9,}$", contrasena):
        # Verificación con credenciales predefinidas
        if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
            print(f"{ANSI_GREEN}Login exitoso. Sistema desbloqueado.{ANSI_RESET}")
        else:
            print(f"{ANSI_RED}Usuario o contraseña incorrectos.{ANSI_RESET}")
    else:
        print(f"{ANSI_RED}La contraseña no cumple las reglas: mínimo 9 caracteres, solo dígitos o '*'.{ANSI_RESET}")
else:
    print(f"{ANSI_RED}El usuario no cumple las reglas: solo letras minúsculas, máximo 10 caracteres.{ANSI_RESET}")

