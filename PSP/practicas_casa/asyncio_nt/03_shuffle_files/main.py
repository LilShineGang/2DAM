"""TODO

Termina este programa en Python para que baraje de forma asíncrona los ficheros
de texto que se tienen en el directorio pasado por línea de comandos como
entrada al programa.

Para barajar el contenido de los ficheros tienes que ejecutar el script
shuffle_file.py como un subproceso. ¿Cómo? Te lo explico:

- Usa la función create_subprocess_exec del módulo asyncio para lanzar el
  script de forma asíncrona como hemos visto en clase.
- El script shuffle_file.py se tiene que ejecutar de esta manera:

  python shuffle_file.py <fichero> <n>

  donde:
  - <fichero> es la ruta a un fichero a barajar, y
  - <n> es el número de veces que va a barajar el fichero.
"""























'''
import sys
import asyncio
from pathlib import Path
from shuffle_file import shuffle_file


async def shuffle_file(path: str) -> None:

  proceso = await asyncio.create_subprocess_exec("python", "shuffle_file.py", str(path), "10")
  await proceso.wait()

async def main(directory: Path) -> None:
    tasks = []
    for f in directory.iterdir():
        if f.is_file():
            tasks.append(shuffle_file(f))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    directory = Path(sys.argv[1])
    if directory.is_dir():
        asyncio.run(main(directory))
'''