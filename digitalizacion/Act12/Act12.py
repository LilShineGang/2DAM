import tkinter as tk

root = tk.Tk()
root.title("Actividad 12 - Blago")
root.geometry("800x600")


# LABEL 1 (Rojo)
label1 = crear_label("Label 1", "red")
label1.place(relx=0.98, rely=0.02, anchor="ne")

# LABEL 2 (Azul claro)
label2 = crear_label("Label 2", "#008fca")
label2.place(relx=0.44, rely=0.18, anchor="se")

# LABEL 3 (Naranja)
label3 = crear_label("Label 3", "#ff7f27")
label3.place(relx=0.20, rely=0.26, anchor="n")

# LABEL 4 (Morado)
label4 = crear_label("Label 4", "purple")
label4.place(relx=0.50, rely=0.46, anchor="e")

# LABEL 5 (Verde)
label5 = crear_label("Label 5", "green")
label5.place(relx=0.50, rely=0.54, anchor="nw")

# LABEL 6 (Azul oscuro)
label6 = crear_label("Label 6", "blue")
label6.place(relx=0.24, rely=0.76, anchor="s")

# LABEL 7 (Marrón)
label7 = crear_label("Label 7", "#885016")
label7.place(relx=0.70, rely=0.84, anchor="s")

# LABEL 8 (Negro)
label8 = crear_label("Label 8", "black")
label8.place(relx=0.32, rely=0.96, anchor="sw")

root.mainloop()
