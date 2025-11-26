import tkinter as tk

root = tk.Tk()
root.title("Ejemplo grid básico de Blagovest Doukov Dimitrova")
root.geometry("900x400")

# ----- Frame superior -----
frame_superior = tk.Frame(root, bg="white")
frame_superior.pack(fill="both", pady=10)

temasRetosAmbientales = [
    "RETOS AMBIENTALES",
    "Cambio climático",
    "Gestión de residuos",
    "Contaminación",
    "Transición energética y energías renovables",
    "Protección de la biodiversidad",
    "Protección de los recursos hídricos",
    "Modelos de alimentación sostenible",
    "Desarrollo urbano y movilidad sostenible"
]

# Crear etiquetas en malla 3x3
fila = 0
columna = 0

for texto in temasRetosAmbientales:
    etiqueta = tk.Label(frame_superior, text=texto,
                        bg="lightgreen", font=("Arial", 11),
                        padx=10, pady=10)
    etiqueta.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
    
    frame_superior.grid_columnconfigure(columna, weight=1)

    columna += 1
    if columna == 3:  # cuando llega a 3 columnas -> pasa a la fila siguiente
        columna = 0
        fila += 1

# ----- Frame inferior -----
frame_inferior = tk.Frame(root, bg="white")
frame_inferior.pack(fill="both", pady=10)

# Lista de retos sociales
temasRetosSociales = [
    "RETOS SOCIALES",
    "Fin de la pobreza y desigualdad",
    "Educación de calidad",
    "Salud y bienestar",
    "Igualdad de género",
    "Trabajo decente y crecimiento"
]

# Reiniciamos contadores para la nueva malla
fila = 0
columna = 0

for texto in temasRetosSociales:
    # Usamos un color diferente para distinguir los retos sociales
    etiqueta = tk.Label(frame_inferior, text=texto,
                        bg="lightblue", font=("Arial", 11),
                        padx=10, pady=10)
    etiqueta.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

    # Configuración para las columnas
    frame_inferior.grid_columnconfigure(columna, weight=1)

    fila += 1
    if fila == 3:  # Malla 2x3
        fila = 0
        columna += 1

root.mainloop()