"""Contador de segundos con fecha y hora.

Escribe un programa que ejecute dos corrutinas de forma asíncrona durante
20 segundos. Tras llegar a estos 20 segundos se cancelarán las corrutinas.
Estas corrutinas son:

- Una corrutina mostrará en un bucle infinito los segundos.
- Una segunda corrutina mostrará el día y la hora indefinidamente cada cinco
  segundos.

Para mostrar el día y la hora puedes usar el módulo datetime de Python:

from datetime import datetime
print(datetime.now())

Esta sería la salida esperada:

0
2025-10-23 17:37:33.163444
1
2
3
4
2025-10-23 17:37:38.165262
5
6
7
8
9
2025-10-23 17:37:43.166825
10
11
12
13
14
2025-10-23 17:37:48.168843
15
16
17
18
19
"""
