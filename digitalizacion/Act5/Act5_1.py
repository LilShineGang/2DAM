import re

# En expresión regular:
# .  -> representa un punto literal (el carácter ".")
# \. -> se escribe con una barra invertida porque, sin ella, el punto (.) significaría "cualquier carácter"
# -  -> el guion también se permite
# +  -> uno o más de los caracteres anteriores
#
# En resumen: permite letras, números, puntos y guiones.
patron_email = r'^[a-zA-Z0-9\._-]+@[a-zA-Z0-9\.-]+\.[a-zA-Z]+$'

# Solicitar email al usuario
email = input("Introduce tu correo electrónico: ")

# Comprobar si el formato es válido
if re.match(patron_email, email):
    print("\033[92mEl formato del correo electrónico es válido.\033[0m")
else:
    print("\033[91mEl formato del correo electrónico NO es válido.\033[0m")
