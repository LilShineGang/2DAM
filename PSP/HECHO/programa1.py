# 1.Sumar los numeros pares de 2 digitos. Mostrar el resultado final.

# Genera los numeros del 10 al 99 en pasos de 2 dígitos, los suma y los printea.
# suma = sum(range(10, 100, 2))
# print(suma)

# x = 0
# for i in range (10,100):
#     if i % 2 == 0:
#         x += i

# print(f"La suma de los números de 2 dígitos es {x}")

# Resumido y en una sola línea: 
# print(f"La suma de los números de 2 dígitos es {sum([i for i in range(10, 100) if i % 2 == 0])}")

# ---------------------------------------------------------------------------------------------------------------------

# 2.Mostrar los números impares que hay desde el número 103(incluido)al número 137 (incluido)
'''
# Un número es impar si al dividirlo por 2 el resto es 1 (n % 2 == 1).
# Empezamos en 103 y avanzamos de 2 en 2: 103, 105, 107, ... hasta llegar a 137.
# Avanzar de 2 en 2 garantiza que mantenemos la paridad (impar → impar).

Mi manera:

impares = list(range(103, 138, 2))
print(impares)

Manera del profesor:

for num in range (103, 138):
    if num % 2 != 0:
        print(num, end=" - ")
print()

Resumido y en una sola línea:

print(", ".join([str(num) for num in range(103, 138) if num % 2 != 0]))
'''

# ---------------------------------------------------------------------------------------------------------------------

# 3. Dada la siguiente lista de nombres: -["Alice", "Bob", "Mary"]=.
# Escribe un programa en Python que calcule el promedio del número de letras de la lista de nombres.

'''
Mi manera: 

nombres = ["Alice", "Bob", "Mary"]
total_letras = sum(len(nombre) for nombre in nombres)
promedio = total_letras / len(nombres)
print(f"El promedio del número de letras es: {promedio}")

Manera del profesor: 

acc = 0
for nombre in nombres:
    acc += len(nombre)

print(f"El promedio del número de letras es: {acc / len(nombres)}")

Con esto convertimos los nombres en una lista de números que representan la cantidad de letras de cada nombre.

sum([len(nombre) for nombre in nombres])

'''

# ---------------------------------------------------------------------------------------------------------------------

# 4. Escribe un programa en Python que muestre de forma amigable las temperaturas máximas como números enteros
# (usa la función int para convertir un número real a entero)(recorrer el diccionario en un bucle for).
# b) Añade al programa anterior el cálculo de la temperatura media de la semana.
'''
temperaturas = {
    "lunes": 31.3,
    "martes": 29.5,
    "miércoles": 32.0,
    "jueves": 27.1,
    "viernes": 27.5,
    "sábado": 26.8,
    "domingo": 25.9
}

acc = 0

for day, temp in temperaturas.items():
    acc += temp
    print(f"\t{day}\t{int(temp)} ºC")
print(f"Temperatura media: {int(acc / len(temperaturas))} ºC")
'''

# ---------------------------------------------------------------------------------------------------------------------

# 5. Dado el siguiente diccionario que representa las temperaturas máximas y mínimas de una semana,
# escribe un programa en Python que muestre la información del diccionario de forma amigable.
# Luego añade al programa anterior el cálculo de la temperatura media mínima y máxima de la semana.

temperaturas = {
    "lunes": (22.5, 31.3),
    "martes": (20.2, 29.5),
    "miércoles": (23.2, 32.0),
    "jueves": (20.7, 27.1),
    "viernes": (21.8, 27.5),
    "sábado": (22.0, 26.8),
    "domingo": (19.9, 25.9)
}




