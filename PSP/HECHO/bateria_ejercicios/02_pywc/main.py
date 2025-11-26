"""PyWC: versión escrita en Python del comando wc.

El comando wc, de GNU/Linux, muestra por pantalla el número de caracteres,
palabras y líneas que hay en un fichero dado. Se usa tal que así, por ejemplo:

$ wc ~/Documentos/fichero.txt

Lo puedes probar tú mism@.

En este ejercicio te propongo que escribas tu versión de wc en Python.

El programa recibe un argumento por línea de comandos que tiene que ser una
ruta al fichero a analizar y mostrará por pantalla algo así:

Número de caracteres: 1895
Número de palabras: 790
Número de líneas: 34

En Python puedes obtener los argumentos que se pasan por la línea de comandos
de muchas maneras. La más sencilla es usando el módulo sys como en este
ejemplo:

_______________________________________________________________________________
import sys


print(f"Arguments count: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
    print(f"Argument {i:>6}: {arg}")
_______________________________________________________________________________

Así que si quieres obtener el nombre del programa puedes usar:
sys.argv[0]

Y si quieres obtener el primer argumento:
sys.argv[1]
"""

# TODO Escribe aquí tu programa...

import sys

# Verificar que se haya proporcionado un argumento
if len(sys.argv) < 2:
    print("Error: Debes proporcionar la ruta de un fichero.")
    print("Uso: python main.py <ruta_del_fichero>")
    print("Ejemplo: python main.py ../01_file_tools/main.py")
    sys.exit(1)

# Obtener la ruta del fichero desde los argumentos
ruta_fichero = sys.argv[1]

# Abrir y leer el fichero
with open(ruta_fichero, 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()

# Contar caracteres
num_caracteres = len(contenido)

# Contar palabras (dividiendo el texto por espacios en blanco)
num_palabras = len(contenido.split())

# Contar líneas (dividiendo el texto por saltos de línea)
num_lineas = len(contenido.splitlines())

# Mostrar los resultados
print(f"Número de caracteres: {num_caracteres}")
print(f"Número de palabras: {num_palabras}")
print(f"Número de líneas: {num_lineas}")
