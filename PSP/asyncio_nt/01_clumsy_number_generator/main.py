import sys
import asyncio
import random
from unittest import result


async def clumsy_numgen(start: int, end: int) -> int:
    res = random.randint(start, end)
    await asyncio.sleep(res % 3)
    return res


###############################################################################
#
# TODO
#
# Escribe un programa en Python que genere números aleatorios entre 1 y 100
# llamando a la corrutina clumsy_numgen definida arriba.
#
# Este programa recibirá por línea de comandos la cantidad de números que se
# tienen que generar.
#
# Asegúrate que se generan los números de forma asíncrona y no síncrona.
#
# Ejemplo de uso con resultado por salida estándar:
#     $ python main.py 3
#     Números generados: 73, 82, 71
#
###############################################################################


async def main2(count: int) -> None:
    num_numbers = int(sys.argv[1])
    numbers = await asyncio.gather(*[clumsy_numgen(1, 100) for _ in range(num_numbers)])
    print(f"Numero/s generados: {', '.join(map(str, numbers))}")


async def main(count: int) -> None:
    tasks = []

    print("Numero/s aleatorios: ", end="")
    for _ in range(count):
        tasks.append(asyncio.create_task(clumsy_numgen(1, 100)))

    for t in tasks:
        result = await t
        print(result, end="")

    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Error: usage: python {sys.argv[0]} <count>")
        exit(1)

    count = int(sys.argv[1])
    asyncio.run(main(count))
    asyncio.run(main2(count))
