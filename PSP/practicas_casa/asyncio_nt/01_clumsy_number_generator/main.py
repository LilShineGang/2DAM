import sys
import asyncio
import random


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


async def main(n):
    num = []
    for _ in range(n):
        num.append(clumsy_numgen(1, 100))

    numeros = await asyncio.gather(*num)

    r = []
    for n in numeros:
        r.append(str(n))

    resultado = " ".join(r)
    print(f"Numeros generados: {resultado}")



if __name__ == "__main__":
    n = int(sys.argv[1])
    asyncio.run(main(n))
        

