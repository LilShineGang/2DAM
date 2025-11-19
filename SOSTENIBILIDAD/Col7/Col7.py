# -----------------------------------------------------------------------------
# Ejercicio 1 - ¿Qué es el efecto invernadero?
#
# a) ¿Qué tres gases constituyen el 99,93% de los gases de la atmósfera?
#    Nitrógeno (N2), Oxígeno (O2) y Argón (Ar)
#
# b) ¿Qué cinco gases son los principales causantes del efecto invernadero?
#    Dióxido de carbono (CO2), Metano (CH4), Óxido nitroso (N2O),
#    Ozono (O3) y Vapor de agua (H2O)
# -----------------------------------------------------------------------------
# Ejercicio 2
# Programa: Validación de respuestas sobre el Acuerdo de París
# try = intenta ejecutar código que puede fallar
# except = captura el error si ocurre
# raise = lanza un error manualmente
# ValueError = error cuando el valor es del tipo correcto pero no válido
# FileNotFoundError = error cuando no se encuentra un archivo
# -----------------------------------------------------------------------------

print("Cuestionario sobre el Acuerdo de París\n")

# a) Año (entero)
try:
    año = int(input("a) ¿En qué año tuvo lugar el Acuerdo de París? (ejemplo: 2015): "))
except ValueError:
    print("Debes introducir un número entero válido (ejemplo: 2015).")
    año = None

# b) Temperatura (decimal con punto)
try:
    temperatura = float(
        input(
            "b) ¿Qué valor de temperatura se marcó para mantenerla por debajo de 2? (ejemplo: 1.5): "
        )
    )
except ValueError:
    print("Debes introducir un número decimal con punto (ejemplo: 1.5).")
    temperatura = None

# c) Reducción de emisiones (texto)
try:
    reduccion = input(
        "c) ¿Qué reducción en las emisiones debe realizarse? (ejemplo: 45%): "
    ).strip()
    if not reduccion:
        raise ValueError("La respuesta no puede estar vacía.")
except ValueError as e:
    print(e)
    reduccion = None

# d) Gases de efecto invernadero (lista separada por comas)
try:
    gases = input(
        "d) Indica los gases de efecto invernadero separados por coma (ejemplo: CO2, CH4, N2O): "
    ).strip()
    if "," not in gases:
        raise ValueError(
            "Debes separar los elementos con comas (ejemplo: CO2, CH4, N2O)."
        )
except ValueError as e:
    print(e)
    gases = None

# e) Ubicación o ruta de un archivo txt
try:
    ruta_archivo = input(
        "e) Introduce la ruta de un archivo .txt sobre el Acuerdo de París: "
    ).strip()
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("No se encontró el archivo en la ruta indicada.")
    ruta_archivo = None
    contenido = None
