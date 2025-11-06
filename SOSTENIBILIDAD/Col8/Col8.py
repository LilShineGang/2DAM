# Decimos que nombre queremos que tenga el archivo
archivo_nombre = "Col8.txt"

preguntas_respuestas = [
    (
        "1a. ¿Qué son las energías renovables?",
        "\nSon fuentes de energía limpias, inagotables y competitivas que se obtienen de fuentes naturales que no contribuyen al calentamiento global.",
    ),
    (
        "1b. ¿Cuáles son las 5 fuentes de energía renovable más utilizada?",
        "\nEólica, solar, hidroeléctrica, biomasa y geotérmica.",
    ),
    (
        "2a. ¿Qué es la energía geotérmica?",
        "\nEs un tipo de energía renovable que se obtiene aprovechando el calor interno de la Tierra.",
    ),
    (
        "2b. ¿Cuáles son las principales ventajas y desventajas de esta fuente de energía?",
        "\nVentajas: Es un recurso renovable, fiable y predecible. \nDesventajas: Requiere ubicaciones geográficas muy específicas y no es transportable.",
    ),
    (
        "3a. ¿Qué países cuentan con centrales mareomotrices?",
        "\nFrancia, Corea del Sur, Canadá, China y Reino Unido.",
    ),
    (
        "3b. ¿Cuál es la principal ventaja de esta fuente de energía?",
        "\nSu principal ventaja es la previsibilidad siendo una fuente constante ya que las mareas siguen patrones regulares y predecibles.",
    ),
]

# Abrimos el archivo en modo escritura
with open(archivo_nombre, "w", encoding="utf-8") as archivo:
    archivo.write("Preguntas y respuestas sobre energías renovables:\n\n")

    for pregunta, respuesta in preguntas_respuestas:
        archivo.write(f"{pregunta}\nRespuesta: {respuesta}\n\n")

print(f"El archivo '{archivo_nombre}' ha sido creado con éxito.")

# Leemos y mostramos el contenido del archivo por terminal
print("\n--- Contenido del archivo Col8.txt ---")
with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)
