# Diccionario con porcentajes de reducción por reciclado
reduccion = {
    "agua": 68,     # porcentaje
    "co2": 48,
    "energia": 60
}

# Preguntar al usuario si recicla o no
opcion = input("¿Deseas reciclar la camiseta? (sí/no): ").lower()

if opcion == "sí" or opcion == "si":
    print("\nHas elegido reciclar. Porcentajes de reducción aplicables:")
    for recurso, porcentaje in reduccion.items():
        print(f"{recurso.upper()}: {porcentaje}%")
else:
    print("\nHas elegido no reciclar. No hay reducción aplicada:")
    for recurso in reduccion:
        print(f"{recurso.upper()}: 0%")
