import re

# Credenciales válidas predefinidas
USUARIO_VALIDO = "admin123"
CONTRASENA_VALIDA = "pass2025"

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
if re.match("^[a-zA-Z0-9]+$", usuario):
    # Validación de la contraseña
    # ----------------------------
    # Patrón: '^[a-zA-Z0-9]{6,}$'
    # ^          - inicio de la cadena
    # [a-zA-Z0-9] - cualquier letra o número
    # {6,}       - al menos 6 caracteres
    # $          - final de la cadena
    if re.match("^[a-zA-Z0-9]{6,}$", contrasena):
        # Verificación con credenciales predefinidas
        if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
            print("Login exitoso.")
        else:
            print("Usuario o contraseña incorrectos.")
    else:
        print("La contraseña no cumple con las reglas básicas (mínimo 6 caracteres, letras y números).")
else:
    print("El usuario no cumple con las reglas básicas (solo letras y números).")
