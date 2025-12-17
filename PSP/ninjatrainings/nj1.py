'''
En esta práctica vas a escribir un programa donde varios procesos van a competir
por registrar a sus usuarios.
El programa está diseñado para gestionar la lectura de múltiples ficheros de texto
que se encuentran en un directorio específico. Cada fichero contiene nombres de
usuario, uno en cada línea. A continuación, el programa ejecuta los siguientes pasos:
1. Lee todos los ficheros de texto del directorio especificado y crea un proceso
por cada fichero encontrado.
2. Cada proceso es responsable de abrir su respectivo fichero, leer los nombres
de usuario línea por línea, y agregar estos nombres a un Array compartido de
tamaño 10, que almacena los nombres de usuario.
3. Para garantizar que los accesos al Array compartido sean seguros y evitar
condiciones de carrera, se implementa un lock. Este lock permite que solo un
proceso acceda al Array a la vez, asegurando una inserción correcta de los
nombres de usuario.
4. Se utilizará un contador compartido para rastrear en qué posición del Array se
están insertando los nombres. Este contador incrementa su valor a medida que
cada nombre es añadido.
5. Al finalizar la ejecución de todos los procesos, el proceso padre imprimirá en
pantalla la lista completa de los nombres de usuario que se han registrado en
el Array compartido.
'''





from multiprocessing import Process, current_process, Semaphore, Array, Value, Lock
import multiprocessing
from time import sleep, time
from random import randint
from pathlib import Path

carpeta = Path('./usuarios')
max_users = 10 # 2

def ficheros():
    carpeta.mkdir(exist_ok=True)
    (carpeta / 'u1.txt').write_text('dan\nbob\ncharlie\n')
    (carpeta / 'u2.txt').write_text('eve\nfrank\ngrace\n')
    (carpeta / 'u3.txt').write_text('elliot\njudy\nmallory\n')

def proceso(archivo_path):
    nombre_proceso = multiprocessing.current_process().name
    print(f'[{nombre_proceso}] Leyendo archivo: {archivo_path.name}')
    sleep(1)

    with open(archivo_path, 'r') as f:
        for linea in f:
            usuario = linea.strip()
            if not usuario: continue
            
if __name__ == '__main__':
    ficheros()

    print(f"\n--- Buscando ficheros en {carpeta.absolute()} ---\n")

    procesos = []

    for archivo in carpeta.glob("*.txt"):
        p = multiprocessing.Process(target=proceso, args=(archivo,))
        p.start()
        procesos.append(p)

    for p in procesos:
        p.join()

    print("\n--- Todos los procesos han sido lanzados y han terminado ---\n")







