# Programa 3: Infraestructuras 5G - Medición de velocidad

# Se importa desde la librería openpyxl dos clases/funciones:
# Workbook: para crear un nuevo libro de Excel (.xlsx).
# load_workbook: para abrir...leer un archivo .xlsx ya existente.
from openpyxl import Workbook, load_workbook

# Crear archivo con datos de pruebas
wb = Workbook()
ws = wb.active  # se toma la hoja activa por defecto
ws.title = "Pruebas5G"

ws.append(["Zona", "Velocidad (Mbps)"])
ws.append(["Centro", 1200])
ws.append(["Periferia", 850])
ws.append(["Aeropuerto", 950])

wb.save("redes5G.xlsx")

# Leer archivo generado
wb2 = load_workbook("redes5G.xlsx")
ws2 = wb2.active
print("=== Velocidades registradas ===")
# iter_rows devuelve tuplas con los valores de cada celda
for fila in ws2.iter_rows(values_only=True):
    print(fila)
