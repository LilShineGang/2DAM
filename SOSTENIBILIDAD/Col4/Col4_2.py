import re

enlaces = {}
patron = r"^https://acortar\.link/[A-Za-z0-9]{5,6}$"

print("--- Completar diccionario llamado enlaces ---")
print("Introduce claves con el formato: https://acortar.link/Fb05iF")
print("Escribe 'fin' para terminar.\n")

clave = input("Introduce la clave: ").strip()

while clave.lower() != "fin":
    # Validar con expresión regular
    if re.match(patron, clave):
        valor = input("Introduce el valor para esta clave: ")
        enlaces[clave] = valor
        print("Clave y valor añadidos correctamente.\n")
    else:
        print("Clave inválida. Debe tener el formato: https://acortar.link/XXXXX\n")

    clave = input("Introduce la siguiente clave (o 'fin' para terminar): ").strip()

print("\n--- Diccionario final ---")
for k, v in enlaces.items():
    print(f"{k}: {v}")

    print(f"{k}: {v}")



# Cuestión 1: Busca en Internet por qué se debe poner en el patrón la barra de escape \ antes del punto.
# Por que son expresiones regulares, el punto es un metacaracter que coincide con cualquier caracter. 
# Para que coincida literalmente con un punto (es decir, “.”), debes escaparlo con \. para desactivar su significado especial. 


# Cuestión 2: Busca en la web qué hace la función strip() aplicada a una cadena de texto.
# La función strip() aplicada a una cadena elimina los caracteres de espacio en blanco (por defecto: espacios, tabulaciones, saltos de línea) al inicio y al final de la cadena.


# Cuestión 3: Busca en Internet qué hace la función items() aplicada al diccionario.
# El método items() de un diccionario retorna una vista (dict_items) que contiene pares (clave, valor) del diccionario como tuplas. Permite iterar sobre ambos al mismo tiempo.
