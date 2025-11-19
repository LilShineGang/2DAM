# Lista de objetivos de desarrollo sostenible
ods = [
    "Fin de la pobreza",
    "Hambre cero",
    "Salud y bienestar",
    "Educación de calidad",
    "Igualdad de género",
    "Agua limpia y saneamiento"
]

# Agregar un nuevo objetivo a la lista
ods.append("Energía asequible y no contaminante")

# Eliminar un objetivo de la lista
# Usamos remove() para eliminar por valor
ods.remove("Hambre cero")

# Mensaje inicial
print("Lista actualizada de Objetivos de Desarrollo Sostenible:")

# Bucle for para recorrer y mostrar todos los objetivos
for objetivo in ods:
    print(f"- {objetivo}")
