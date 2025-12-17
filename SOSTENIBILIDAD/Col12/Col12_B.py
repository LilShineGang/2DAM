import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de uso de place en Actividades Agrícolas")
root.geometry("900x400")

# Etiqueta superior
label_top = tk.Label(root, text="B) ACTIVIDADES AGRÍCOLAS", bg="lightblue")
label_top.place(relx=0.5, rely=0.1, anchor="center")
# anchor="center" -> ubica el centro del widget en ese punto

# Etiqueta izquierda
label_left = tk.Label(root, text="Uso excesivo de pesticidas y ferilizantes", bg="lightgreen")
label_left.place(relx=0.1, rely=0.5, anchor="w")

# Etiqueta derecha
label_right = tk.Label(root, text="Deforestación para la expansión de tierras de cultivo", bg="lightyellow")
label_right.place(relx=0.95, rely=0.5, anchor="e")

# Etiqueta inferior
label_bottom = tk.Label(root, text="Contaminación del agua y del suelo", bg="lightcoral")
label_bottom.place(relx=0.4, rely=0.8, anchor="nw")

# Etiqueta central superior
label_center = tk.Label(root, text="La pérdida de biodiversidad", bg="lightgray")
label_center.place(relx=0.5, rely=0.4, anchor="center")
# anchor="center" -> ubica el centro del widget en ese punto

# Etiqueta central supeinferiorrior
label_center = tk.Label(root, text="Erosión del suelo", bg="lightgray")
label_center.place(relx=0.5, rely=0.6, anchor="center")
# anchor="center" -> ubica el centro del widget en ese punto

root.mainloop()
