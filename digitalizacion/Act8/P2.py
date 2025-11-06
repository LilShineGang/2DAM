# Programa 2: IoT - Registro de datos de sensores
import csv

# Agregar datos de sensores
with open("datos_sensores.csv", "a+", newline="", encoding="utf-8") as f:
    # newline="" evita que se añada un salto de línea extra tras cada línea
    writer = csv.writer(f)
    # mueve el puntero al principio para leer desde allí
    f.seek(0)
    contenido = f.read()
    # Si el archivo está vacío, agregar encabezado
    if not contenido:
        writer.writerow(["SensorID", "Temperatura", "Unidad"])
    writer.writerow(["S001", "22.5", "C"])
    writer.writerow(["S002", "21.9", "C"])

# Leen los datos
with open("datos_sensores.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("=== Datos de sensores IoT ===")
    for fila in reader:
        print(fila)
