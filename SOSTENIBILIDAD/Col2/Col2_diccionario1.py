# Crear un diccionario
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

# Acceder a un valor por su clave
print(persona["nombre"])    # Ana

# Agregar un nuevo par clave:valor
persona["profesion"] = "Ingeniera"

# Modificar un valor
persona["edad"] = 26

# Eliminar un elemento
del persona["ciudad"]

print(persona)
