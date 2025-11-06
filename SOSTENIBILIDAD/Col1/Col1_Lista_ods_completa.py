# Col1_Lista_ods_completa.py
# Lista de objetivos de desarrollo sostenible
ods = [
    "Fin de la pobreza",
    "Hambre cero",
    "Salud y bienestar",
    "Educación de calidad",
    "Igualdad de género",
    "Agua limpia y saneamiento"
]

# Agregar el resto de los ODS con append hasta completar los 17
ods.append("Energía asequible y no contaminante")
ods.append("Trabajo decente y crecimiento económico")
ods.append("Industria, innovación e infraestructura")
ods.append("Reducción de las desigualdades")
ods.append("Ciudades y comunidades sostenibles")
ods.append("Producción y consumo responsables")
ods.append("Acción por el clima")
ods.append("Vida submarina")
ods.append("Vida de ecosistemas terrestres")
ods.append("Paz, justicia e instituciones sólidas")
ods.append("Alianzas para lograr los objetivos")

# Mensaje inicial
print("Lista completa de Objetivos de Desarrollo Sostenible (ONU 2015):")

# Bucle for para recorrer y mostrar todos los objetivos
for i, objetivo in enumerate(ods, start=1):
    print(f"{i}. {objetivo}")
