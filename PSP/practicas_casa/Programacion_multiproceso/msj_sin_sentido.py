import sys
import asyncio
import random
from multiprocessing import Process, current_process


# NO TOCAR FUNCIONA Y NO SE POR QUE


async def mostrar_mensaje_sin_sentido(num):

    caracteres = [chr(i) for i in range(33, 127)]
    msj = "".join(random.choice(caracteres) for _ in range(30))
    
    pid = current_process().pid

    print(f"\tProceso {num} con PID: {pid}")
    print(f"\t\tMensaje sin sentido {num}: {msj}")

async def main(num):
    pid_padre = current_process().pid
    print(f"Proceso padre con PID: {pid_padre} generando {num} mensajes de 30 caracteres")


    procesos = []
    for i in range(num):
        a = mostrar_mensaje_sin_sentido(i+1)
        procesos.append(a)

    await asyncio.gather(*procesos)

    print(f"Proceso padre con PID {pid_padre}: FIN DEL TRABAJO")
    
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 2

    asyncio.run(main(num))
