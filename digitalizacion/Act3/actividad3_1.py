# Diccionario con empleados y sus correos
empleados = {
    "Ana": "ana.garcia@empresa.com",
    "Luis": "luis.martinez@empresa.com",
    "Marta": "marta.lopez@empresa.com",
    "Carlos": "carlos.sanchez@empresa.com"
}

# Mostrar los nombres disponibles
print("Empleados disponibles:")
for nombre in empleados.keys():
    print("-", nombre)

# Pedir al usuario el nombre
nombre = input("\nIntroduce el nombre del empleado: ")

# Buscar en el diccionario
if nombre in empleados:
    print(f"El correo de {nombre} es: {empleados[nombre]}")
else:
    print("Empleado no encontrado.")
