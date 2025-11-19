import tkinter as tk

root = tk.Tk()
root.title("PREGUNTAS")

tk.Label(root, text="1: ¿Qué beneficios generan los bosques?").pack()
entry1 = tk.Entry(root, width=80)
entry1.pack(padx=10, pady=5)

tk.Label(
    root,
    text="2: ¿Cuáles son las causas de la contaminación de nuestros acuíferos?",
).pack()
entry2 = tk.Entry(root, width=80)
entry2.pack(padx=10, pady=5)

tk.Label(root, text="3: ¿Cuál es la solución propuesta?").pack()
entry3 = tk.Entry(root, width=80)
entry3.pack(padx=10, pady=5)

tk.Label(root, text="4: ¿Qué es la sopa verde?").pack()
entry4 = tk.Entry(root, width=80)
entry4.pack(padx=10, pady=5)

tk.Label(
    root,
    text="5: ¿Qué actividades realizadas por la agroindustria son causantes de este colapso según David Verdiell?",
).pack()
entry5 = tk.Entry(root, width=80)
entry5.pack(padx=10, pady=5)

label_mensaje = tk.Label(root, text="")
label_mensaje.pack(pady=5)


def guardar():
    r1 = entry1.get()
    r2 = entry2.get()
    r3 = entry3.get()
    r4 = entry4.get()
    r5 = entry5.get()

    # w para sobreescribir el archivo cada vez
    try:
        with open("Col9.txt", "w", encoding="utf-8") as f:
            f.write("RESPUESTAS" + "\n\n")

            f.write("1: ¿Qué beneficios generan los bosques?" + "\n")
            f.write("R: " + r1 + "\n\n")

            f.write(
                "2: ¿Cuáles son las causas de la contaminación de nuestros acuíferos?"
                + "\n"
            )
            f.write("R: " + r2 + "\n\n")

            f.write("3: ¿Cuál es la solución propuesta?" + "\n")
            f.write("R: " + r3 + "\n\n")

            f.write("4: ¿Qué es la sopa verde?" + "\n")
            f.write("R: " + r4 + "\n\n")

            f.write(
                "5: ¿Qué actividades realizadas por la agroindustria son causantes de este colapso según David Verdiell?"
                + "\n"
            )
            f.write("R: " + r5 + "\n")

        label_mensaje.config(text="Respuestas guardadas en Col9.txt", fg="green")

    except Exception as e:
        label_mensaje.config(text=f"Error al guardar: {e}", fg="red")


tk.Button(root, text="Guardar Respuestas", command=guardar, width=30).pack(pady=20)

root.mainloop()
