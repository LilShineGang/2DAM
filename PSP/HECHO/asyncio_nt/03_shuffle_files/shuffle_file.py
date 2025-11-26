import sys


def shuffle_file(path: str, n: int) -> None:
    """Baraja el contenido de un fichero generando uno nuevo.

    De forma bastante ineficiente, lo que hace esta función es leer el fichero
    path y rota hacia la derecha los caracteres n veces.

    El resultado lo guarda en un fichero en el mismo lugar y nombre acabado en
    .s.

    Imprime por pantalla mensajes con la información necesaria para saber
    cuándo comenzó a procesar el fichero y cuándo terminó.
    """
    print(f"[START] Shuffling file {path} {n} times -------------------------")
    with open(path, "r") as fr:
        text = fr.read()

        for _ in range(n):
            with open(f"{path}.s", "w") as fw:
                text = text[1:] + text[0]
                fw.write(text)
    print(f"[END]   Shuffling file {path} {n} times -------------------------")


if __name__ == "__main__":
    shuffle_file(sys.argv[1], int(sys.argv[2]))
