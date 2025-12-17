import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de uso de place en Actividades Industriales")
root.geometry("900x400")

label_title = tk.Label(root, text="C) ACTIVIDADES GANADERAS", bg="#CCCCCC", font=("Arial", 12))
label_title.place(relx=0.7, rely=0.1, anchor="e")

label_1 = tk.Label(root, text="Emisión de gases de efecto invernadero", bg="#CCCCCC", font=("Arial", 11))
label_1.place(relx=0.1, rely=0.3, anchor="w")

label_2 = tk.Label(root, text="Deforestación y pérdida de biodiversidad", bg="#CCCCCC", font=("Arial", 11))
label_2.place(relx=0.2, rely=0.6, anchor="w")

label_3 = tk.Label(root, text="Degradación del suelo debido a la actividad ganadera", bg="#CCCCCC", font=("Arial", 11))
label_3.place(relx=0.5, rely=0.8, anchor="n")

root.mainloop()
