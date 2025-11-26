import tkinter as tk

root = tk.Tk()
root.title("Tecnologías Disruptivas de Blagovest Doukov Dimitrova")
root.geometry("900x450")

# ----- Frame principal -----
frame = tk.Frame(root, bg="white")
frame.pack(expand=True, fill="both", pady=10)

# Lista de textos completada con los ejemplos de la imagen
tecnologias = [
    "REALIDAD AUMENTADA Y VIRTUAL\nEntretenimiento y juegos\nFormación virtual\nMedicina virtual",
    "COMPUTACIÓN EN LA NUBE\nAlmacenamiento en la nube\nSoftware como servicio\nInfraestructura como servicio",
    "BLOCKCHAIN\nFinanzas descentralizadas\nTrazabilidad en la cadena de suministro\nContratos inteligentes",
    "REDES 5G\nTelecomunicaciones\nOcio multimedia\nVehículos inteligentes",
    "INTELIGENCIA ARTIFICIAL\nAutomatización industrial\nSalud digital\nAsistentes virtuales",
    "INTERNET DE LAS COSAS\nCiudades inteligentes\nHogar conectado\nAgricultura inteligente",
    "BIG DATA\nAnálisis empresarial\nSalud predictiva\nPublicidad personalizada",
    "IMPRESIÓN 3D\nIngeniería y diseño industrial\nSector médico"
]

# Lista de colores de fondo
colores = [
        "#FAF0FF", "#FFECEB",
        "#E3FFF2", "#E8F8FF",
        "#FFF2E5", "#E3FFF2",
        "#F3F0FF", "#FEEBF7"
        ]


# Crear etiquetas en grid 4 filas x 2 columnas
fila = 0
columna = 0

for i, texto in enumerate(tecnologias):
    
    etiqueta = tk.Label(frame, text=texto,
                        bg=colores[i], font=("Arial", 11),
                        padx=10, pady=10)
    
    etiqueta.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
    # sticky norte, sur, este, oeste hace que cada etiquete se pegue a los 4 lados de su celda

    columna += 1
    if columna == 2:  # Cuando llega a la 2ª columna -> pasa a la siguiente fila
        columna = 0
        fila += 1

# Configurar columnas para que se expandan uniformemente [cite: 10]
for c in range(2):
    frame.grid_columnconfigure(c, weight=1, uniform="col")
    # hace que cada columna se expanda proporcionadamente y todas tengan el mismo ancho


# Configurar filas para que se expandan uniformemente [cite: 10]
for r in range(4):
    frame.grid_rowconfigure(r, weight=1, uniform="row")
    # hace que cada fila se expanda proporcionadamente y todas tengan la misma altura

root.mainloop()



