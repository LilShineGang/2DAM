# Programa 5: Big Data - Generación de datos para análisis
import csv

# Crean archivo con datos simulados
with open("datos_bigdata.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Ciudad", "Consumo_Kwh"])
    for i in range(1, 6):
        writer.writerow([i, f"Ciudad_{i}", 100 + i * 25])

# Leer y mostran los datos
with open("datos_bigdata.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("=== Datos de consumo eléctrico ===")
    for fila in reader:
        print(fila)
