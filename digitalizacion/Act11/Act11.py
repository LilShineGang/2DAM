import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Ejemplo de uso de place en Tecnologías Habilitadoras Digitales Emergentes")
root.geometry("600x600")

# LABEL 1
img1 = ImageTk.PhotoImage(Image.open("images/imgNanotecnología.png"))
label1 = tk.Label(root, image=img1)
label1.place(relx=0.05, rely=0.05, anchor="nw")

# LABEL 2
img2 = ImageTk.PhotoImage(Image.open("images/imgBiotecnología.png"))
label2 = tk.Label(root, image=img2)
label2.place(relx=0.50, rely=0.05, anchor="n")

# LABEL 3
img3 = ImageTk.PhotoImage(Image.open("images/imgMateriales.png"))
label3 = tk.Label(root, image=img3)
label3.place(relx=0.95, rely=0.05, anchor="ne")

# LABEL 4
img4 = ImageTk.PhotoImage(Image.open("images/imgMicro.png"))
label4 = tk.Label(root, image=img4)
label4.place(relx=0.15, rely=0.95, anchor="sw")

# LABEL 5
img5 = ImageTk.PhotoImage(Image.open("images/imgFotonica.png"))
label5 = tk.Label(root, image=img5)
label5.place(relx=0.60, rely=0.95, anchor="s")

# LABEL 6
img6 = ImageTk.PhotoImage(Image.open("images/imgTecnologías.png"))
label6 = tk.Label(root, image=img6)
label6.place(relx=1.05, rely=0.95, anchor="se")

root.mainloop()










