import tkinter as tk

root = tk.Tk()
root.title("Blagovest Doukov Dimitrova") 
root.geometry("600x300")

# Frames externos
izq = tk.Frame(root, bg="darkgray", padx=10, pady=10)
der = tk.Frame(root, bg="lightgray", padx=10, pady=10)
izq.pack(side="left", expand=True, fill="both")
der.pack(side="left", expand=True, fill="both")

# Textos para las etiquetas de la izquierda
textos_izquierda = (
    "Ecodiseño:\n- Diseño ambientalmente responsable.\n- Materiales sostenibles.",
    "Extensión de la vida del producto:\n- Alargar vida útil.\n- Reducir desperdicios.",
    "Simbiosis industrial:\n- Intercambio de procesos.\n- Colaboración empresarial."
)

# Textos para las etiquetas de la derecha
textos_derecha = (
    "Cadena de suministro sostenible:\n- Materiales reciclables.\n- Integración de biodegradables.",
    "Producto como servicio:\n- Servicio en lugar de producto.\n- Uso compartido.",
    "Reciclado y reconversión:\n- Generar energía.\n- Materias primas para nuevos productos."
)

# --- COLUMNA IZQUIERDA ---

# Frame 1 Izquierdo (Rosa)
f1 = tk.Frame(izq, bg="#FFA6FF", padx=10, pady=10)
f1.pack(expand=True, fill="both")
l1 = tk.Label(f1, text=textos_izquierda[0], justify="center")
l1.pack()

# Frame 2 Izquierdo (Verde)
f2 = tk.Frame(izq, bg="#B8F1C9", padx=10, pady=10)
f2.pack(expand=True, fill="both")
l2 = tk.Label(f2, text=textos_izquierda[1], justify="center")
l2.pack()

# Frame 3 Izquierdo (Naranja)
f3 = tk.Frame(izq, bg="#FFB98A", padx=10, pady=10)
f3.pack(expand=True, fill="both")
l3 = tk.Label(f3, text=textos_izquierda[2], justify="center")
l3.pack()


# --- COLUMNA DERECHA ---

# Frame 4 Derecho (Verdde)
f4 = tk.Frame(der, bg="#B8F1C9", padx=10, pady=10)
f4.pack(expand=True, fill="both")
l4 = tk.Label(f4, text=textos_derecha[0], justify="center")
l4.pack()

# Frame 5 Derecho (Rosa)
f5 = tk.Frame(der, bg="#FFA6FF", padx=10, pady=10)
f5.pack(expand=True, fill="both")
l5 = tk.Label(f5, text=textos_derecha[1], justify="center")
l5.pack()

# Frame 6 Derecho (Naranja)
f6 = tk.Frame(der, bg="#FFB98A", padx=10, pady=10)
f6.pack(expand=True, fill="both")
l6 = tk.Label(f6, text=textos_derecha[2], justify="center")
l6.pack()

root.mainloop()