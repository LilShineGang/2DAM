# Programa 1: Aplicaciones móviles - Reseñas de turistas
# Crea y lee reseñas en un archivo de texto

# Escribir reseñas de usuarios
with open("turismo_app.txt", "w", encoding="utf-8") as f:
    f.write("Usuario: Ana - Opinión: Excelente experiencia en la app de rutas\n")
    f.write("Usuario: Luis - Opinión: Buena interfaz y mapas útiles\n")

# Leen las reseñas guardadas
with open("turismo_app.txt", "r", encoding="utf-8") as f:
    print("=== Reseñas de usuarios ===")
    for linea in f:
        print(linea.strip())
