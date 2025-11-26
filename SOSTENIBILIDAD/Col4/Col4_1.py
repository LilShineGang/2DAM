import re

# Creamos un diccionario vacío para guardar los pares clave-valor (DNI : nombre)
personas = {}

patron_dni = r"^\d{8}-[A-Z]$"
# ^ indica el inicio de la cadena (no debe haber nada antes)
# \d{8} exactamente 8 dígitos numéricos (0-9)
# - un guion literal entre los números y la letra
# [A-Z] una letra mayúscula de la A a la Z
# $ indica el final de la cadena (no debe haber nada después)

print("---- Registro de personas ----\nFormato de DNI válido: 12345678-A\nEscribe 'fin' como DNI para terminar.\n")

# Solicitamos el primer DNI al usuario
dni = input("Introduce el DNI: ").strip()

# Bucle que continúa hasta que el usuario escriba 'fin'
while dni.lower() != "fin":
    if re.match(patron_dni, dni):
        nombre = input("Introduce el nombre de la persona: ").strip()
        personas[dni] = nombre
        print("DNI y nombre añadidos correctamente.\n")
    else:
        print("Formato de DNI inválido. Debe ser del tipo 12345678-A\n")

    dni = input("Introduce el siguiente DNI (o 'fin' para terminar): ").strip()

# Mostramos el contenido final del diccionario
print("\n=== Diccionario final de personas ===")
for k, v in personas.items():
    print(f"{k}: {v}")
