"""Set of Python problems: working with files in Python.

En este fichero tienes un programa escrito en Python con un menú.

Pruébalo, léelo y asegúrate que entiendes perfectamente cada línea de código
fuente.

A partir de ahí, añade las siguientes tareas (que te doy en inglés):

TODO Añade una opción para contar el número de vocales en el fichero.
TODO Añade una opción para contar el número de minúsculas y mayúsculas.
TODO Añade una opción para crear un fichero con N bytes de caracteres aleatorios.
     Puedes generar caracteres aleatorios con dos librerías: string y random.
     Ejemplo de uso:
     import string
     import random
     random_letter = random.choice(string.ascii_letters)
     print(random_letter)
"""
from pathlib import Path


def find_word_in_a_file():
    response = input("Select a file (path): ")
    path = Path(response)

    if not path.exists() or not path.is_file():
        print(f"Error: '{path}' is not a file or does not exists")
        return

    word = input("Word to find: ").split(" ")[0]

    print(f"Looking for '{word}' into '{path}' file...")

    lino = 0
    with open(path, "r") as fd:
        for line in fd.readlines():
            lino += 1
            for i, w in enumerate(line.split()):
                if word == w:
                    print(f"Line {lino}, word {i + 1}")
            

def copy_file_without_vowels():
    origin = input("Select a file (path): ")
    path_origin = Path(origin)

    if not path_origin.exists() or not path_origin.is_file():
        print(f"Error: '{path}' is not a file or does not exists")
        return

    path_dest = Path(path_origin.parent, f"copy_{path_origin.name}")

    with open(path_origin, "r") as fo:
        with open(path_dest, "w") as fd:
            while c := fo.read(1):
                if c.lower() not in ("a", "e", "i", "o", "u"):
                    fd.write(c)


def show_menu():
    print("WELCOME TO FILE TOOLS")
    print("________________________________________________________________________________")
    print("1.- Find word in a file")
    print("2.- Copy file without vowels")
    print("0.- Exit")


def main():
    while True:
        show_menu()
        option = input("Select an option: ")

        if option == "0":
            print("See you soon")
            break

        if option == "1":
            find_word_in_a_file()
        elif option == "2":
            copy_file_without_vowels()
        else:
            print(f"Error: option '{option}' unknown.")



if __name__ == "__main__":
    main()
