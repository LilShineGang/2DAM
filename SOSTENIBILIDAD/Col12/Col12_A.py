import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de uso de place en Actividades Industriales")
root.geometry("900x400")

# Etiqueta superior
label_title = tk.Label(root, text="A) ACTIVIDADES INDUSTRIALES", bg="#C1BBDD", font=("Arial", 12))
label_title.place(relx=0.3, rely=0.1, anchor="center")

# Etiqueta derecha
label_1 = tk.Label(root, text="Las emisiones de gases de efecto invernadero", bg="#C1BBDD", font=("Arial", 11))
label_1.place(relx=1.0, rely=0.2, anchor="e")

# Etiqueta izquierda
label_2 = tk.Label(root, text="La contaminación del agua y del aire", bg="#C1BBDD", font=("Arial", 11))
label_2.place(relx=0.2, rely=0.5, anchor="w")

# Etiqueta central
label_3 = tk.Label(root, text="La generación de residuos tóxicos", bg="#C1BBDD", font=("Arial", 11))
label_3.place(relx=0.5, rely=0.7, anchor="center")

# Etiqueta inferior
label_4 = tk.Label(root, text="La degradación de los ecosistemas", bg="#C1BBDD", font=("Arial", 11))
label_4.place(relx=0.0, rely=0.9, anchor="w")

root.mainloop()

