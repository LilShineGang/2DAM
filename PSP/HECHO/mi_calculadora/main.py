from operaciones.calc import suma


if __name__ == "__main__":
	num1_str = input("Dame un número: ")
	num1 = int(num1_str)

	num2_str = input("Dame otro número: ")
	num2 = int(num2_str)

	res_suma = suma(num1, num2)
	print(f"Resultado: {res_suma}")


'''

 Si pusieramos en la importación en vez de operaciones.calc,
 luego tendríamos que poner abajo en vez de suma, calc.suma.

 Las herencias se ponen entre parentesis indicandole el nombre
 de la clase de la cual hereda. 
 Ej:
 class Estudiante(Persona)...
 					^

'''