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
import string
import random


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
        print(f"Error: '{path_origin}' is not a file or does not exists")
        return

    path_dest = Path(path_origin.parent, f"copy_{path_origin.name}")

    with open(path_origin, "r") as fo:
        with open(path_dest, "w") as fd:
            while c := fo.read(1):
                if c.lower() not in ("a", "e", "i", "o", "u"):
                    fd.write(c)

# Ejercicio 1:

def count_vowels_in_file():
    response = input("Select a file (path): ")
    path = Path(response)

    if not path.exists() or not path.is_file():
        print(f"Error: '{path}' is not a file or does not exists")
        return

    vowels = "aeiouAEIOU"
    count = 0

    with open(path, "r") as fd:
        content = fd.read()
        for char in content:
            if char in vowels:
                count += 1

    print(f"Number of vowels in the file: {count}")


# Ejercicio 2:

def count_upper_and_lower():
    response = input("Select a file (path): ")
    path = Path(response)

    if not path.exists() or not path.is_file():
        print(f"Error: '{path}' is not a file or does not exists")
        return

    upper_count = 0
    lower_count = 0

    with open(path, "r") as fd:
        content = fd.read()
        for char in content:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1

    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")


# Ejercicio 3: 

def create_random_file():
    filename = input ("Dame un nombre para el archivo: ")
    n_ch = int(input ("Dame el numero de caracteres que quieres que tenga: "))

    path = Path(filename)

    with open (path, 'x') as y:
        for i in range(n_ch):
            random_letter = random.choice(string.ascii_letters)
            y.write(random_letter)

    print(f"El archivo {filename} ha sido creado con {n_ch} caracteres aleatorios.")


def show_menu():
    print("WELCOME TO FILE TOOLS")
    print("________________________________________________________________________________")
    print("1.- Find word in a file")
    print("2.- Copy file without vowels")
    print("3.- Count vowels in a file")
    print("4.- Count uppercase and lowercase letters")
    print("5.- Create file with random characters")
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
        elif option == "3":
            count_vowels_in_file()
        elif option == "4":
            count_upper_and_lower()
        elif option == "5":
            create_random_file()
        else:
            print(f"Error: option '{option}' unknown.")



if __name__ == "__main__":
    main()
