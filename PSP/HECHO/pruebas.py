# numbers = [2, 4, 5, 1, 7] # Variable tipo "list"
# numbers = [10] + numbers # Ponemos delante el elemento numero 10

# Aceptan las listas cualquier tipo de elemento por defecto:

# Añadir una cadena de texto a la lista: numbers = ["hola"] + numbers
# Añadir una cadena de numeros a la lista: numbers =[[2, 3, 4]] + numbers
# numbers.append(adios)

# Mostrar todos los elementos: print (numbers)
# Mostrar el quinto elemento de la lista: print(numbers[4])
# Mostrar el numero de elementos que hay en la lista: print(f"Numero de items: {len(numbers)}")

# Modificar elementos de la lista (por elemplo el quinto): del numbers[4] numbers[0] = 1 


# last = numbers.pop()
# print(f"El ultimo elemento era {last} y ahora hay = {numbers}")

# numbers = numbers[1:]

# ------------------------------------------------------------------------------------------------------

# Tuplas / Diccionarios / Sets

# coordenada = (1, 5)
# person = ("Alicee", "Smith", 24, True)

# person = {                Esto es tipo diccionario por que tiene una lista de parejas.
#     "name": "Alice",
#     "age": 20,
#     "city": "Alicante"
# }

# data = {"Alice", 20, "Alicante"}   Esto es un set por que no tiene parejas solo valores.

# person_name = person["name"]
# print(f"Nombre: {person_name}")

# print(f"Nombre: {person['name']}")    Aqui da error si ponemos las comillas dobles asi que ponemos comillas simples.
# Puedo cambiar los valores de un diccionario: person["age"] = 21   /   Como ya existe la clave "age" solo cambia su valor.
# Puedo añadir mas elementos al diccionario: person["color"] = "blue" / Si no existe el elemento añade esa clave y su valor.

# print(person.keys()) # Me devuelve una lista con las claves del diccionario.
# rint(person.values()) # Me devuelve una lista con los valores del diccionario.

# Añadimos un elemento mas al diccionario que a su vez es otro diccionario: 
#
# person["pets"] = {
#     "dog": "Otto",
#     "cat": "Mini"
# }
#

# Para acceder a esos diccionarios deberiamos de hacer lo siguiente: 
# dog_name = person["pets"]["dog"]




