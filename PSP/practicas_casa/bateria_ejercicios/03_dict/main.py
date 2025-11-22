"""Colecciones en Python.

En el fichero data.py tienes definida una lista de diccionarios con información
relativa a varias imágenes de Docker (resultado de ejecutar docker image
inspect).

Completa el programa con los mensajes TODO que hay en este fichero fuente.
"""
from data import students
from data import images


# TODO Añade información sobre la edad
for num, student in students.items():
    print(f"{num}: {student['name']}")


# TODO Calcula y muestra por pantalla la media de edad de los estudiantes que
#      hay en el diccionario students. El resultado deberá ser un número real.


# TODO Muestra por pantalla la nota media de cada estudiante que hay en el
#      diccionario students. La nota media será un número real. La salida
#      tendrá este formato: "<nombre>: <nota media>". Por ejemplo:
#      Alice: 7.85


# TODO Añade el tamaño de la imagen a la información que se muestra aquí.
for image in images:
    image_id = image["Id"]
    image_created = image["Created"]
    print(f"Image {image_id} created at {image_created}")


# TODO Escribe un bucle for para mostrar, por imagen, todas las variables de
#      entorno que se usan (dadas por la clave "Env" que hay dentro de "Config").



# TODO Escribe un bucle for para recorrer todos los elementos de la lista
#      y mostrar, por cada diccionario:
#
#      Imagen número <NÚMERO DE ELEMENTO EN LA LISTA>
#      Capas:
#            sha256:607ddfe5f3c3f9e9df2b45f6275ad18bc76e49fdebcf0777c1c02c66f5012956
#            sha256:0dd5860cbc60e77cc364ce36be1a9055d4139f2123324e14f756af1af719ffb0
#            sha256:08e14ec5b7497da231d70d47d1d80440ba7d9997d43c0796a8394923bbc98183
#            sha256:a9410d27207aec98b812b3d965ca2e03275f827993d34d4c0d13626efbe30415
#            sha256:d52ca6ce2fa3c9595355a8a2519d36919e3414dc002d47aa8fcadeac1fdb8b74
#            sha256:bafcf71d651a5230ebe9650cbcb4f874a7536f246844a2509f1118f6cde243bc
